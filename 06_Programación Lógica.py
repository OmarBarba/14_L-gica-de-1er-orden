# Base de conocimiento
base_de_conocimiento = {
    "padre": [("Juan", "Carlos"), ("Juan", "Maria"), ("Pedro", "Juan")],
    "hermano": [("Carlos", "Maria"), ("Carlos", "Juan")],
    "abuelo": [],
}

# Regla para inferir la relación "abuelo"
def regla_abuelo(x, z):
    global base_de_conocimiento
    for padre, hijo in base_de_conocimiento["padre"]:
        if x == padre:
            for hijo2, nieto in base_de_conocimiento["padre"]:
                if hijo == hijo2:
                    base_de_conocimiento["abuelo"].append((x, nieto))

# Consultas
def consulta(relacion, x, y):
    global base_de_conocimiento
    if relacion in base_de_conocimiento:
        if (x, y) in base_de_conocimiento[relacion]:
            return True
    if relacion == "abuelo":
        regla_abuelo(x, y)
        if (x, y) in base_de_conocimiento[relacion]:
            return True
    return False

# Consultas de relaciones
print("¿Carlos es hermano de Maria?", consulta("hermano", "Carlos", "Maria"))
print("¿Pedro es padre de Juan?", consulta("padre", "Pedro", "Juan"))
print("¿Juan es abuelo de Maria?", consulta("abuelo", "Juan", "Maria"))
