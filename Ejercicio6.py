# Porcentaje de hombres y mujeres en un grupo de estudiantes

# Importacion de modulos
import os

# Definicion de funciones

def limpia_pantalla():
    if os.name == 'posix':
        os.system(clear)
    else:
        os.system('cls')

def captura_datos():
    num_hombres = int(input('Hombres: '))
    num_mujeres = int(input('Mujeres: '))
    return num_hombres, num_mujeres

def suma_estudiantes(num_hombres,num_mujeres):
    total_estudiantes = num_hombres + num_mujeres
    return total_estudiantes

def porcentaje_hombres(total_estudiantes, num_hombres):
    porcentaje_h = (num_hombres * 100)/total_estudiantes
    return porcentaje_h

def porcentaje_mujeres(total_estudiantes, num_mujeres):
    porcentaje_m = (num_mujeres * 100)/total_estudiantes
    return porcentaje_m

def genera_salida(total_estudiantes, porcentaje_h, porcentaje_m):
    print(f'Total estudiantes: {total_estudiantes}\nPorcentaje de hombres: {porcentaje_h}%\nPorcentaje de mujeres: {porcentaje_m}%')

# Codigo principal
if __name__ == '__main__':
    limpia_pantalla()
    num_hombres, num_mujeres = captura_datos()
    total_estudiantes = suma_estudiantes(num_hombres, num_mujeres)
    porcentaje_h = porcentaje_hombres(total_estudiantes, num_hombres)
    porcentaje_m = porcentaje_mujeres(total_estudiantes, num_mujeres)
    genera_salida(total_estudiantes, porcentaje_h, porcentaje_m)

