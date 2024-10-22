'''Elaborar un programa que me muestre el significado de aniversario de cada decada hasta los 60
Bodasde hojalata    10 años
Bodas de porcelana  20 años
Bodas de perlas     30 años
Bodas de rubi       40 años
Bodas de oro        50 años
Bodas de diamante   60 años'''
#Importacion de modulos
import os
#Definicion de funciones
def clear():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def captura_anios():
    anios = int(input('Anios: '))
    return anios

def evalua_aniversario(anios):
    if anios == 10:
        aniversario = 'Bodas de Hojalata'
    elif anios == 20:
        aniversario = 'Bodas de Porcelana'
    elif anios == 30:
        aniversario = 'Bodas de Perlas'
    elif anios == 40:
        aniversario = 'Bodas de Rubi'
    elif anios == 50:
        aniversario = 'Bodas de Oro'
    elif anios == 60:
        aniversario = 'Bodas de Diamante'
    else:
        aniversario = 'Decada no existente'
    return aniversario

def muestra(aniversario):
    print(aniversario)
#Codigo principal
if __name__ == '__main__':
    clear()
    anios = captura_anios()
    aniversario = evalua_aniversario(anios)
    muestra(aniversario)