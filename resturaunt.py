#resturaunt.py
class Resturaunt(): #create the class
	def __init__(self, resturaunt_name, cuisine_type): #initialize
		self.resturaunt_name = resturaunt_name #attribute
		self.cuisine_type = cuisine_type #attribute
		self.number_served = 0
	
	def describe_resturaunt(self): #this function prints a basic description of the resturaunt
		print("The resturaunt is called " + self.resturaunt_name + " and it serves " + self.cuisine_type)
	
	def open_resturaunt(self): #this functions prints a message that the resturaunt is open
		print(self.resturaunt_name + " is open!")
		
	def set_number_served(self,number):
		self.number_served += number
		

#now I want to create 2 instances of the class

in_n_out = Resturaunt('In-n-out','burgers')
pancheros = Resturaunt('Pancheros','burritos')

in_n_out.describe_resturaunt()
in_n_out.open_resturaunt()
pancheros.describe_resturaunt()
pancheros.open_resturaunt()
print(str(in_n_out.number_served) + " have been served")
in_n_out.set_number_served(20)
print(str(in_n_out.number_served) + " have been served now.")
