# Escribe la ecuacion cuadratica de forma algoritmica
import os
import math

def limpia_pantalla():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def captura_datos():
    a = float(input('a: '))
    b = float(input('b: '))
    c = float(input('c: '))
    return a,b,c

def calcula(a,b,c):
    resultado = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
    return resultado

def muestra_resultado(resultado):
    print (f'Resultado: {resultado:.2}')

if __name__ == '__main__':
    limpia_pantalla()
    a, b, c = captura_datos()
    resultado = calcula(a,b,c)
    muestra_resultado(resultado)


