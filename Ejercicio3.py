import time

def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        tiempo_transcurrido = fin - inicio
        print(f"Tiempo de ejecución para {func.__name__}: {tiempo_transcurrido:.6f} segundos")
        return resultado
    return wrapper

@medir_tiempo
def multiplicacion(*args):
    resultado = 1
    for num in args:
        resultado *= num
    return resultado

# Ejemplo 1
print(multiplicacion(2, 3, 4))  # Debería mostrar el resultado y el tiempo de ejecución

# Ejemplo 2
print(multiplicacion(5, 10, 2, 3))  # Debería mostrar el resultado y el tiempo de ejecución

# Ejemplo 3
print(multiplicacion(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))  # Debería mostrar el resultado y el tiempo de ejecución
