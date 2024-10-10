# Solución logica de operacion

# Importacion de modulos
import os

# Definicion de funciones

def limpiar_pantalla(): # Limpia pantalla al ejecutar
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def captura_datos(): # Entrada de a y b
    a = float(input('a: '))
    b = float(input('b: '))
    return a, b

def operacion(a,b): # Realiza operacion
    resultado = (3+5*8)<3 and (((-6/3)*4)+2<2) or (a>b)
    return resultado

def muestra_datos(resultado): # Genera la salida del resultado en pantalla
    print(resultado)

if __name__ == '__main__':
    limpiar_pantalla()
    a,b = captura_datos()
    resultado = operacion(a,b)
    muestra_datos(resultado)