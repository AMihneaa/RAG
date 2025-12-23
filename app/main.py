from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.routes import router as chat_router


def create_app() -> FastAPI:
    app = FastAPI(title="Ticket Assistant API", redirect_slashes=False)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:5173",
            "http://127.0.0.1:5173",
            "http://localhost:3000",
            "http://127.0.0.1:3000",
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


    app.include_router(chat_router, prefix="", tags=["chat"])

    @app.get("/health")
    def health_check():
        return {"status": "ok"}

    return app


app = create_app()

if __name__ == "__main__":
    import uvicorn

    print("Pornesc API-ul LLM pe http://localhost:8001 ...")
    uvicorn.run("app.main:app", host="0.0.0.0", port=8001, reload=True)

#python -m uvicorn app.main:app --reload
