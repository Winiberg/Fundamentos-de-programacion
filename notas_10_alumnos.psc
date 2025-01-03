Algoritmo notas_10_alumnos
	Definir calificacion_promedio, calificacion_baja Como Real;
	Definir calificacion, suma como real;
	Definir i Como Entero;
	
	suma <- 0;
	calificacion_baja <- 99999;
	
	Para i<-1 Hasta 10 Con Paso 1 Hacer
		Escribir i,". Digite una calificacion: ";
		Leer calificacion;
		
		//Suma iterativa de las calificaciones
		suma <- suma + calificacion;
		Si calificacion < calificacion_baja Entonces
			calificación_baja <- calificacion;
		FinSi
	FinPara
	
	calificacion_promedio <- suma/10;
	
	Escribir "Promedio de notas: ",calificacion_promedio
	Escribir "Nota mas baja: ",calificacion_baja
FinAlgoritmo
