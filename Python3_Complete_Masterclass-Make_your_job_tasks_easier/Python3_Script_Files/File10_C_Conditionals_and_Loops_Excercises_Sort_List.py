
# SORT A LIST OF  NUMBERS

# Write a Python program to sort a list of numbers entered by the user. The user can
# select if order is acending or descending. The list of numbers can include 
# positive and negative values. Add a control to catch when the users adds strings.

# Display an alert box to show the result. 

# Sample numbers : 0, -1, 4
# Output : 4, 0, -1

# Lógica del algoritmo.
# 1.	Mostrar un título del programa.
# 2.	Solicitar al usuario los números a ordenar.
# 	-	Capturar los errores 
# 	-	Ingresar el dato válido a una lista
# 	-	Salir del ciclo de carga de datos
# 3.	Ordenar los datos
#	-	Inicializar una lista.
#	-	
# 4.	Mostrar los resultados al usuario

# Test path in Command Prompt:
# C:\Users\ulrichca\Documents\Jupyter_Projects\Python3_Complete_Masterclass-Make_your_job_tasks_easier\Python3_Script_Files\File10_C_Conditionals_and_Loops_Excercises_Sort_List.py

''' 
Cualquier texto
'''

# VARIABLES
strDato = str()
intDato = int()
intCont = 1
booOrdenamiento = bool()
lstDatos = list()
lstOrdenada = list()

# PROCESO
print("")
print("================================================================================")
print("                     ORDENAMIENTO DE LISTA DE NÚMEROS")
print("================================================================================")

# Captura de la lista de datos a ordenar
print("")
print(" Ingrese una serie de números enteros a ordenar")
print("")
print("================================================================================")
print("")
while (strDato != "S") or (strDato != "s"):
	print("Número[", intCont,"]: ")
	strDato = input()
	if (strDato == "S") or (strDato == "s"):
		break
	try:
		intDato = int(strDato)
	except ValueError as e:
		print("Error: \"", strDato, "\" no es un número entero!")
	except Exception as e:
		print("Error: ", e)
	else:
		lstDatos.append(intDato)
		intCont += 1
	finally:
		pass

# Capturar tipo de ordenamiento dado or el usuario
print("================================================================================")
print("")
print(" Ingrese el tipo de ordenamiento sea ascendente (ASC) o descendente (DES)")
print("")
print("================================================================================")
print("")

booOrdenamiento = False
while not ((strDato == 'ASC') or (strDato == 'asc') or (strDato == 'DES') or (strDato == 'des')):
	# Explicit line join is expressed by the \ character
	strDato = input("Ordenamiento: ")
	if (strDato == "ASC") or (strDato == "asc"):
		booOrdenamiento = True
		#break
#	elif (strDato != "DES") or (strDato != "des"):
#		booOrdenamiento = False
		#break

# Imprimir el vector sin ordenar y el ordenamiento ingresado
print("")
print("================================================================================")
print("")
print(" Datos iniciales (", (intCont - 1),"): ", lstDatos)
print(" Ordenamiento ascendente: ", booOrdenamiento)
print("")
print("================================================================================")
print("")

# Ordenar el vector

# Imprimir el resultado