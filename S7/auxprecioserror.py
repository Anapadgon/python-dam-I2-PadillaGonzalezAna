# Módulo para analizar una lista de precios con manejo de errores

def validar_lista(precios):
    """
    Comprueba que la lista de precios sea válida.
    Lanza un error (raise) si encuentra algo incorrecto.
    """
    if not isinstance(precios, list): #si no es lista
        raise TypeError("Error: Los precios deben estar en una lista.")
    if len(precios) == 0: #si lista vacía
        raise ValueError("Error: La lista de precios está vacía.")
    for p in precios:
        if not isinstance(p, (int, float)):
            raise ValueError(f"Error: '{p}' no es un número válido.")


def precio_maximo(precios):
    """Devuelve el precio máximo, con manejo de errores."""
    try:
        validar_lista(precios)
        resultado = max(precios)
    except (TypeError, ValueError) as e:
        print(e)
        resultado = None
    else:
        print("Se calculó correctamente el precio máximo.")
    finally:
        print("→ Operación precio_maximo terminada.\n")
    return resultado


def precio_minimo(precios):
    """Devuelve el precio mínimo, con manejo de errores."""
    try:
        validar_lista(precios)
        resultado = min(precios)
    except (TypeError, ValueError) as e:
        print(e)
        resultado = None
    else:
        print("Se calculó correctamente el precio mínimo.")
    finally:
        print("→ Operación precio_minimo terminada.\n")
    return resultado


def promedio_precios(precios):
    """Devuelve el promedio (media) de los precios."""
    try:
        validar_lista(precios)
        resultado = sum(precios) / len(precios)
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero (lista vacía).")
        resultado = None
    except (TypeError, ValueError) as e:
        print(e)
        resultado = None
    else:
        print("Se calculó correctamente el promedio.")
    finally:
        print("→ Operación promedio_precios terminada.\n")
    return resultado


def resumen(precios):
    """Devuelve un resumen con el máximo, mínimo y promedio."""
    try:
        validar_lista(precios)
        maximo = precio_maximo(precios)
        minimo = precio_minimo(precios)
        promedio = promedio_precios(precios)
        if None in (maximo, minimo, promedio): #si alguno es None
            raise ValueError("Error: No se pudieron calcular todas las estadísticas.")
        resultado = {"maximo": maximo, "minimo": minimo, "promedio": promedio}
    except Exception as e: #captura cualquier error
        print("Error al generar el resumen:", e)
        resultado = None
    else:
        print("Resumen generado correctamente.")
    finally:
        print("→ Operación resumen terminada.\n")
    return resultado

# ---- Adaptación personal ----
def total_precios(precios):
    """Devuelve la suma total de los precios con manejo de errores"""
    try:
        validar_lista(precios)
        total = sum(precios)
    except (TypeError, ValueError) as e:
        print("Error al calcular el total:", e)
        total = None
    else:
        print("Total calculado correctamente.")
    finally:
        print("→ Operación total_precios terminada.\n")
    return total