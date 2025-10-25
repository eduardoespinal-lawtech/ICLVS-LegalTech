def adaptar_texto(texto, reglas):
    cambios = []
    resultado = texto

    for palabra, reemplazo in reglas.items():
        if palabra.lower() in resultado.lower():
            resultado = resultado.replace(palabra, reemplazo)
            cambios.append(f"Sustituido '{palabra}' por '{reemplazo}'")
        else:
            resultado += f"\n\n{reemplazo}"
            cambios.append(f"Insertado '{reemplazo}'")

    return resultado, cambios
