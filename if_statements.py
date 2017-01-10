#if statements
cars = ['audi','bmw','subaru','toyota']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())
	
#alien colors game

alien_color = 'green'

if alien_color == 'green':
	print("you get 5 points")

elif alien_color == 'red':
	print("you get 10 points")

elif alien_color == 'blue':
	print("you get 8 points")
	
#favorite fruit game make a list and test if your favorite fruit is in the list
#if it is print something out that says so

fruit = ['apple','banana','orange','coconut']
favorite_fruit = 'pear'
if favorite_fruit in fruit:
	print('yay')
else:
	print('only sadness for you')

#i want to take a list of strings and numbers
#and copy only the strings to a new list

shitty_list = ['grant',1,'linda',2,'steve',3,'madi',4] #list mixed data types
string_list = []
numbers_list = []
for x in shitty_list:
	if x == str(x):
		string_list.append(x)
	else:
		numbers_list.append(x)
		
print(string_list) #separated by data type
print(numbers_list)	

dict = {'user' : 'key'}
print(len(dict))
