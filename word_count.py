#word_count.py
#practice handling exceptions

def count_words(filename):#will give it a file and it will count the number of words in it
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
			
			
	except FileNotFoundError:#so we dont get a file not found error
		msg = 'sorry the file ' + filename + 'doesnt exist'
		print(msg)
		
		
	else:#carry out the function
		words = contents.split()
		num_words = len(words)
		print('the file ' + filename + ' has ' + str(num_words) + ' words ')
		
		
filename = 'grant_rules.txt'
count_words(filename)


