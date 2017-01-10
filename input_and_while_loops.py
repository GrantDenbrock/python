#user input and while loops
active = True
while active:
	message = input("tell me something and ill repeat it back to you: ")
	
	if message == 'quit':
		active = False
	
	else:
		print(message)


#rental car
print('running rental car program:')

ask = input('enter the type of rental car you would like: ')
print(ask)
if ask == 'subaru':
	print('we have it!')
else:
	print('we dont have it')
	
#resturaunt seating
seats = input('how many in your party? : ')
if int(seats) > 8:
	print('no soup for you')
else:
	print('we have seats')
	
#multiple of 10?

number = input('enter a number and ill tell you if its a multiple of 10:')
if int(number) % 10 == 0:
	print('yeah buddy')
else:
	print('nope')

#while loops

current_number = 1
while current_number < 5:
	print(current_number)
	current_number += 1
print('done')#counts up to 4

#pizza toppings program

topping = input('enter a topping: ')
while topping != 'quit':
	toppings.append(topping)
print(toppings)

pets = ['cat','dog','goldfish','cat','hamster','cat']
print(pets)

while 'cat' in pets:
	pets.remove('cat')

print(pets)
