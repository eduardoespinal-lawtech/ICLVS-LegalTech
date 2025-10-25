from pathlib import Path

def abrir_documento(ruta):
    texto = Path(ruta).read_text(encoding="utf-8")
    partes = [p.strip() for p in texto.split("\n\n") if p.strip()]
    return partes
