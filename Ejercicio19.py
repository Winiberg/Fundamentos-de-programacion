# Ciclos
# Numero determinado de iteraciones
def para(): 
    for i in range(1, 11):
        print(i)

# Numero indeterminado de itenaciones
def mientras_hacer():
    i = 1
    while i <= 10:
        print(i)
        i = i + 1

def repetir_hasta_que(): 
    i = 1
    while True:
        print(i)
        i = i + 1
        if i > 10:
            break

if __name__ == '__main__':
    repetir_hasta_que()
    
