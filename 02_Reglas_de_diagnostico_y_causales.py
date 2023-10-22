# Ejemplo de reglas de diagnóstico y causales
def verificar_sintomas(sintomas):
    if "fiebre" in sintomas and "tos" in sintomas:
        return "Posible infección"
    elif "dolor_de_garganta" in sintomas:
        return "Irritación de garganta"
    else:
        return "Sin diagnóstico"

sintomas_paciente = ["fiebre", "tos"]
resultado = verificar_sintomas(sintomas_paciente)
print("Diagnóstico:", resultado)
