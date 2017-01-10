#cars.py
def build_profile(first, last, **user_info):
	profile = {}
	profile['first name'] = first
	profile['last name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile('albert', 'einstein', location = 'princeton', field = 'physics')

print(user_profile)


def build_car(make, model, **car_info):
	car = {}
	car['make'] = make
	car['model'] = model
	for key, value in car_info.items():
		car[key] = value
	return car
	
car1 = build_car('mitsubishi', 'eclipse', color = 'blue', dents = 'yes')

print(car1) #check if the function works, it does.

lot=[]
lot.append(car1)
print(lot)
