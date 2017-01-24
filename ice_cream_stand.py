#ice_cream_stand.py
from resturaunt import Resturaunt

#I hate that it runs resturaunt.py every time I import it

class IceCreamStand(Resturaunt):
	
	def __init__(self, resturaunt_name, cuisine_type): #initialize the icecreamstand class
		
		super().__init__(resturaunt_name, cuisine_type) #initializes the superclass resturaunt
	
		self.flavors = [''] #list attribute
	
	def display_flavors(self):
		print(self.flavors)
		
#instantiaite the class

cold_stone = IceCreamStand('cold stone', 'icecream')
cold_stone.flavors = ['chocolate','vanilla']
cold_stone.display_flavors()
