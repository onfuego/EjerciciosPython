def promedio(velocidad):
    contador = 0
    for i in velocidad:
        contador = contador + i
    promedio = contador / len(velocidad)
    return promedio 