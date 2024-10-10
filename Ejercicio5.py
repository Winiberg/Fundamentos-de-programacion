# Calcular area y y longiud de una circunferencia a partir del radio

# Importacion de modulos
import os
import numpy as np

# Definicion de funciones
def limpia_pantalla(): # Limpia la pantalla al ejecutar
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def captura_datos(): # Captura dato en variable radio
    radio = float(input('Radio: '))
    return radio

def calcula_area(radio): # Calcula area de circunferencia
    area = np.pi * (radio**2)
    return area

def calcula_longitud(radio): # Calcula longitud de circunferencia
    longitud = 2 * np.pi * radio
    return longitud

def genera_salida(area, longitud): # Muestra en pantalla el resultado
    print(f'Area: {area} - Longitud: {longitud}')

# Codigo principal
if __name__ == '__main__':
    limpia_pantalla()
    radio = captura_datos()
    area = calcula_area(radio)
    longitud = calcula_longitud(radio)
    genera_salida(area, longitud)
