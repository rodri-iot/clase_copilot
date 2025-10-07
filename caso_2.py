# CASO 2: Código correcto pero sin tests ni documentación
# Ideal para /doc y /test

def media(numeros):
    total = 0
    for n in numeros:
        total += n
    return total / len(numeros)



"""
@selection /doc
Rol: tech writer.
Objetivo: generar docstring estilo Google.
Restricciones: sin cambiar la firma.
Validación: incluir ejemplo de uso.
"""

"""
@file /test
Rol: QA engineer.
Objetivo: crear archivo tests/test_media.py con pytest.
Casos: lista vacía, un elemento, negativos, floats.
"""