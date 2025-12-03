import json
from pathlib import Path
from hashlib import sha256
from datetime import datetime
from typing import Any, Dict, List

def calcular_hash_archivo(ruta: Path) -> str:
    """Devuelve el hash SHA-256 de un archivo."""
    return sha256(ruta.read_bytes()).hexdigest()

def calcular_hash_texto(texto: str) -> str:
    """Devuelve el hash SHA-256 de un texto."""
    return sha256(texto.encode("utf-8")).hexdigest()

def guardar_traza(nombre_entrada: str, texto_salida: str, cambios: List[str], archivo_salida: str = "traza.json") -> str:
    """Guarda una traza de cambios en un archivo JSON."""
    entrada = Path(nombre_entrada)
    salida = Path(archivo_salida)

    traza: Dict[str, Any] = {
        "archivo": nombre_entrada,
        "marca_tiempo": datetime.now().isoformat(),
        "hash_entrada": calcular_hash_archivo(entrada),
        "hash_salida": calcular_hash_texto(texto_salida),
        "acciones": cambios
    }

    # Si ya existe, acumula las trazas en una lista
    if salida.exists():
        try:
            contenido = json.loads(salida.read_text(encoding="utf-8"))
            if isinstance(contenido, list):
                contenido.append(traza)
            else:
                contenido = [contenido, traza]
        except json.JSONDecodeError:
            contenido = [traza]
    else:
        contenido = [traza]

    salida.write_text(json.dumps(contenido, indent=2, ensure_ascii=False), encoding="utf-8")
    return f"Traza guardada en {archivo_salida}"
