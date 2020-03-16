# VARIABLES IN PYTHON

# Python Keywords
print('Python Keywords:')
print('----------------------------------------')
print(' False\tawait\telse\timport\tpass')
print(' None\tbreak\texcept\tin\traise')
print(' True\tclass\tfinally\tis\treturn')
print(' and\tfor\tlambda\ttry\tcontinue')
print(' as\tdef\tfrom\twhile\tnonlocal')
print(' assert\tdel\tglobal\tnot\twith')
print(' async\telif\tif\tor\tyield')
print('----------------------------------------')

# Declaring variables:
# 1. Integer
a = 10

print('\nDeclaración: \n\ta = 10')
print('Value of a:', a)

#2. Assign same value to multiple variables
a = b = c = 15

print('\nDeclaración: \n\ta = b = c = 15')
print('Value of a:', a)
print('Value of b:', b)
print('Value of c:', c)

#3. Assign several values to multiple variables on same line
d, e, f = 5, 10, 15

print('\nDeclaración: \n\td, e, f = 5, 10, 15')
print('Value of d:', d)
print('Value of e:', e)
print('Value of f:', f)

#4. Working with pointers
g = id(f)
h = id(5)
i = id(d)

print('\nDeclaración: \n\tg = id(f)\n\th = id(5)\n\ti = id(d)')
print('Value of g:', g)
print('Value of h:', h)
print('Value of i:', i)

#5. Defining a variable
my_var1 = 10 		#type integer
my_var2 = "Hello" 	#type string
my_var3 = True 		#type boolean

print('\nDeclaración: \n\tmy_var1 = 10\n\tmy_var2 = "Hello"\n\tmy_var3 = True')
print('Value of my_var1 (integer):', my_var1)
print('Value of my_var2 (string):', my_var2)
print('Value of my_var3 (boolean):', my_var3)

#6. Python Data Types
print('\nPython Data Types:\n\tstrings\n\tnumbers\n\tbooleans')
print('\tlists\n\tsets\n\tfrozensets\n\ttuples')
print('\tranges\n\tdictionaries\n\tNone')