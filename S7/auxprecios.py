# auxprecios.py
# Módulo sencillo para analizar listas de precios

def mostrar_precios(precios):
    """Muestra todos los precios uno por uno."""
    for p in precios:
        print(p)

def precio_maximo(precios):
    """Devuelve el precio más alto."""
    return max(precios)

def precio_minimo(precios):
    """Devuelve el precio más bajo."""
    return min(precios)

def promedio_precios(precios):
    """Devuelve el promedio (media) de los precios."""
    return sum(precios) / len(precios)

def aumentar_precios(precios, porcentaje):
    """Devuelve una nueva lista con los precios aumentados según el porcentaje indicado."""
    nueva_lista = []
    for p in precios:
        nuevo_precio = p + (p * porcentaje / 100)
        nueva_lista.append(nuevo_precio)
    return nueva_lista

def resumen(precios):
    """Devuelve un pequeño resumen con el máximo, mínimo y promedio."""
    maximo = precio_maximo(precios)
    minimo = precio_minimo(precios)
    promedio = promedio_precios(precios)
    return {"maximo": maximo, "minimo": minimo, "promedio": promedio}

# ---- Adaptación personal ----
def contar_mayores(precios, limite):
    """Cuenta cuántos precios son mayores que el valor dado"""
    contador = 0
    for p in precios:
        if p > limite:
            contador += 1
    return contador
