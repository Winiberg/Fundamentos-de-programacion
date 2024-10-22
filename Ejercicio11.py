'''Determina si un alumno aprueba o reprueba un curso,
sabiendo que aprobara si su promedio de tres calificaciones
es mayor o igual a 4; reprueba en caso contrario'''

#Importacion de modulos
import os

#Definicion de funciones
def clear():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def captura_calificaciones():
    c1 = float(input('Nota 1: '))
    c2 = float(input('Nota 2: '))
    c3 = float(input('Nota 3: '))
    return c1, c2, c3

def calcula_promedio(c1, c2, c3):
    promedio = (c1 + c2 + c3)/3
    return promedio

def determina_resultado(promedio):
    if promedio >= 4:
        resultado = 'Aprobado'
    else:
        resultado = 'Reprobado'
    return resultado

def muestra_resultado(promedio, resultado):
    print(f'Nota final: {promedio:.2f}\nResultado: {resultado}')

#Codigo principal
if __name__ == '__main__':
    clear()
    c1, c2, c3 = captura_calificaciones()
    promedio = calcula_promedio(c1, c2, c3)
    resultado = determina_resultado(promedio)
    muestra_resultado(promedio, resultado)