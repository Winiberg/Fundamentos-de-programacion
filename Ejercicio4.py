# Calcular la cantidad de segundos que estan incluidos en el numero de h. min. y seg. ingresados por el usuario

# importación de modulos
import os
# Definicion de funciones
def limpia_pantalla(): # Limpia pantalla al ejecutar programa
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def captura_datos(): # Captura los datos ingresados por el usuario
    horas = int(input('Horas: '))
    minutos = int(input('Minutos: '))
    segundos = int(input('Segundos: '))
    return horas, minutos, segundos

def horas_a_seg(horas): # Convierte horas a segundos
    horas_en_segundos = horas * 3600
    return horas_en_segundos

def minutos_a_segundos(minutos): # Convierte minutos a segundos
    minutos_en_segundos = minutos * 60
    return minutos_en_segundos

def suma_seg(horas_en_segundos, minutos_en_segundos, segundos): # Suma el total de segundos
    total_seg = horas_en_segundos + minutos_en_segundos + segundos
    return total_seg

def genera_salida(total_seg): # Muestra en pantalla el resultado
    print(f'Los segundos equivalentes son: {total_seg}')

# Codigo principal
if __name__ == '__main__':
    limpia_pantalla()
    horas, minutos, segundos = captura_datos()
    horas_en_segundos = horas_a_seg(horas)
    minutos_en_segundos = minutos_a_segundos(minutos)
    total_seg = suma_seg(horas_en_segundos, minutos_en_segundos, segundos)
    genera_salida(total_seg)

