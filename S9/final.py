# Usamos el módulo random para generar valores aleatorios
import random

# -----------------------------------------------------------
# Función 1: Crear personaje
# Recibe nombre y clase del personaje y devuelve un diccionario.
# -----------------------------------------------------------
def crear_personaje(nombre, clase):
    personaje = {
        "nombre": nombre,
        "clase": clase,
        "nivel": 1
    }
    return personaje

# -----------------------------------------------------------
# Función 2: Generar estadísticas aleatorias
# Recibe un personaje y le asigna valores de fuerza, agilidad y magia.
# Devuelve el mismo personaje modificado.
# -----------------------------------------------------------
def generar_estadisticas(personaje):
    personaje["fuerza"] = random.randint(1, 10)
    personaje["agilidad"] = random.randint(1, 10)
    personaje["magia"] = random.randint(1, 10)
    return personaje

# -----------------------------------------------------------
# Función 3: Subir de nivel
# Suma +1 al nivel del personaje y mejora una estadística aleatoria.
# Devuelve el personaje actualizado.
# -----------------------------------------------------------
def subir_nivel(personaje):
    personaje["nivel"] += 1

    # Mejora una estadística aleatoria
    stat = random.choice(["fuerza", "agilidad", "magia"])
    personaje[stat] += 1

    return personaje

# -----------------------------------------------------------
# ADAPTACIÓN
# Recibe la clase del personaje y devuelve una frase descriptiva.
# -----------------------------------------------------------
def descripcion_clase(clase):
    if clase == "Guerrero":
        return "Un valiente combatiente experto en la batalla cuerpo a cuerpo."
    elif clase == "Mago":
        return "Un sabio dominador de hechizos y energías arcanas."
    elif clase == "Arquero":
        return "Un maestro del sigilo y la puntería a larga distancia."
    else:
        return "Personaje misterioso sin clase definida."

# -----------------------------------------------------------
# Programa principal con control de errores
# -----------------------------------------------------------
print("=== GENERADOR DE PERSONAJES ===")

# Pedimos el nombre del personaje
nombre = input("Introduce el nombre del personaje: ")

# Control de errores para seleccionar clase
while True:
    print("\nElige la clase del personaje:")
    print("1. Guerrero")
    print("2. Mago")
    print("3. Arquero")

    try:
        opcion = int(input("Introduce un número (1-3): "))

        if opcion == 1:
            clase = "Guerrero"
            break
        elif opcion == 2:
            clase = "Mago"
            break
        elif opcion == 3:
            clase = "Arquero"
            break
        else:
            print("Por favor, introduce un número válido (1-3).")

    except ValueError:
        print("ERROR: Debes introducir un número, no texto.")


# Creamos el personaje
personaje = crear_personaje(nombre, clase)

# Generamos estadísticas aleatorias
personaje = generar_estadisticas(personaje)

# -----------------------------------------------------------
# Añadimos la descripción generada al personaje
# -----------------------------------------------------------
personaje["descripcion"] = descripcion_clase(clase)

# Mostramos el personaje
print("\n=== PERSONAJE CREADO ===")
print(personaje)

# Preguntamos si quiere subir de nivel
op = input("\n¿Quieres subir de nivel al personaje? (s/n): ")

if op.lower() == "s":
    personaje = subir_nivel(personaje)
    print("\n¡El personaje ha subido de nivel!")
    print(personaje)
else:
    print("\nNo se ha subido de nivel.")

print("\nPrograma finalizado.")