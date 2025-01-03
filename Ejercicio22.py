'''Leer 10 numeros e imprimir cuantos son positivos, negativos y neutros'''
import os # Importacion de modulos
# Definicion de funciones
def clear():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def entrada():
    cont_positivos = 0
    cont_negativos = 0
    cont_neutros = 0
    for i in range(10):
        n = int(input('Escriba un numero: '))
        if n == 0:
            cont_neutros = cont_neutros + 1
        elif n > 0:
            cont_positivos = cont_positivos + 1
        else:
            cont_negativos = cont_negativos + 1
    return cont_positivos, cont_negativos, cont_neutros

def salida(cont_positivos, cont_negativos, cont_neutros):
    print(f'Cantidad de positivos: {cont_positivos}\nCantidad de negativos: {cont_negativos}\nCantidad de neutros: {cont_neutros}')

if __name__ == '__main__':
    clear()
    cont_positivos, cont_negativos, cont_neutros = entrada()
    salida(cont_positivos, cont_negativos, cont_neutros)