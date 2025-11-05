# Cálculo de notas de alumnos

def programa():
    alumnos = []  # Lista donde se guardan las notas

    # Pedimos cuántos alumnos hay
    try:
        n = int(input("¿Cuántos alumnos? "))
    except ValueError:
        print("Error: debes escribir un número entero.")
        return  # Salimos del programa si hay error

    # Si el número de alumnos es 0 o negativo
    if n <= 0:
        print("No hay alumnos para evaluar.")
        return

    # Pedimos las notas una a una
    for i in range(n):
        try:
            nota = int(input(f"Nota del alumno {i + 1}: "))
            if nota < 0 or nota > 10:
                print("La nota debe estar entre 0 y 10.")
                return
            alumnos.append(nota)
        except ValueError:
            print("Error: debes escribir un número válido.")
            return

    # Calculamos la media (controlando división por cero)
    if len(alumnos) == 0:
        print("No hay notas para calcular la media.")
    else:
        media = sum(alumnos) / len(alumnos)
        print("Media:", round(media, 2))

    # Mostramos los aprobados
    print("Aprobados:")
    for nota in alumnos:
        if nota >= 5:
            print(nota)


# Ejecutamos el programa
programa()
