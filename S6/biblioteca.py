#Programa: Sistema sencillo de gestión de biblioteca

#Diccionario principal: cada clave es el título del libro y el valor es otro diccionario con autor y cantidad disponible
biblioteca = {
    "Cien años de soledad": {"autor": "Gabriel García Márquez", "disponibles": 4},
    "Don Quijote": {"autor": "Miguel de Cervantes", "disponibles": 2},
    "El principito": {"autor": "Antoine de Saint-Exupéry", "disponibles": 5}
}

#Bucle principal del programa
while True:
    print("\n=== MENÚ DE LA BIBLIOTECA ===")
    print("1. Ver libros")
    print("2. Insertar nuevo libro")
    print("3. Modificar libro existente")
    print("4. Eliminar libro")
    print("5. Calcular estadísticas")
    print("0. Salir")

    opcion = input("Elige una opción: ")

    #Ver todos los libros
    if opcion == "1":
        if len(biblioteca) == 0: #len mira cuántos elementos hay en el diccionario
            print("No hay libros registrados.")
        else:
            print("\n--- LISTADO DE LIBROS ---")
            #Recorremos el diccionario con un bucle for y usamos items() para obtener clave y valor
            for titulo, datos in biblioteca.items():
                print(f"Título: {titulo} | Autor: {datos['autor']} | Disponibles: {datos['disponibles']}")

    #Insertar nuevo libro
    elif opcion == "2":
        titulo = input("Introduce el título del libro: ").strip()
        autor = input("Introduce el autor del libro: ").strip()
        try:
            disponibles = int(input("Introduce cuántos ejemplares hay disponibles: "))
        except ValueError:
            print("Error: Debes introducir un número entero para la cantidad.")
            continue

        #Insertamos en el diccionario
        biblioteca[titulo] = {"autor": autor, "disponibles": disponibles}
        print(f"Libro '{titulo}' añadido correctamente.")

    #Modificar libro existente
    elif opcion == "3":
        titulo = input("Introduce el título del libro que deseas modificar: ").strip()
        if titulo in biblioteca:
            print(f"Libro encontrado: {titulo} - Autor: {biblioteca[titulo]['autor']} - Disponibles: {biblioteca[titulo]['disponibles']}")
            nuevo_autor = input("Nuevo autor (deja vacío si no quieres cambiarlo): ").strip()
            if nuevo_autor != "": #Si el usuario introduce algo, cambiamos el autor
                biblioteca[titulo]['autor'] = nuevo_autor #Actualizamos el autor
            try:
                nuevo_disp = input("Nueva cantidad disponible (deja vacío si no quieres cambiarla): ").strip()
                if nuevo_disp != "":
                    biblioteca[titulo]['disponibles'] = int(nuevo_disp)
            except ValueError:
                print("Error: cantidad no válida. No se cambió la cantidad.")
            print("Libro modificado correctamente.")
        else:
            print("Ese libro no se encuentra en la biblioteca.")

    #Eliminar libro
    elif opcion == "4":
        titulo = input("Introduce el título del libro que deseas eliminar: ").strip()
        if titulo in biblioteca:
            del biblioteca[titulo]
            print(f"Libro '{titulo}' eliminado correctamente.")
        else:
            print("No se encontró ese libro en la biblioteca.")

    #Calcular estadísticas
    elif opcion == "5":
        if len(biblioteca) == 0:
            print("No hay libros para calcular estadísticas.")
        else:
            total_libros = sum(datos["disponibles"] for datos in biblioteca.values()) #Sumamos las cantidades disponibles
            media_disponibles = round(total_libros / len(biblioteca), 2) #Calculamos la media y redondeamos a 2 decimales
            max_libros = max(datos["disponibles"] for datos in biblioteca.values()) #Máximo de ejemplares disponibles

            print("\n--- ESTADÍSTICAS DE LA BIBLIOTECA ---")
            print(f"Total de libros disponibles: {total_libros}")
            print(f"Media de ejemplares por libro: {media_disponibles}")
            print(f"Máximo de ejemplares de un libro: {max_libros}")

            #Adaptación personalizada: mensaje si no hay ejemplares
            if total_libros == 0:
                print("Atención: no hay libros disponibles en este momento.")

    #Salir del programa
    elif opcion == "0":
        print("Gracias por usar el sistema de biblioteca. ¡Hasta pronto!")
        break

    #Si la opción no es válida
    else:
        print("Opción no válida. Intenta de nuevo.")
