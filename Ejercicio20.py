# Calcular la suma de los "N" primeros numeros
# Importacion de modulos
import os
# Definicion de funciones
def clear():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def captura_n():
    n = int(input('Digite la cantidad de numeros a sumarse: '))
    return n

def proceso(n):
    suma = 0
    for i in range(1, n+1):
        suma = suma + i
    return suma

def muestra(suma):
    print(suma)
# Codigo principal
if __name__ == '__main__':
    clear()
    n = captura_n()
    suma = proceso(n)
    muestra(suma)