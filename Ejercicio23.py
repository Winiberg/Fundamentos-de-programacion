'''Suponga que se tiene un conjunto de calificaciones de un grupo de 10 alumnos. Realizar un algoritmo
para calcular la calificación promedio y la calificacion mas baja de todo el grupo'''
# Importacion de modulos
import os
# Funciones
def clear(): # Limpia pantalla al ejecutar
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def cc(): # Captura notas, calcula promedio y nota mas baja
    suma = 0
    mas_baja = 999

    for i in range (1, 11):
        nota = float(input(f"Nota {i}: ")) # Captura notas
        
        suma = suma + nota
        if nota < mas_baja: # Calcula la nota mas baja
            mas_baja = nota
    promedio = suma / 10 # Calcula el promedio de las notas
    return mas_baja, promedio

def muestra(mas_baja, promedio): # Muestra resultado en pantalla
    print(f"Promedio de notas: {promedio}\nNota mas baja: {mas_baja}")

# Codigo principal
if __name__ == '__main__':
    clear()
    mas_baja, promedio = cc()
    muestra(mas_baja, promedio)