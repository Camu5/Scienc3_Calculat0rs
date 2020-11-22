#Coded by Camu5
import sys

def menu0():
	print("Escoge una Operación Para Realizar: ")
	print("1) UNIÓN *U*")
	print("2) INTERSECCIÓN *∩*")
	print("3) COMPLEMENTO *x'*")
	print("4) DIFERENCIA *()-()*")
	print("5) DIFERENCIA SIMÉTRICA *Δ*")
	print()

def pregunta():
	print()
	print("¿Deseas calcular algo más?")
	respuesta = input("S/N: ")
	if respuesta == "S":
		print()
		inicio()
	elif respuesta == "SI":
		print()
		inicio()
	elif respuesta == "si":
		print()
		inicio()
	elif respuesta == "s":
		print()
		inicio()
	elif respuesta == "Si":
		print()
		inicio()
	elif respuesta == "Sí":
		print()
		inicio()
	elif respuesta == "N":
		sys.exit()
	elif respuesta == "NO":
		sys.exit()
	elif respuesta == "No":
		sys.exit()
	elif respuesta == "no":
		sys.exit()
	elif respuesta == "n":
		sys.exit()
	else:
		print("Opción Inválida. Escoga, Sí o No")
		pregunta()

	

def menu1():
	print("Escogiste: UNIÓN DE CONJUNTOS")
	print("Define el conjunto A introduciendo los elementos separados por ENTER (Si deseas parar, introduce el símbolo *)")
	valor = input("Introduce el elemento:")
	conjunto1 = []
	while valor!="*":
		conjunto1.append(valor)
		valor = input(str("Introduce el elemento: "))
	print("Conjunto A =", conjunto1)
	print()
	print("Define el conjunto B introduciendo los elementos separados por ENTER (Si deseas parar, introduce el símbolo *)")
	valor1 = input("Introduce el elemento:")
	conjunto2 = []
	while valor1!="*":
		conjunto2.append(valor1)
		valor1 = input(str("Introduce el elemento: "))
	print("Conjunto B =", conjunto2)
	print()
	resultado = set(conjunto1 + conjunto2)
	print("CONJUNTO (A + B) =", resultado)
	pregunta()

def menu2():
	print("Escogiste: INTERSECCIÓN DE CONJUNTOS")
	print("Define el conjunto A introduciendo los elementos separados por ENTER (Si deseas parar, introduce el símbolo *)")
	valor = input("Introduce el elemento:")
	conjunto1 = []
	while valor!="*":
		conjunto1.append(valor)
		valor = input(str("Introduce el elemento: "))
	conjunto_1 = set(conjunto1)
	print("Conjunto A =", conjunto1)
	print()
	print("Define el conjunto B introduciendo los elementos separados por ENTER (Si deseas parar, introduce el símbolo *)")
	valor1 = input("Introduce el elemento:")
	conjunto2 = []
	while valor1!="*":
		conjunto2.append(valor1)
		valor1 = input(str("Introduce el elemento: "))
	conjunto_2 = set(conjunto2)
	print("Conjunto B =", conjunto2)
	print()
	resultado = conjunto_1.intersection(conjunto_2)
	print("CONJUNTO (A∩B) = ", resultado)
	pregunta()

def menu3():
	print("Escogiste: COMPLEMENTO DE CONJUNTOS")
	print("Define el conjunto A introduciendo los elementos separados por ENTER (Si deseas parar, introduce el símbolo *)")
	valor = input("Introduce el elemento:")
	conjunto1 = []
	while valor!="*":
		conjunto1.append(valor)
		valor = input(str("Introduce el elemento: "))
	conjunto_1 = set(conjunto1)
	print("Conjunto A =", conjunto1)
	print()
	print("Define el Conjunto Universal introduciendo los elementos separados por ENTER (Si deseas parar, introduce el símbolo *)")
	valor1 = input("Introduce el elemento:")
	conjuntou = []
	while valor1!="*":
		conjuntou.append(valor1)
		valor1 = input(str("Introduce el elemento: "))
	conjunto_u = set(conjuntou)
	print("Conjunto B =", conjuntou)
	print()
	resultado = (conjunto_u - conjunto_1)
	print("CONJUNTO COMPLEMENTO (A') = ", resultado)
	pregunta()

def menu4():
	print("Escogiste: DIFERENCIA DE CONJUNTOS")
	print("Define el conjunto A introduciendo los elementos separados por ENTER (Si deseas parar, introduce el símbolo *)")
	valor = input("Introduce el elemento:")
	conjunto1 = []
	while valor!="*":
		conjunto1.append(valor)
		valor = input(str("Introduce el elemento: "))
	conjunto_1 = set(conjunto1)
	print("Conjunto A =", conjunto1)
	print()
	print("Define el Conjunto B introduciendo los elementos separados por ENTER (Si deseas parar, introduce el símbolo *)")
	valor1 = input("Introduce el elemento:")
	conjunto2 = []
	while valor1!="*":
		conjunto2.append(valor1)
		valor1 = input(str("Introduce el elemento: "))
	conjunto_2 = set(conjunto2)
	print("Conjunto B =", conjunto2)
	print()
	print("¿Qué conjunto debe actuar como minuendo?")
	print("1) Conjunto A")
	print("2) Conjunto B")
	seleccion = int(input("Opción:"))
	if seleccion == 1:
		resultado = (conjunto_1 - conjunto_2)
		print("CONJUNTO (A - B) = ", resultado)
	else: 
		resultado = (conjunto_2 - conjunto_1)
		print("CONJUNTO (B - A) = ", resultado)
	pregunta()

def menu5(): 
	print("Escogiste: DIFERENCIA SIMÉTRICA DE CONJUNTOS")
	print("Define el conjunto A introduciendo los elementos separados por ENTER (Si deseas parar, introduce el símbolo *)")
	valor = input("Introduce el elemento:")
	conjunto1 = []
	while valor!="*":
		conjunto1.append(valor)
		valor = input(str("Introduce el elemento: "))
	conjunto_1 = set(conjunto1)
	print("Conjunto A =", conjunto1)
	print()
	print("Define el Conjunto B introduciendo los elementos separados por ENTER (Si deseas parar, introduce el símbolo *)")
	valor1 = input("Introduce el elemento:")
	conjunto2 = []
	while valor1!="*":
		conjunto2.append(valor1)
		valor1 = input(str("Introduce el elemento: "))
	conjunto_2 = set(conjunto2)
	print("Conjunto B =", conjunto2)
	print()
	resultado = set((conjunto_1.union(conjunto_2)) - (conjunto_1.intersection(conjunto_2)))
	print("CONJUNTO (A Δ B) = ", resultado)
	pregunta()


def inicio():
	print("¡Calculadora de Conjuntos!")
	menu0()
	option = int(input("Opción: "))
	if option == 1:
		menu1()
	elif option == 2:
		menu2()
	elif option == 3:
		menu3()
	elif option == 4:
		menu4()
	elif option == 5:
		menu5()
	else:
		print("Opción Incorrecta.")
inicio()