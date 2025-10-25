def revisar_clausulas(lista):
    faltantes = []
    palabras_requeridas = ["confidential", "law", "jurisdiction"]
    texto = " ".join(lista).lower()

    for palabra in palabras_requeridas:
        if palabra not in texto:
            faltantes.append(f"Falta la palabra clave: {palabra}")

    return faltantes
