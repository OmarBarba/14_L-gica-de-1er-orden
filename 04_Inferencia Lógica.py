# Ejemplo de unificación en inferencia lógica
def unificar(termino1, termino2, sustitucion={}):
    if sustitucion is None:
        return None
    elif termino1 == termino2:
        return sustitucion
    elif isinstance(termino1, str):
        return unificar_variable(termino1, termino2, sustitucion)
    elif isinstance(termino2, str):
        return unificar_variable(termino2, termino1, sustitucion)
    elif isinstance(termino1, list) and isinstance(termino2, list):
        return unificar(termino1[1:], termino2[1:], unificar(termino1[0], termino2[0], sustitucion))
    else:
        return None

def unificar_variable(variable, termino, sustitucion):
    if variable in sustitucion:
        return unificar(sustitucion[variable], termino, sustitucion)
    elif termino in sustitucion:
        return unificar(variable, sustitucion[termino], sustitucion)
    else:
        sustitucion[variable] = termino
        return sustitucion

# Ejemplo de unificación
termino1 = ["padre", "Juan", "Maria"]
termino2 = ["padre", "x", "y"]
sustitucion = unificar(termino1, termino2)
print("Sustitución:", sustitucion)
