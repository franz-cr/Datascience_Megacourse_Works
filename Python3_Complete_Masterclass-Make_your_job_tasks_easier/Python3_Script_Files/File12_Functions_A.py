# Functions, global variables, modules - Basics
#===============================================================================
#
# Documentation:
# https://docs.python.org/3/tutorial/controlflow.html#defining-functions
# https://docs.python.org/3/tutorial/modules.html#standard-modules
# https://www.tutorialspoint.com/python3/python_functions.htm

# VARIABLES GLOBALES:
# ===================
global_variable = 0

# Defining a function that takes two positional parameters and returns a result
def fixed_number_arguments_function(x, y): 
	'''This is the 'docstring' for the function useful with the 'help' keyword'''
	# The first statement of the function body can optionally be a string literal; 
	# this string literal is the function’s documentation string, or docstring.
	# There are tools which use docstrings to automatically produce online or 
	# printed documentation, or to let the user interactively browse through code;
	# it’s good practice to include docstrings in code that you write, so make a 
	# habit of it.
    suma = x + y

    # Reference to a variable outside the local namespace of a function
    print(global_variable)

    # This statement is used to exit a function and return something when the 
    # function is called
    return suma 

# Specifying a default parameter value in a function definition
# https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions
def default_value_arguments_function(x, y, z = 3): 
	'''Función con parámetros mixtos'''
	# Recibe 2 parámetros posicionales obligatorios y 1 argumento por defecto
	# y opcional.
	pass

# Arbitrary Arguments, *args
# ==========================
# If you do not know how many arguments that will be passed into your function, 
# add a '*'' before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the 
# items accordingly:
# Specifying a variable number of positional parameters in a function definition; 
# args is a tuple
def arbitrary_arguments_function(x, *args):
	'''Función con parámetros mixtos'''
	# Recibe 1 parámetro posicional obligatorio y una serie abierta de parámetros
	# opcionales.
	pass

# Specifying a variable number of keyword parameters in a function definition; 
# args is a tuple
def arbitrary_keyword_arguments_function(x, **kwargs):
	pass 
 
# <====  Punto de entrada de la ejecución del script luego de las funciones.

# Calling a function and passing two POSITIONAL arguments, the values of 1 and 2; 
# result is 3
resultado = my_first_function(1, 2) 
print("x + y = ", resultado)

# Calling a function and passing two KEYWORD arguments, the values of 1 and 2; 
# result is 3
my_first_function(x = 1, y = 2)

# Calling a function and passing mixed types of arguments, the values of 1 and 2; 
# result is 3.
# Gold Rule: positional arguments always before keyword arguments!
my_first_function(1, y = 2) 

