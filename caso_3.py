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
    # Sugerencia para Copilot: devolver top-k palabras como lista de tuplas ordenada
    return conteo

# TODO: /optimize proponer uso de collections.Counter, normalización más robusta,
#       quitar signos de puntuación, soportar diferentes idiomas, etc.


"""
@selection /optimize
//mostrar-ejemplo
Rol: data engineer.
Objetivo: optimizar usando collections.Counter.
Restricciones: devolver top_k palabras, limpiar puntuación.
"""