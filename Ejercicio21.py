'''Calcular independientemente la suma de los numeros pares e impares comprendidos entre 1 y 50.'''
# Importacion de modulos
import os

# Definicion de funciones
def clear():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def proceso():
    suma_pares =  0
    suma_impares = 0
    for i in range(2, 50):
        if i % 2 == 0:
            suma_pares = suma_pares + i
        else:
            suma_impares = suma_impares + i
    return suma_pares, suma_impares

def muestra(suma_pares, suma_impares):
    print(f'Suma pares: {suma_pares}\nSuma impares: {suma_impares}')

# Codigo principal
if __name__ == '__main__':
    clear()
    suma_pares, suma_impares = proceso()
    muestra(suma_pares, suma_impares)