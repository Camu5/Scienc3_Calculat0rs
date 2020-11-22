#Coded by Camu5

from datetime import date, timedelta
import os
from datetime import date, timedelta

if os.path.exists('dat0s.py'): 
	from dat0s import *
else: 
	print("¿Qué día fué tu última menstruación?")
	dia = int(input('Escribe el día:'))
	mes1 = int(input('Escribe el mes:'))
	ano1 = int(input('Escribe el año:'))
	print("¿Qué día fué tu anterior menstruación (hace dos meses)?")
	dia2 = int(input('Escribe el día:'))
	mes2 = int(input('Escribe el mes:'))
	ano2 = int(input('Escribe el año:'))	
	primer_dia1 = date(ano1, mes1, dia)
	primer_dia2 = date(ano2, mes2, dia2)
	with open("dat0s.py", 'w') as archivo:
		archivo.write(f"import datetime\n")
		archivo.write(f"from datetime import date\n")
		archivo.write(f"primer_dia1 = {repr(primer_dia2)}\n")
		archivo.write(f"primer_dia2 = {repr(siguiente_dia)}\n")

dias_ciclo = abs(primer_dia2 - primer_dia1).days
siguiente_dia = (primer_dia1) + timedelta(days=dias_ciclo)
ovulacion = (primer_dia1) + timedelta(days=(dias_ciclo - 14))
print("Tu siguiente día será:", siguiente_dia)
print("Ovularás el:", ovulacion)
print("Tu periodo es de:", dias_ciclo, "días")