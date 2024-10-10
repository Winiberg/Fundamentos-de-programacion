'''Un profesor prepara tres cuestionarios para una
evaluacion final: A, B Y C. Se sabe que se tarda 5 
minutos en revisar el cuestionario A, 8 el B y 6 el C.
La cantidad de examenes de cada tipo se entran por teclado.
¿Cuantas horas y cuantos minutos se tardara en revisar
las evaluaciones?'''

# Importacion de modulos
import os
import math

# Funciones
def limpiar_pantalla(): # Limpia la pantalla al ejecutar
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def captura_datos(): # Captura la cantidad de cuestionarios por tipo
    cant_a = int(input('Cantidad de cuestionarios tipo A: '))
    cant_b = int(input('Cantidad de cuestionarios tipo B: '))
    cant_c = int(input('Cantidad de cuestionarios tipo C: '))
    return cant_a, cant_b, cant_c

def calcula_tiempo_a(cant_a): # Calcula el tiempo de revision de cuestionarios tipo A en minutos
    tiempo_a = cant_a * 5
    return tiempo_a

def calcula_tiempo_b(cant_b): # Calcula el tiempo de revision de cuestionarios tipo B en minutos
    tiempo_b = cant_b * 8
    return tiempo_b

def calcula_tiempo_c(cant_c): # Calcula el tiempo de revision de cuestionarios tipo C en minutos
    tiempo_c = cant_c * 6
    return tiempo_c

def suma_minutos(tiempo_a, tiempo_b, tiempo_c): # Suma el tiempo en minutos
    total_en_minutos = tiempo_a + tiempo_b + tiempo_c
    return total_en_minutos

def calcula_horas_minutos(total_en_minutos): # Calcula el tiempo en horas y minutos
    h = (total_en_minutos / 60)
    horas = math.trunc(h)
    minutos = total_en_minutos % 60
    return horas, minutos

def genera_salida(horas, minutos): # Muestra el resultado en horas y minutos
    print(f'Tiempo de revision: {horas} h. con {minutos} min.')

# Codigo principal
if __name__ == '__main__':
    limpiar_pantalla()
    cant_a, cant_b, cant_c = captura_datos()
    tiempo_a = calcula_tiempo_a(cant_a)
    tiempo_b = calcula_tiempo_b(cant_b)
    tiempo_c = calcula_tiempo_c(cant_c)
    total_en_minutos = suma_minutos(tiempo_a, tiempo_b, tiempo_c)
    horas, minutos = calcula_horas_minutos(total_en_minutos)
    genera_salida(horas, minutos)