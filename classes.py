#classes.py
class Dog(): #define a class called Dog, notice the capital D
	"""a simple attempt to model a dog"""
	
	def __init__(self,name,age): #the __init__ method
		"""initialize name and age attributes"""
		self.name = name #attributes
		self.age = age
		
	def sit(self):
		"""simulate a dog sitting in response to a command"""
		print(self.name.title() + " is now sitting.")
		
	def roll_over(self):
		"""simulate rolling over"""
		print(self.name.title() + " is now rolling over")

my_dog = Dog('hendrix', 6) #instantiation of the class Dog

print("my dogs name is " + my_dog.name.title() + ".")
print("my dog is " + str(my_dog.age))

my_dog.sit()
my_dog.roll_over()
