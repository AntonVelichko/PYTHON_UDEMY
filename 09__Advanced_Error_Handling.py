### ERROR HANDLING

while True:
	try: 
		age = int(input('What is your age?'))
		print(age)
	except ValueError:
		print('Please enter a number')
	except ZeroDivisionError:
		print('Please enter age higher than 0')
	else: 
		print('thank you')
		break


---


def sum(num1, num2):
	try:
	    return num1 + num2
	except TypeError as err:
		print(f'Please enter numbers --> {err}')

print(sum('1', 2))


---


def sum(num1, num2):
	try:
	    return num1 / num2
	except (TypeError, ZeroDivisionError):
		print('Oops')

print(sum(1, 0))


---

def sum(num1, num2):
	try:
	    return num1 / num2
	except (TypeError, ZeroDivisionError) as err:
		print(err)

print(sum(1, 0))



---

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
		print('your attempt is logged')
	print('Can you hear me?')


---

# raise ValueError
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


---

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





