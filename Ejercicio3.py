# Intercambiar el valor de 2 variables

# Importacion de modulos
import os

# Definicion de funciones
def limpia_pantalla(): # Limpia la pantalla al ejecutar programa
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def captura_variables(): # Captura el valor de las variables
    a = (input('a:'))
    b = (input('b:'))
    return a, b

def intercambia_variables(a, b): # Intercambia el valor de las variables
    letra_a = a
    a = b
    b = letra_a
    return a, b

def genera_salida(a,b): # Muestra en pantalla las variables con su nuevo valor
    print(f'a: {a}, b: {b}')

# Codigo principal
if __name__ == '__main__':
    limpia_pantalla()
    a, b = captura_variables()
    a, b = intercambia_variables(a, b)
    genera_salida(a, b)

