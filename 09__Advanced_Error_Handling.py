
##########################################################################################################################
###  ERROR HANDLING  ###
# An error that crashes the program is called an Exception
# Built-in exceptions  -->  https://docs.python.org/3/library/exceptions.html



try: 
	age = int(input('What is your age?'))
	print(age)						# if enter is not an Integer
except:
	print('Please enter a number')



---------------



while True:							# allows to start the program for every try
	try: 
		age = int(input('What is your age?'))
		10/age
	except ValueError:					# only one of the errors will be caught
		print('Please enter a number')
	except ZeroDivisionError:
		print('Please enter age higher than 0')
	else: 
		print('thank you')
		break						# finish the program when input is correct



---------------



def sum(num1, num2):
	try:
	    return num1 + num2
	except TypeError as err:
		print(f'Please enter numbers --> {err}')	# Please enter numbers --> can only concatenate str (not "int") to str
		print(err)					# can only concatenate str (not "int") to str

print(sum('1', 2))						# None
								


---------------



def sum(num1, num2):
	try:
	    return num1 / num2
	except (TypeError, ZeroDivisionError):
		print('Oops')

print(sum(1, 0))						# Oops



---------------



def sum(num1, num2):
	try:
	    return num1 / num2
	except (TypeError, ZeroDivisionError) as err:
		print(err)					# division by zero

print(sum(1, 0))						# None



---------------



def sum(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as err:
        print(err)						# unsupported operand type(s) for /: 'int' and 'str'

print(sum(1, '2'))						# None



---------------



# finally
while True:
	try: 
		age = int(input('What is your age?'))
		10/age
	except ValueError:
		print('Please enter a number')
		continue
	except ZeroDivisionError:
		print('Please enter age higher than 0')
	else: 
		print('Accepted! Thank you')
		break
	finally:
		print('your attempt is recorded')				# finally runs regardless of everything
	print('Can you hear me?')



---------------



# raise ValueError
# use very rare, in some specific cases

while True:
	try: 
		age = int(input('What is your age?'))
		10/age
		raise ValueError('STOP IT!')
	except ZeroDivisionError:
		print('Please enter age higher than 0')
	else: 
		print('Accepted! Thank you')
		break
	finally:
		print('your attempt is logged')
	print('Can you hear me?')



---------------



# raise Exception

while True:
	try: 
		age = int(input('What is your age?'))
		10/age
		raise Exception('STOP IT!')
	except ZeroDivisionError:
		print('Please enter age higher than 0')
	else: 
		print('Accepted! Thank you')
		break
	finally:
		print('your attempt is logged')
	print('Can you hear me?')





