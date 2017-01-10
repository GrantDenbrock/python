#lists.py
starfleet_ships = ['USS Enterprise','USS Constelation','USS Relativity']
print(starfleet_ships) #prints the list in brackets
print(starfleet_ships[0]) # prints USS Enterprise
print(starfleet_ships[-1]) #prints the last element of the list
message = "Captain Kirk was capitain of the " + starfleet_ships[0] + "."
print(message)
starfleet_ships[2] = 'USS Saratoga' #changing list element
print(starfleet_ships)
starfleet_ships.append('USS Stargazer') #appending to the list
print(starfleet_ships)
starfleet_ships.insert(0,'USS Titan') #inserting an element
print(starfleet_ships)
del starfleet_ships[2] #removes third element of the list
print(starfleet_ships)
deploy_ship = starfleet_ships.pop() #takes the last element and returns it
print(deploy_ship)
send_the_enterprise = starfleet_ships.pop(1) #send in the big guns
print(send_the_enterprise) #enterprise is no longer in the list
remove_the_titan = starfleet_ships.remove('USS Titan')
print(starfleet_ships)

klingon_warships = ['brel','kvort','bird of prey','ktinga']
print(klingon_warships)
print(sorted(klingon_warships)) #temporary sort
klingon_warships.sort() #alphabetical sort
print(klingon_warships)
klingon_warships.sort(reverse=True) #reverse alphabetical sort
print(klingon_warships)
klingon_warships.reverse() #puts the list in reverse
print(klingon_warships)
print(len(klingon_warships)) #print the length of a list

crew = ['Kirk','Spock','Sulu']
for member in crew:
	print(member)

some_list = [1,2,3]
for thing in some_list:
	thing = thing+2
	print(thing)
	
for x in range(0,5):
	print(x)

list_of_evens = list(range(2,11,2))
print(list_of_evens)

list_of_squares = []
for value in range(1,11):
	square = value**2
	list_of_squares.append(square)
print(list_of_squares)

better_list_of_squares = []
for value in range (1,11):
	better_list_of_squares.append(value**2)
print(better_list_of_squares)

digits = [1,2,3,4,5,6,7,8,9]
print(min(digits))
print(max(digits))
print(sum(digits))

#list comprehension allows you do make a list in one line of code
squares = [value**2 for value in range(1,11)]
print(squares)

#make a list to print numbers 1 through 20 inclusive
number_list = [value for value in range(1,21)]
print(number_list)

#make list on numbers 1 to 1000000 and use a for loop to print the numbers
million_list = [num for num in range(1,1000001)]
print(million_list)
print(min(million_list))
print(max(million_list))
print(sum(million_list))

twenty_odd_list = [x for x in range(1,21,2)]
print(twenty_odd_list)

#make list of multiples of 3 from 3 to 30 and print em
threes_list = [value for value in range(3,31,3)]
print(threes_list)

#make list of the first ten cubes and print em
cubes_list =[cube**3 for cube in range(1,11)]
print(cubes_list)

ncc1701_d = ['picard','riker','laforge','whorf']
print(ncc1701_d[1:3]) #returns riker and laforge
ncc1701_d.append('crusher')
print(ncc1701_d)

dimensions = (200,50)#dimensions is a "tuple" or immutable list because of the parentheese rather than brackets
width = dimensions[0]
height = dimensions[1]
area = width*height
print(area)

