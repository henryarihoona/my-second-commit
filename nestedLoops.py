for x in range(4):
    for y in range(2):
        print(f'({x},{y})')
#shapes
#alternative
numbers = [5,2,5,2,2]
for number in numbers:
    output = ''
    for count in range(number):
        output += 'x'
        print(output)
#max number
numbers = [3,4,6,7,10]
max = numbers[0]
for number in numbers:
    if number>max:
        max = number
print(number)
#unpacking
coordinates = (2,4,5)
x,y,z = coordinates
print(f'{x},{y},{z}')

   