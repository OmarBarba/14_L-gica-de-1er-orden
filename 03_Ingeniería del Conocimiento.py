# Ejemplo de ingeniería del conocimiento
base_de_conocimiento = {
    "persona1": {"nombre": "Juan", "edad": 30},
    "persona2": {"nombre": "María", "edad": 25}
}

# Obtener información de una persona
persona = "persona1"
nombre = base_de_conocimiento[persona]["nombre"]
edad = base_de_conocimiento[persona]["edad"]
print(f"{nombre} tiene {edad} años.")
