# CASO 3: Código ineficiente (ideal para /optimize)
# Objetivo: contar ocurrencias de palabras. Se puede optimizar.

def contar_palabras(texto):
    palabras = texto.lower().replace("\n", " ").split(" ")
    conteo = {}
    for p in palabras:
        if p.strip() == "":
            continue
        if p in conteo:
            conteo[p] = conteo[p] + 1
        else:
            conteo[p] = 1

    return conteo



"""
@selection /optimize
//mostrar-ejemplo
Rol: data engineer.
Objetivo: optimizar usando collections.Counter.
Restricciones: devolver top_k palabras, limpiar puntuación.
"""