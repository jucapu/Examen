# Archivo funciones.py

import random
import math

def escribir_numeros_aleatorios(n):
    numeros = [random.randint(1, 100) for _ in range(n)]
    with open("notas.txt", "a") as archivo:
        archivo.write("Números aleatorios:\n")
        for num in numeros:
            archivo.write(f"{num}\n")

def calcular_raiz_cuadrada():
    with open("notas.txt", "a") as archivo:
        archivo.write("\nRaíz cuadrada de los números:\n")
        with open("notas.txt", "r") as archivo_lectura:
            for linea in archivo_lectura:
                try:
                    num = float(linea.strip())
                    raiz = math.sqrt(num)
                    archivo.write(f"{raiz:.2f}\n")
                except ValueError:
                    pass  # Ignorar líneas no numéricas

    print("Operaciones completadas. Los resultados se han escrito en 'notas.txt'.")

# Cerrar los archivos automáticamente al salir del bloque 'with'
