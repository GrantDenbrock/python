#exceptions.py
print('enter 2 numbers and they will be divided.')

while True:
	first_number = input('\nFirst number:')
	if first_number == 'q':
		break
	
	second_number = input('\nSecond number:')
	try:
		answer = int(first_number)/int(second_number)
	except ZeroDivisionError:
		print('no div by 0')
		
	except ValueError:
		print('make sure you enter numbers not strings')
		
	else:
		print(answer)
