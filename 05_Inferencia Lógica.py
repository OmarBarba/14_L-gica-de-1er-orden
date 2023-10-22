# Ejemplo de encadenamiento hacia adelante y hacia atrás
base_de_conocimiento = {
    "regla1": {"si": ["p", "q"], "entonces": "r"},
    "regla2": {"si": ["s", "t"], "entonces": "p"},
    "regla3": {"si": ["u"], "entonces": "s"},
}

hechos = ["u"]

def encadenamiento_hacia_adelante(base_conocimiento, hechos):
    nuevos_hechos = []
    while True:
        se_agregaron_nuevos_hechos = False
        for regla, datos in base_conocimiento.items():
            if all(condicion in hechos for condicion in datos["si"]) and datos["entonces"] not in hechos:
                nuevos_hechos.append(datos["entonces"])
                se_agregaron_nuevos_hechos = True
        hechos.extend(nuevos_hechos)
        if not se_agregaron_nuevos_hechos:
            break
    return hechos

def encadenamiento_hacia_atras(base_conocimiento, hechos, meta):
    if meta in hechos:
        return True
    for regla, datos in base_conocimiento.items():
        if datos["entonces"] == meta:
            if all(encadenamiento_hacia_atras(base_conocimiento, hechos, condicion) for condicion in datos["si"]):
                return True
    return False

nuevos_hechos = encadenamiento_hacia_adelante(base_de_conocimiento, hechos)
print("Hechos derivados por encadenamiento hacia adelante:", nuevos_hechos)

meta = "r"
resultado = encadenamiento_hacia_atras(base_de_conocimiento)
