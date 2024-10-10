'''Calcular calificacion final.
55% del promedio de 3 calificaciones parciales
30% de calificacion examen final
15% de la calificacion de trabajo final'''

# Importacion de modulos
import os

# Funciones
def clear(): # Limpia pantalla al ejecutar
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def captura_datos(): # Captura las calificaciones
    print('---Ingrese sus calificaciones: ---')
    parcial1 = float(input('Parcial 1: '))
    parcial2 = float(input('Parcial 2: '))
    parcial3 = float(input('Parcial 3: '))
    examen = float(input('Examen final: '))
    trabajo = float(input('Trabajo final:'))
    return  parcial1, parcial2, parcial3, examen, trabajo

def calcula_parciales(parcial1, parcial2, parcial3): # Calcula el promedio de los parciales
    nota_parciales = (parcial1 + parcial2 + parcial3)/3
    return nota_parciales
    
def calcula_calificacion_final(nota_parciales, examen, trabajo): # Calcula la calificacion final
    porcentaje_parciales = nota_parciales * 0.55
    porcentaje_examen = examen * 0.3
    porcentaje_trabajo = trabajo * 0.15
    calificacion_final = porcentaje_parciales + porcentaje_examen + porcentaje_trabajo
    return calificacion_final

def muestra_calificacion_final(calificacion_final): # Muestra la calificacion final
    print(f'Calificacion final: {calificacion_final:.2f}')

# Codigo principal
if __name__ == '__main__':
    clear()
    parcial1, parcial2, parcial3, examen, trabajo = captura_datos()
    nota_parciales = calcula_parciales(parcial1, parcial2, parcial3)
    calificacion_final = calcula_calificacion_final(nota_parciales, examen, trabajo)
    muestra_calificacion_final(calificacion_final)
