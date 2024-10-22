'''Una fruteria ofrece manzanas con descuento segun lo siguiente:
Numero de kilos comprados   % descuento
0-2                         0%
2.01-5                      10%
5.01.10                     15%
10.01 en adelante           20%     
Determinar cuanto pagara una persona que compre manzanas en esa fruteria'''
#Importacion de modulos
import os
#Definicion de funciones
def clear():#Limpia la pantalla a ejecutar
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def captura_datos():#Captura variable kilos y precio por kilo
    kilos = float(input('Kilos: '))
    precio_kilo = float(input('Precio por kilo: $'))
    return kilos, precio_kilo

def evalua_descuento(kilos, precio_kilo):#Evalua el decuento correspondiente
    if kilos <= 2:
        descuento = 0
    elif kilos >= 2.01 and kilos <= 5:
        descuento = ((kilos * precio_kilo) * 10)/100
    elif kilos >= 5.01 and kilos <= 10:
        descuento = ((kilos * precio_kilo) * 15)/100
    elif kilos >= 10.01:
        descuento = ((kilos * precio_kilo) * 20)/100
    return descuento

def aplica_descuento(kilos, precio_kilo, descuento):#Aplica el descuento a la compra
    sub_total = (kilos * precio_kilo)
    total_pagar = sub_total - descuento
    return sub_total, total_pagar

def muestra(sub_total, total_pagar):#Muestra el descuento aplicado y el total a pagar
    print(f'Sub total: ${sub_total}\nDescuento: ${descuento}\nTotal a pagar: ${total_pagar}')

#Codigo principal
if __name__ == '__main__':
    clear()
    kilos, precio_kilo = captura_datos()
    descuento = evalua_descuento(kilos, precio_kilo)
    sub_total, total_pagar = aplica_descuento(kilos, precio_kilo, descuento)
    muestra(sub_total, total_pagar)