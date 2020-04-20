# Flow Control: Conditionals, Loops Exercises
# Dibuje el siguiente patrón:
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *
# El usuario debe poder ingresar la cantidad de líneas. 
# Hasta un máximo de 50 y un mínimo 5.

# 	Lógica del proceso:
# 1.	Preguntar al usuario por la cantidad de líneas.
# 2.	Calcular el centro de la la figura.
# 3.	Calcular los parámetros de ciclo ascendente
# 4.	Ejecutar la impresión del ciclo
# 5.	Calcular los parámetros del ciclo descendente
# 6.	Ejecutar la impresión del ciclo

# VARIABLES DEL PROCESO:
intLineas = int()
intMitad = int()
strLineas = str()

# ALGORITMO:
print('')
print('+    EL CUADRADO    +\n')
print('Por favor indique la cantidad de líneas.\n')

while strLineas != 'S':

	while (intLineas > 30) or (intLineas < 5):
		strLineas = input('Ingrese el lado: ')
		if strLineas == 'S':
			break
		intLineas = int(strLineas)
		strLineas = ''

	print('Líneas: ', intLineas)

	#if ((intLineas % 2) == 0):
	#	intMitad = (intLineas // 2) + 1
	#	intLineas += 1
	#else:
	#	intMitad = (intLineas // 2) + 1

	#print('\n-----------------------')
	#print('Líneas: ', intLineas)
	#print('Línea media: ', intMitad)
	#print('-----------------------\n')

	for i in range(0, intLineas):
		if (i == 0) or (i == intLineas -1):
			print(intLineas * '* ')
		else:
			print('* ', (intLineas - 3) * '  ', '*')

	print('\n')