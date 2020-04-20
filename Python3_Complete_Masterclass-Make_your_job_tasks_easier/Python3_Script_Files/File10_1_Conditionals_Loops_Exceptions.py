# Flow Control: Conditionals, Loops and Exceptions

# IF Statements: Perhaps the most well-known statement type is the if statement
# C:\Users\ulrichca\Documents\Jupyter_Projects\Python3_Complete_Masterclass-Make_your_job_tasks_easier\Python3_Script_Files\File10_Conditionals_Loops_Exceptions.py


print('--------------------------------------------------------') 
print('  Ejemplo de IF ELIF y ELSE')
print('--------------------------------------------------------') 

strTexto = input('Ingrese cualquier número: ')

dato = int(strTexto)

if dato < 0:
	print(dato, ' es menor que cero.')
elif dato == 0:
	print(dato, ' es igual a cero.')
else:
	print(dato, ' es mayor que cero.')
print('\n')

print('--------------------------------------------------------') 
print('  Ejemplo de FOR-ELSE usando la función \"range(n)\"')
print('--------------------------------------------------------') 

for i in range(5):
	print('i = ', i)
else:
	print('range = 5')

print('\n')

for i in range(5, 10):
	print('i = ', i)
else:
	print('range = 5, 10')

print('\n')

for i in range(5, 20, 2):
	print('i = ', i)
else:
	print('range = 5, 10, 2')

print('\n')

for i in range(-10, -100, -10):
	print('i = ', i)
else:
	print('range = -10, -100, -10')

print('\n')

print('--------------------------------------------------------') 
print('  Ejemplo de FOR-ELSE usando la función listas o tuplas')
print('--------------------------------------------------------') 

lstLista = ["Limón", "Naranja", "Banano", "Mango", "Sandía", "Melón"]

for i in lstLista:
	print('i = ', i)
else:
	print('Lista: ', lstLista)

print('\n')

print('----------------------------------------------------------') 
print('  Ejemplo de FOR-ELSE usando la función \"Range\" y listas')
print('----------------------------------------------------------') 

for i in range(len(lstLista)):
	print('i = ', i, ' valor = ', lstLista[i])
else:
	print('Lista: ', lstLista)

print('\n')

print('-----------------------------------------------------------------') 
print('  Ejemplo de FOR-ELSE usando la función un cadena de caracteres')
print('-----------------------------------------------------------------') 

j = 0
for j in range(len(lstLista)):
	for i in lstLista[j]:
		print('i[', j, '] = ', i)
	else:
		print('Lista: ', lstLista[j])
else:
	print('Lista: ', lstLista)

print('\n')

print('--------------------------------------------------------') 
print('  Ejemplo de WHILE-ELSE con entrada del usuario')
print('--------------------------------------------------------') 

while (strTexto != "99") or (strTexto != "-99"):
	strTexto = input('Ingrese cualquier número (\"S\"): ')
	dato = int(strTexto)
	if dato < 0:
		print(dato, ' es menor que cero.')
	elif dato == 0:
		print(dato, ' es igual a cero.')
	else:
		print(dato, ' es mayor que cero.')
else:
	print('Programa finalizado')

print('\n')
