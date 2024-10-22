'''Hacer un programa que tenga un menu con las siguientes opciones:
Opcion 1: Elevar un numero a una potencia X
Opcion 2: Sacar la raiz cuadrada de un numero
Opcion 3: Salir'''
#Importacion de modulos
import os
import math
#Definicion de funciones
def clear():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def captura_opciones():
    print('Ingrese una opcion\nOpcion 1: Elevar un numero a una potencia x\nOpcion 2: Sacar la raiz cuadrada de un numero\nOpcion 3: Salir')
    opcion =  int(input('Opcion: '))
    return opcion

def eleva_n_a_ex():
    n = int(input('Ingrese un numero: '))
    ex = int(input('Ingrese un exponente: '))
    resultado = n**ex
    return resultado

def raiz_cuadrada():
    n = int(input('Ingrese un numero: '))
    resultado = math.sqrt(n)
    return resultado

def proceso(opcion):
    if opcion == 1:
        resultado = eleva_n_a_ex()
    elif opcion == 2:
        resultado = raiz_cuadrada()
    elif opcion == 3:
        resultado = 'Fin proceso'
    else:
        resultado = 'Opcion no valida'
    return resultado

def muestra(resultado):
    print(resultado)

#Codigo principal
if __name__ == '__main__':
    clear()
    opcion = captura_opciones()
    resultado = proceso(opcion)
    muestra(resultado)