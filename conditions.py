is_hot  = False
is_cold  = True

if is_hot:
   print("Its a hot day")
   print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("Enjoy your lovely day")

print("Its a lovely weekend")
#Another condition
price = 1000000
has_good_credit = True
if has_good_credit:
    down_payment = 0.1*price
else:
    down_payment=0.2*price
print(f"Down payment: ${down_payment}")
#logical operators
has_good_income = True
has_good_cedit = True

if has_good_credit and has_good_income:
    print("Eligible for loan")

#comparison operators

name ="A"
if len(name)<3:
    print("Name must be atleast 3 characters")
elif len(name)>50:
    print("Name must have a maximum of 50 characters.")
else:
    print("Name looks good!")
#converted weight
weight = int(input('weight: '))
unit = input('L(bs) or K(g): ')
if unit.upper()=="L":
    converted = weight * 0.45
    print(f"you are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"you are {converted} kilos")


