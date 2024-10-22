'''Elaborar un programa que me muestre los dias de la semana cuando ingrese los siete primeros numeros'''
#Importacion de modulos
import os
#Definicion de funciones
def clear():#Limpia la pantalla al ejecutar
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def captura_numero():#Captura la variable n
    n = int(input('Ingrese un numero del 1 al 7: '))
    return n

def evalua_numero(n):#Evalua a que dia de la semana corresponde la variable n
    if n == 1:
        dia = 'Lunes'
    elif n == 2:
        dia = 'Martes'
    elif n == 3:
        dia = 'Miercoles'
    elif n == 4:
        dia = 'Jueves'
    elif n == 5:
        dia = 'Viernes'
    elif n == 6:
        dia = 'Sabado'
    elif n == 7:
        dia = 'Domingo'
    else:
        dia = 'No existe dia para ese numero'
    return dia

def muestra(dia):#Muestra el dia de la semana correspondiente a la variable n
    print(dia)
#Codigo principal
if __name__ == '__main__':
    clear()
    n = captura_numero()
    dia = evalua_numero(n)
    muestra(dia)