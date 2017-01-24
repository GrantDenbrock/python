#cars_classes.py
class Car():
	"""model of a car"""
	
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		
	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
		
	def read_odometer(self):
		print("this car has " + str(self.odometer_reading) + " miles on it.")
		
	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
			
		else:
			print("nice try buddy")
			
	def increment_odometer(self, miles):
		self.odometer_reading += miles
		
		
class ElectricCar(Car):
	"""represents aspects of a car specific to an electric car"""
	
	def __init__(self, make, model, year):
		"""initialize attributes of parent class"""
		super().__init__(make, model, year)
		self.battery_size = '70'
		
	def describe_battery(self):
		print("this car has a " + self.battery_size + " kWh  battery.")
		
my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
