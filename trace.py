import json
import time
from hashlib import sha256
from pathlib import Path

def guardar_traza(nombre_entrada, texto_salida, cambios):
    traza = {
        "archivo": nombre_entrada,
        "marca_tiempo": time.ctime(),
        "hash_entrada": sha256(Path(nombre_entrada).read_bytes()).hexdigest(),
        "hash_salida": sha256(texto_salida.encode("utf-8")).hexdigest(),
        "acciones": cambios
    }

    Path("traza.json").write_text(json.dumps(traza, indent=2), encoding="utf-8")
    return "traza.json guardada correctamente"
