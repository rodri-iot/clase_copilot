# CASO 1: Código con bug simple (ideal para /explain y /fix)
# Objetivo: sumar números de una lista. Hay un error intencional.

def sumar_lista(numeros):
    # BUG: uso de variable equivocada y ausencia de validaciones
    suma = 0
    for n in numeros:  # <--- debería ser "numeros"
        suma += n
    return suma

if __name__ == "__main__":
    print("CASO 1 -> suma:", sumar_lista([1, 2, 3, 4]))



"""
@selection /explain
Rol: desarrollador senior.
Objetivo: detectar errores y posibles riesgos.
"""

"""
@selection /fix
//mostrar-ejemplo
Rol: desarrollador Python.
Objetivo: corregir bug y agregar validaciones básicas (lista vacía, tipos).
"""