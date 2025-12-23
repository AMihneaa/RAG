import httpx
import unicodedata
from langchain_core.tools import tool
from ..config import get_settings

settings = get_settings()

def strip_diacritics(s: str) -> str:
    s_norm = unicodedata.normalize("NFD", s)
    return "".join(ch for ch in s_norm if unicodedata.category(ch) != "Mn")

def fmt_transport(t: str) -> str:
    t = (t or "").upper()
    mapping = {
        "BUS": "Autobuz",
        "TRAIN": "Tren",
        "PLANE": "Avion",
        "AIRPLANE": "Avion",
    }
    return mapping.get(t, "Transport")

@tool
def get_route_options(departure: str, arrival: str) -> str:
    """
    Caută opțiuni de rute (tren / bus / avion) între două locații,
    folosind backend-ul Spring Boot.
    Returnează text "curat" pentru UI (fără diacritice, fără id-uri interne).
    """
    dep = strip_diacritics(departure).strip()
    arr = strip_diacritics(arrival).strip()

    base = settings.spring_base_url.rstrip("/")
    url = f"{base}/api/routes/options"

    print(f"[TOOL] get_route_options called with departure={dep!r}, arrival={arr!r}")
    print(f"[TOOL] HTTP GET {url}")

    try:
        resp = httpx.get(url, params={"departure": dep, "arrival": arr}, timeout=10.0)
    except Exception as e:
        msg = f"[EROARE_TOOL] Nu am putut face request la {url}: {type(e).__name__}: {e!r}"
        print(msg)
        return "Nu pot contacta serverul de rute momentan. Te rog încearcă din nou."

    if resp.status_code != 200:
        print(f"[TOOL] status={resp.status_code} body={resp.text!r}")
        return "Nu am putut obține rute acum. Te rog încearcă mai târziu."

    try:
        data = resp.json()
    except Exception:
        print(f"[TOOL] invalid json body={resp.text!r}")
        return "Serverul de rute a trimis un răspuns invalid. Te rog încearcă mai târziu."

    if not data:
        return f"Nu am găsit rute disponibile pentru {dep} → {arr}."

    # 2) Formatare "curată" pentru UI
    lines: list[str] = []
    lines.append(f"Opțiuni de rută pentru {dep} → {arr}:")

    shown = 0
    for opt in data:
        if shown >= 5:
            break

        legs = opt.get("legs") or []
        if not legs:
            continue

        shown += 1
        lines.append("")  # linie goală
        lines.append(f"Opțiunea {shown}:")

        for idx, leg in enumerate(legs, start=1):
            t = fmt_transport(leg.get("transportType"))
            stops = leg.get("stops") or []
            seats = leg.get("availableSeats", None)

            route_path = " → ".join(strip_diacritics(s).strip() for s in stops) if stops else "N/A"

            
            seats_txt = ""
            if isinstance(seats, int) or (isinstance(seats, str) and str(seats).isdigit()):
                seats_txt = f" ({seats} locuri disponibile)"

            lines.append(f"  {idx}. {t}: {route_path}{seats_txt}")

    if shown == 0:
        return f"Nu am găsit rute disponibile pentru {dep} → {arr}."

    lines.append("")
    lines.append("Dacă vrei, spune-mi dacă preferi cel mai ieftin sau cel mai rapid și îți recomand o opțiune.")

    return "\n".join(lines)
