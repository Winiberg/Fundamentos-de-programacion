'''Ingresar un numero entero y reportar si es par o impar'''

# Importacion de modulos
import os
# Definición de funciones
def clear():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def captura_n():
    n = int(input('Ingrese un numero entero: '))
    return n

def determina_tipo(n):
    resultado = n % 2
    if resultado == 0:
        tipo = 'par'
    else:
        tipo = 'impar'
    return tipo

def muestra_tipo(n, tipo):
    print(f'El numero {n} es {tipo}')

# Codigo principal
if __name__ == '__main__':
    clear()
    n = captura_n()
    tipo = determina_tipo(n)
    muestra_tipo(n, tipo)