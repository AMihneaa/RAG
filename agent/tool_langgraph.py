from pathlib import Path

from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader

from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

from langgraph.graph import StateGraph, MessagesState
from langgraph.prebuilt import ToolNode, tools_condition


#Config LLM
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model = os.getenv("MODEL_NAME"),
    base_url = os.getenv("LM_BASE_URL"),
    api_key = os.getenv("LM_API_KEY"),
    temperature=0.3,
    max_completion_tokens=1024
)

# Config Embeddings 
embeddings = HuggingFaceEmbeddings(model_name=os.getenv("EMB_MODEL"))


#Construim FAISS / iL incarcam

def build_or_load_index():
    DOCS_DIR = os.getenv("DOCS_DIR") 
    Path(DOCS_DIR).mkdir(exist_ok=True, parents=True)

    INDEX_DIR = os.getenv("INDEX_DIR")
    if Path(INDEX_DIR).exists():
        return FAISS.load_local(
            folder_path= INDEX_DIR,
            embeddings= embeddings,
            allow_dangerous_deserialization=True
        )

    urls = ["https://docs.langchain.com/oss/python/langgraph/agentic-rag"]
    docs = WebBaseLoader(urls).load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    chunks = splitter.split_documents(docs)

    vs_ = FAISS.from_documents(chunks, embeddings)
    vs_.save_local(INDEX_DIR)
    return vs_

vs = build_or_load_index()

@tool
def rag_search(query: str) -> str:
    """
    Caută în indexul FAISS fragmente relevante pentru întrebare
    și întoarce contextul concatenat, numerotat [1], [2], etc.
    """
    docs = vs.similarity_search(query, k=4)
    if not docs:
        return "Nu am găsit fragmente relevante în index."

    context = "\n\n".join(
        f"[{i+1}] {d.page_content}" for i, d in enumerate(docs)
    )
    return context


tools = [rag_search]
model_with_tools = llm.bind_tools(tools)


def call_model(state: MessagesState):
    system_prompt = (
        "Ești un asistent care ajută utilizatorul să înțeleagă LangGraph, LangChain și RAG.\n"
        "- Dacă întrebarea este despre concepte, cod sau documentație LangGraph/LangChain, "
        "folosește tool-ul `rag_search` pentru a căuta în documentație.\n"
        "- După ce folosești tool-ul, sintetizează răspunsul în română, citând fragmentele relevante (ex. [1], [2]...).\n"
        "- Dacă informația nu este disponibilă în contextul primit de la tool, spune clar ce lipsește."
    )

    messages = state["messages"]
    full_messages = [SystemMessage(content=system_prompt), *messages]

    response = model_with_tools.invoke(full_messages)
    return {"messages": [response]}

tool_node = ToolNode(tools)

graph = StateGraph(MessagesState)

graph.add_node("model", call_model)
graph.add_node("tools", tool_node)

graph.set_entry_point("model")

graph.add_conditional_edges(
    "model",
    tools_condition,
    {
        "tools": "tools",       
        "__end__": "__end__",  # -> Aici e gen finalul, * FINAL_RESPONSE *, daca tool ul nu se apeleaza 
    },
)

graph.add_edge("tools", "model") 

app = graph.compile()

if __name__ == "__main__":
    state = {"messages": []}

    while True:
        q = input("\nQ> ").strip()
        if not q:
            break

        state["messages"].append(HumanMessage(content=q))

        result = app.invoke(state)
        state = result

        last_msg = result["messages"][-1]
        if isinstance(last_msg, AIMessage):
            print("\nA>", last_msg.content)
        else:
            print("\nA>", last_msg)

