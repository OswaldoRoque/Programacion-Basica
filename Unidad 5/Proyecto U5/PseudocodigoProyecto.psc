Algoritmo Detectar_pasos_agua
	
	Definir Sensor Como Real
	Definir Detectar_agua Como Real
	
	Leer Sensor
	Leer Detectar_agua
	
	Si sensor=Detectar_agua entonces
		escribir "Se detecta paso de agua" Encender PIN_LED
	Sino
		escribir "NO se detecta paso de agua" Apagar PIN_LED
	Fin Si

FinAlgoritmo
