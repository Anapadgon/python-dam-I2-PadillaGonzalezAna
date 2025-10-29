# Programa que usa auxprecioserror.py con manejo de errores

import auxprecioserror

def main():
    print("=== CASO 1: Lista válida ===")
    precios_correctos = [10, 20, 30, 40, 50]
    resumen1 = auxprecioserror.resumen(precios_correctos)
    total1 = auxprecioserror.total_precios(precios_correctos)
    print("Resultado resumen:", resumen1)
    print("Total de precios:", total1)
    print()

    print("=== CASO 2: Lista con error (uno no es número) ===")
    precios_erroneos = [10, "hola", 30]
    resumen2 = auxprecioserror.resumen(precios_erroneos)
    total2 = auxprecioserror.total_precios(precios_erroneos)
    print("Resultado resumen:", resumen2)
    print("Total de precios:", total2)
    print()

    print("=== CASO 3: Lista vacía ===")
    precios_vacios = []
    resumen3 = auxprecioserror.resumen(precios_vacios)
    total3 = auxprecioserror.total_precios(precios_vacios)
    print("Resultado resumen:", resumen3)
    print("Total de precios:", total3)
    print()

if __name__ == "__main__":
    main()
