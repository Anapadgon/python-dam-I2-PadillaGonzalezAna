# GESTIÓN DE PANADERÍA MERCADONA

# FUNCIÓN PARA AÑADIR UN NUEVO REGISTRO
def agregar_registro(produccion):
    dia = input("Día de la semana: ").strip()
    tipo_pan = input("Tipo de pan: ").strip()
    cantidad_str = input("Cantidad vendida: ").strip()

    if dia == "" or tipo_pan == "" or cantidad_str == "":
        print("Error: ningún campo puede estar vacío.")
        return produccion  # devolvemos la lista sin cambios

    if not cantidad_str.isdigit():
        print("Error: la cantidad debe ser un número entero positivo.")
        return produccion

    cantidad = int(cantidad_str)

    for registro in produccion:
        if registro["dia"].lower() == dia.lower() and registro["tipo_pan"].lower() == tipo_pan.lower():
            print("Error: ya existe un registro con ese día y tipo de pan.")
            return produccion

    nuevo = {"dia": dia, "tipo_pan": tipo_pan, "cantidad": cantidad}
    produccion.append(nuevo)
    print("Registro añadido correctamente.")
    return produccion  # devolvemos la lista modificada


# FUNCIÓN PARA BUSCAR UN REGISTRO POR TIPO DE PAN
def buscar_por_tipo(produccion):
    tipo = input("Introduce el tipo de pan que quieres buscar: ").strip()
    encontrados = []

    for registro in produccion:
        if registro["tipo_pan"].lower() == tipo.lower():
            encontrados.append(registro)

    if len(encontrados) == 0:
        print("No se encontraron registros para ese tipo de pan.")
    else:
        print(f"\nResultados para '{tipo}':")
        for r in encontrados:
            print(f"- Día: {r['dia']}, Cantidad: {r['cantidad']}")

    return produccion


# FUNCIÓN PARA CALCULAR LA MEDIA DE VENTAS
def calcular_media(produccion):
    if len(produccion) == 0:
        print("No hay registros para calcular la media.")
        return produccion

    suma = 0
    for registro in produccion:
        suma += registro["cantidad"]

    media = suma / len(produccion)
    print(f"La media de unidades vendidas es: {media:.2f}")
    return produccion


# FUNCIÓN PARA MOSTRAR EL PAN MÁS VENDIDO
def pan_mas_vendido(produccion):
    if len(produccion) == 0:
        print("No hay registros todavía.")
        return produccion

    mas_vendido = produccion[0]
    for r in produccion:
        if r["cantidad"] > mas_vendido["cantidad"]:
            mas_vendido = r

    print("El pan más vendido es:", mas_vendido["tipo_pan"])
    print("Unidades vendidas:", mas_vendido["cantidad"])
    return produccion


# FUNCIÓN PARA MOSTRAR TODOS LOS REGISTROS
def mostrar_todos(produccion):
    if len(produccion) == 0:
        print("No hay registros todavía.")
    else:
        print("\nLISTA DE REGISTROS:")
        for r in produccion:
            print(f"- Día: {r['dia']}, Pan: {r['tipo_pan']}, Cantidad: {r['cantidad']}")
    return produccion


# MENÚ PRINCIPAL
def menu():
    # Creamos la lista
    produccion = [
        {"dia": "Lunes", "tipo_pan": "Baguette", "cantidad": 25},
        {"dia": "Martes", "tipo_pan": "Integral", "cantidad": 30},
        {"dia": "Miércoles", "tipo_pan": "Chapata", "cantidad": 20},
        {"dia": "Jueves", "tipo_pan": "Baguette", "cantidad": 40},
        {"dia": "Viernes", "tipo_pan": "Centeno", "cantidad": 35}
    ]


    while True:
        print("\n====== MENÚ PANADERÍA ======")
        print("1. Añadir registro")
        print("2. Buscar por tipo de pan")
        print("3. Mostrar todos los registros")
        print("4. Calcular media de ventas")
        print("5. Mostrar el pan más vendido")
        print("6. Salir")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            produccion = agregar_registro(produccion)
        elif opcion == "2":
            produccion = buscar_por_tipo(produccion)
        elif opcion == "3":
            produccion = mostrar_todos(produccion)
        elif opcion == "4":
            produccion = calcular_media(produccion)
        elif opcion == "5":
            produccion = pan_mas_vendido(produccion)
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")


# EJECUTAR EL PROGRAMA
menu()
