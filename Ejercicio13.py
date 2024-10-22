'''Leer 2 numeros: si son iguales que los multiplique, si el primero es mayor que el segundo que los reste y si no que los sume'''
#Importacion de modulos
import os
#Definicion de funciones
def clear():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def captura_numeros():
    n1 = int(input('Numero 1: '))
    n2 = int(input('Numero 2: '))
    return n1, n2

def proceso(n1, n2):
    if n1 == n2:
        operacion = 'multiplicacion'
        resultado = n1 * n2
    elif n1 > n2:
        operacion = 'resta'
        resultado = n1 - n2
    else:
        operacion = 'suma'
        resultado = n1 + n2
    return operacion, resultado

def muestra_resultado(operacion, resultado):
    print(f'Se realizara una {operacion}\nResultado: {resultado}')
    
#Codigo principal
if __name__ == '__main__':
    clear()
    n1, n2 = captura_numeros()
    operacion, resultado = proceso(n1, n2)
    muestra_resultado(operacion, resultado)