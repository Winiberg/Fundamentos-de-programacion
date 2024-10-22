''' En un almacen se hace un 205 de descuento a los clientes cuya compra supere los $100. ¿Cual es la cantidad que pagara una persona por su compra?'''
#Importacion de modulos
import os
#Definicion de funciones
def clear():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def captura_datos():
    compra = int(input('Valor de la compra: $'))
    return compra

def determina_descuento(compra):
    if compra > 100:
        descuento = (compra*20)/100
    else:
        descuento = 0
    return descuento

def aplica_descuento(compra, descuento):
    total_pagar = compra - descuento
    return total_pagar

def muestra_total_a_pagar(total_pagar):
    print(f'Total a pagar: ${total_pagar}')
#Codigo principal
if __name__ == '__main__':
    clear()
    compra = captura_datos()
    descuento = determina_descuento(compra)
    total_pagar = aplica_descuento(compra, descuento)
    muestra_total_a_pagar(total_pagar)