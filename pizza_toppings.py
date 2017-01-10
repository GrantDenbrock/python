#pizza toppings
prompt = "enter a topping: "
prompt += "enter quit when finished"
toppings = []

while True:  #building the list of toppings
	topping = input(prompt)
	
	if topping == 'quit':
		break
	
	else:
		toppings.append(topping)
		print(toppings)
#now im going to price the pizza based on number of toppings

if len(toppings) < 2:
	price = 10
	
elif len(toppings) <= 4:
	price = 12
	
elif len(toppings) > 4:
	price = 14
	
print("your pizza costs: " + str(price))


