#magicians.py
magicians = ['tina','jimmy jr','tammy']
great_magicians = []

def make_great(list1):
	for magician in magicians:
		great_magicians.append("The Great " + magician.title())
		
make_great(magicians)
print(great_magicians)

def show_magicians(any_list):#accepts any list as the first parameter
	for magician in magicians:
		print(magician.title())#prints out the list we feed in as the argument
		
show_magicians(great_magicians)#does show magicians to the list magicians
