Algoritmo Factorial_de_un_numero
	Definir num como entero
	Definir i, factorial como enteros
	Repetir
		Escribir "Digite un numero: "
		Leer num
	Hasta Que num>0
	i <- 1
	factorial <- 1
	Mientras i <=num Hacer
		factorial <- factorial * i
		i <- i + 1
	FinMientras
	Escribir "El factorial de ",num," es: ",factorial
FinAlgoritmo
