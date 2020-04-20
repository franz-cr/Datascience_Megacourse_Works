# LESSON 10: Break, Continue and Pass commands
# https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops

# Break command: The break statement, like in C, breaks out of the innermost 
# enclosing for or while loop. Loop statements may have an else clause; it is 
# executed when the loop terminates through exhaustion of the iterable (with for) 
# or when the condition becomes false (with while), but not when the loop is 
# terminated by a break statement.

# This is exemplified by the following loop, which searches for prime numbers

for n in range(2, 10):
	for x in range(2, n):
		if n % x == 0:
			print(n, 'equals', x, '*', n//x)
			break
	else:
		# loop fell through without finding a factor
		print(n, 'is a prime number')

# Program output:
#	2 is a prime number
#	3 is a prime number
#	4 equals 2 * 2
#	5 is a prime number
#	6 equals 2 * 3
#	7 is a prime number
#	8 equals 2 * 4
#	9 equals 3 * 3

# Continue command: The continue statement, also borrowed from C, continues with 
# the next iteration of the loop:

for num in range(2, 10):
	if num % 2 == 0:
		print("Found an even number", num)
		continue
	else:
		print("Else code")
	print("Found a number", num)


# Program output:
#	Found an even number 2
#	Else code
#	Found a number 3
#	Found an even number 4
#	Else code
#	Found a number 5
#	Found an even number 6
#	Else code
#	Found a number 7
#	Found an even number 8
#	Else code
#	Found a number 9

# Pass command: The pass statement does nothing. It can be used when a statement 
# is required syntactically but the program requires no action. 

print("Ctrl+C to stop execution")
while True:
	pass  
	# Busy-wait for keyboard interrupt (Ctrl+C)

# This is commonly used for creating minimal classes:

class MyEmptyClass:
	pass

# Another place "pass" can be used is as a place-holder for a function or 
# conditional body when you are working on new code, allowing you to keep thinking 
# at a more abstract level. The pass is silently ignored:

 def initlog(*args):
	pass   
	# Remember to implement this!
