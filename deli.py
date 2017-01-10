#deli
sandwich_orders = ['ham','turkey','pastrami','pastrami','pastrami']
finished_sandwiches = []
for sandwich in sandwich_orders:#loops through each entry in list sandwich_orders
	if sandwich != 'pastrami':
		finished_sandwiches.append(sandwich)#added each sandwich to the empty list finished_sandwich
		print('I have made your ' + sandwich + ' sandwich')
	else:
		print('we got no pastrami')
