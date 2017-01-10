#dictionaries.py
user_0 = {} #building the dictionary
user_0['Grant']= 1
user_0['Linda'] = 2
user_0['Steve'] = 3
user_0['Madison'] = 4
print(user_0)

for key , value in user_0.items(): #looping through dictionary
	print("\nKey: " + key)
	print("\nValue: " + str(value))
	
for key in user_0.keys(): #just print out the keys
	print(key)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

favorite_languages = {
	'g':'python',
	'l':'C',
	's':'pearl',
	'm':'python',
}

friends = ['l','s']

for name in favorite_languages.keys():
	print(name.title())
	
for name in friends: #sends a message to friends
	print('hi ' + name.title() + ', I see your favorite language is ' + favorite_languages[name].title() + '!')

#~~~~~~~~~~~~~~exercises~~~~~~~~~~~~~~~~~~~~

users = {
	'grant' : {'age':'23', 'height':'6'},
	'madi' : {'age':'21','height':'5'}
		}
		
for age, height in users.items():
	print(age)
	print(height)

#~~~~~~~~next program~~~~~~~~
#pets

hendrix = {'breed':'chihuaua','owner':'grant'}
coco = {'breed':'poodle','owner':'madison'}
maizy = {'breed':'lab','owner':'steve'}

pets = [hendrix, coco, maizy]

print(pets)
print('hendrix!' + hendrix['breed'])

#~~~~~~
#cities

phx = {'pop':'23456'}
lon = {'pop':'78987'}

cities = [phx,lon]

print("phoenix has " + phx["pop"] + " people living in it")
print("london has " + lon["pop"] + " people living in it")

#I feel good with dictionaries, although I'm sure there are more efficient methods to what im doing I know its gonna work
