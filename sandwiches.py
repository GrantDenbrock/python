#sandwiches.py
def make_sandwich(*toppings):
	print("Your sandwich will have: ")
	for topping in toppings:
		print("-" + topping)
		
make_sandwich('ham','cheese','pepper')
make_sandwich('tuna','pineapple')
make_sandwich('oreo','pepperoni','onion','cheese')

