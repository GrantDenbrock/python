#using_json.py
#part 1 0f 2, how to store something to json
import json

numbers = [1,2,3,4,5]

filename = 'numbers.json'
with open(filename,'w') as f_obj:
	json.dump(numbers , f_obj)
