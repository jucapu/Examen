import random

def generar_numeros_aleatorios():
    numeros_aleatorios = [random.randint(1, 100) for _ in range(10)]
    print("Números aleatorios generados:", numeros_aleatorios)
    return numeros_aleatorios

# Llamamos a la función

numeros_aleatorios = generar_numeros_aleatorios()
def eliminar_repetidos(lista):
    numeros_no_repetidos = list(set(lista))
    print("Números no repetidos:", numeros_no_repetidos)
    return numeros_no_repetidos

# Llamamos a la función con la lista generada anteriormente
numeros_no_repetidos = eliminar_repetidos(numeros_aleatorios)

def ordenar_listas(lista):
    lista_mayor_a_menor = sorted(lista, reverse=True)
    lista_menor_a_mayor = sorted(lista)
    print("Lista ordenada de mayor a menor:", lista_mayor_a_menor)
    print("Lista ordenada de menor a mayor:", lista_menor_a_mayor)
    return lista_mayor_a_menor, lista_menor_a_mayor

# Llamamos a la función con la lista de números no repetidos
lista_mayor_a_menor, lista_menor_a_mayor = ordenar_listas(numeros_no_repetidos)

def encontrar_mayor_par(lista):
    numeros_pares = [num for num in lista if num % 2 == 0]
    if numeros_pares:
        mayor_par = max(numeros_pares)
        print("El mayor número par es:", mayor_par)
        return mayor_par
    else:
        print("No hay números pares en la lista.")
        return None

# Llamamos a la función con la lista de números no repetidos
mayor_numero_par = encontrar_mayor_par(numeros_no_repetidos)


