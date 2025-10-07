# CASO 4: Función con requisitos ambiguos (ideal para prompting)
# Pide a Copilot que complete/aclare restricciones (constraint prompting)

def filtrar_registros(registros, campo, umbral):
    """
    Filtra registros donde registros[i][campo] > umbral.
    Preguntas clave para Copilot (role: "senior python dev"):
      - ¿Qué hacer si el campo no existe? ¿y si no es numérico?
      - ¿Debe ser > o >=?
      - ¿Se requiere manejo de NaN/None?
      - ¿Devolver lista, iterador o generador?
    """
    filtrados = []
    for r in registros:
        try:
            if r[campo] > umbral:
                filtrados.append(r)
        except Exception as e:
            # TODO: pide a Copilot estrategias de manejo de errores y logging
            pass
    return filtrados


"""
@selection
Rol: senior data engineer.
Objetivo: definir política de errores y tipado.
Restricciones: no modificar lógica principal.
Incluir manejo de KeyError, TypeError y logging.
"""