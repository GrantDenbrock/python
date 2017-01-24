#guest_book.py

guest_book = [] #create empty list in which to store names

print('This program will add your name to a text file, input your names or enter a blank string when finished')

while True:
	
	name = input("Input your name: ") #make this a function?
	
		
	if name == '': #I put this before the append so that it doesnt put an empty string in the list
		break  #breaks out of the while loop
	
	guest_book.append(name) #add name to the list
	

print(guest_book)

#now I want to write the guest book to a file called guest_book.txt

filename = 'guest_book.txt'

with open(filename, 'w') as file_object:
	for entry in guest_book:
		file_object.write(entry + '\n') #successful
		
