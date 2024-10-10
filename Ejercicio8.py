'''Una tienda ofrece un descuento del 15% sobre el total
de la compra y un cliente desea saber cuanto deberá pagar'''

# importacion de modulos
import os

# Funciones
def clear(): # Limpia la pantalla al ejecutar
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def captura_datos(): # Captura valor inicial de la compra
    compra = int(input('Valor compra: $'))
    return compra

def calcula_descuento(compra): # Calcula el total a pagar con descuento aplicado
    total_a_pagar = compra - ((compra * 15) / 100)
    return total_a_pagar

def muestra_total_pagar(total_a_pagar): # Muestra el total a pagar con descuento aplicado
    print(f'El total a pagar es: ${total_a_pagar:.1f}')

# Codigo principal
if __name__ == '__main__':
    clear()
    compra = captura_datos()
    total_a_pagar = calcula_descuento(compra)
    muestra_total_pagar(total_a_pagar)