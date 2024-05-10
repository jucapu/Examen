# Archivo principal (main.py)

import funciones

def main():
    # Crear o abrir el archivo "notas.txt"
    with open("notas.txt", "a") as archivo:
        pass  # No hacemos nada aquí, solo aseguramos que el archivo exista

    # Solicitar el tamaño de la lista
    try:
        n = int(input("Ingrese el tamaño de la lista: "))
    except ValueError:
        print("Debe ingresar un número válido.")
        return

    # Generar números aleatorios y escribirlos en "notas.txt"
    funciones.escribir_numeros_aleatorios(n)

    # Calcular la raíz cuadrada de los números y escribir los resultados en "notas.txt"
    funciones.calcular_raiz_cuadrada()

if __name__ == "__main__":
    main()
