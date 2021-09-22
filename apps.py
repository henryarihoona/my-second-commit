name = input('what is your name ? ')
color = input('what is your favourite color? ')
#Age calculator
print(name + ' likes ' + color)
birth_year = input('Birth_year: ')
print(type(birth_year))
age = 2021 - int(birth_year)
print(type(age))
print(age)
#lbs converter
weight_lbs = input('weight (lbs): ')
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)
#Email msgs
course = '''
Hi Arihoona,
we have great python free courses for you
In these trying days by attending via online
Thank you 
The support Team
'''
print(course)
#formatted texts
first = 'Arihoona'
last = 'Jose'
message = first + '['+ last + '] is a coder'
msg = f'{first} [{last}] is a coder'
print(msg)
#counting the length
course = 'python for beginners'
print(len(course))