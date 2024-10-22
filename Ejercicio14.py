'''Leer 3 numeros diferentes e imprimir el numero mayor de los tres'''
#Importacion de modulos
import os
#Definicion de funciones
def clear():#Limpia la pantalla al ejecutar
    if os.name == 'posix':
        os,system('clear')
    else:
        os.system('cls')

def captura_datos():#Captura el valor de las variables
    n1 = int(input('Numero 1: '))
    n2 = int(input('Numero 2: '))
    n3 = int(input('Numero 3: '))
    return n1, n2, n3

def evalua(n1, n2, n3):#Evalua que numero es mayor
    if (n1 > n2) and (n1 > n3):
        numero = n1
    elif (n2 > n1) and (n2 > n3):
        numero = n2
    else:
        numero = n3
    return numero

def muestra(numero):#Muestra en numero mayor
    print(f'{numero} es el mayor')
#Codigo principal
if __name__ == '__main__':
    clear()
    n1, n2, n3 = captura_datos()
    numero = evalua(n1, n2, n3)
    muestra(numero)