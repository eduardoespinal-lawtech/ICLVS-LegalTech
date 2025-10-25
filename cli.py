from ingest import abrir_documento
from reasoner import revisar_clausulas
from normative_adapter import adaptar_texto
from trace import guardar_traza

def ejecutar(documento, reglas):
    # Paso 1: Leer documento
    partes = abrir_documento(documento)
    print(f"Documento cargado con {len(partes)} secciones.\n")

    # Paso 2: Revisar cláusulas
    faltantes = revisar_clausulas(partes)
    if faltantes:
        print("⚠️ Cláusulas que faltan:")
        for f in faltantes:
            print(" -", f)
    else:
        print("✅ Todas las cláusulas requeridas están presentes.")

    # Paso 3: Adaptar texto
    texto_original = "\n\n".join(partes)
    nuevo_texto, cambios = adaptar_texto(texto_original, reglas)

    # Paso 4: Guardar traza
    guardar_traza(documento, nuevo_texto, cambios)
    print("\n🔍 Traza guardada correctamente en 'traza.json'.")

# Ejemplo de uso directo (puedes modificar el texto de ejemplo)
if __name__ == "__main__":
    reglas = {
        "Governing Law": "Governing Law: California",
        "Venue": "Venue: San Francisco County"
    }
    ejecutar("samples/nda_sample.txt", reglas)
