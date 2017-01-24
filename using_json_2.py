#using_json_2.py
#the second part of how to load from json
import json

filename = 'numbers.json'
with open(filename) as f_obj:
	numbers = json.load(f_obj)
	
print(numbers)
