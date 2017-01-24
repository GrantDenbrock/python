#dice.py
from random import randint
class Die():
	def __init__(self, sides):
		self.sides = 6
	
	def roll_die(self):
		print(randint(1,self.sides))
		
	def change_number_sides(self,number):
		self.sides = number
		
my_roll = Die(6)
my_roll.roll_die()
my_roll.change_number_sides(20)
my_roll.roll_die()

#now im gonna roll it 10 times
for x in range(0,9):
	my_roll.roll_die()
	
