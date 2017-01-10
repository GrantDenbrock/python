#functions
def message():
	"""Display a message""" #called a docstring
	print("we're learning about functions")

def favorite_book(title):
	print('My favorite book is ' + title)
	
favorite_book('call of the wild')	

#positional arguments need to be passed in the order in which they were given

def describe_pet(animal_type, pet_name):#function that takes multiple positional arguments
	"""Describe information about a pet""" #docstring
	print("\n I have a " + animal_type + ".")
	print("\n My " + animal_type + "'s name is " + pet_name.title() + ".")
	
describe_pet('hamster','harry')

#~~~~~make shirt program~~~~~~~~~~
def make_shirt(size = 'default size' ,message = 'no message selected'):
	print("\n The size of the shirt selected is: " + size)
	print("\n the message will be: " + message)
	
make_shirt('large','grant is cool')

# this function will return a dictionary
def build_person(first_name , last_name):
	person = {'first': first_name , 'last' : last_name}
	return person
	
musician = build_person('jimi','hendrix')
print(musician) #prints the dictionary with the name in it

#~~~~~~make album~~~~
def make_album(artist_name = 'none given',album_title= 'none given'):
	album = {"title":album_title,"artist":artist_name}
	print(album)
	
make_album('nirvana','nevermind')
make_album('jimi hendrix','electric ladyland')

#~~~~~~~user profiles~~~~~~~
def build_user_profile(first,last, **user_info):
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile
	
user_profile_1 = build_user_profile('albert','einstein', field = 'physics')
print(user_profile_1)
user_profile_2 = build_user_profile('grant','denbrock', field = 'physics')
print(user_profile_2)
user_profile_3 = build_user_profile('madi','winston', field = 'health')
print(user_profile_3)

