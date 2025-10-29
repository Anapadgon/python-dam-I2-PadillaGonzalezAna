# precios.py
# Programa que usa auxprecios.py

from auxprecios import resumen, contar_mayores, aumentar_precios

def main():
    precios = [10, 20, 30, 40, 50]
    print("Lista original de precios:", precios)
    print("Resumen:", resumen(precios))

    # --- Adaptación personal: contar precios mayores que núm dado ---
    limite = 25
    mayores = contar_mayores(precios, limite)
    print(f"Hay {mayores} precios mayores que {limite}.")

    # Ejemplo de aumentar precios un 10%
    precios_aumentados = aumentar_precios(precios, 10)
    print("Precios aumentados 10%:", precios_aumentados)

if __name__ == "__main__":
    main()
