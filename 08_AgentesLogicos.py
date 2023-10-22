# Reglas lógicas
reglas = {
    "p": True,
    "q": False,
    "r": True,
    "not_p": lambda p: not p,
    "and_pq": lambda p, q: p and q,
    "or_pq": lambda p, q: p or q,
}

# Función para evaluar una expresión lógica
def evaluar_expresion(expresion):
    if expresion in reglas:
        return reglas[expresion]
    elif isinstance(expresion, tuple):
        operador, *operandos = expresion
        if operador in reglas:
            operandos_evaluados = [evaluar_expresion(operand) for operand in operandos]
            return reglas[operador](*operandos_evaluados)
    return None

# Función del agente lógico que responde a preguntas
def agente_logico(pregunta):
    respuesta = evaluar_expresion(pregunta)
    if respuesta is not None:
        return respuesta
    else:
        return "No puedo responder esa pregunta."

# Ejemplos de preguntas y respuestas
pregunta1 = ("and_pq", "p", "q")  # ¿p y q?
pregunta2 = ("or_pq", "p", "not_p")  # ¿p o no p?
pregunta3 = ("and_pq", "p", "r")  # ¿p y r?

respuesta1 = agente_logico(pregunta1)
respuesta2 = agente_logico(pregunta2)
respuesta3 = agente_logico(pregunta3)

print("Pregunta 1:", pregunta1, "Respuesta:", respuesta1)
print("Pregunta 2:", pregunta2, "Respuesta:", respuesta2)
print("Pregunta 3:", pregunta3, "Respuesta:", respuesta3)
