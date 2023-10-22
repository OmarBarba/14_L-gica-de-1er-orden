# Definición de un dominio (por ejemplo, un conjunto de números enteros)
dominio = range(-10, 11)

# Cuantificador "Para todo" (∀)
def para_todo(cuantificador, dominio, condicion):
    for elemento in dominio:
        if not condicion(elemento):
            return False
    return True

# Cuantificador "Existe" (∃)
def existe_un(cuantificador, dominio, condicion):
    for elemento in dominio:
        if condicion(elemento):
            return True
    return False

# Ejemplos de fórmulas con cuantificadores
formula_para_todo = para_todo(1, dominio, lambda x: x > 0)
formula_existe_un = existe_un(1, dominio, lambda x: x < 0)

# Resultados
print("¿x > 0 para todo x es verdadero?", formula_para_todo)
print("¿Hay un y < 0 que existe?", formula_existe_un)
