# Calcular el factorial de un numero n
import os # Importacion de modulos 
def clear():# Limpia pantalla al ejecutar
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def captura_num():# Entrada
    while True:
        num = int(input("Digite un numero: "))
        if num > 0:
            return num

def calcula_factorial(num):# Calcula factorial de num
    i = 1
    factorial = 1
    while i <= num:
        factorial = factorial * i
        i = i + 1
    return factorial

def muestra(num, factorial):# Muestra el resultado en pantalla
    print(f"El factorial de {num} es: {factorial}")

if __name__ == '__main__':
    clear()
    num = captura_num()
    factorial = calcula_factorial(num)
    muestra(num, factorial)
