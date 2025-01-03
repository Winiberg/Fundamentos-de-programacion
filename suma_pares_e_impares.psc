Algoritmo suma_pares_e_impares
	Definir suma_pares, suma_impares como enteros
	suma_pares <- 0
	suma_impares <- 0
	Para i<-2 Hasta 49 Con Paso 1 Hacer
		Si i mod 2 = 0 Entonces
			suma_pares <- suma_pares + i
		SiNo
			suma_impares <- suma_impares + i
		FinSi
	FinPara
	Escribir "La suma de pares es: ",suma_pares
	Escribir "La suma de impareses: ",suma_impares
FinAlgoritmo
