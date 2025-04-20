# Python uses indentation to define blocks of code, not curly brackets or other symbols.

temp = 20
if temp > 30:
    print("It's hot outside")
elif temp > 20:
    print("It's a nice day!")
else:
    print("It's cold outside")

# Checking multiple conditions with logical operators
age = 25
has_licence = True

if age >= 18 and has_licence:
    print("You can drive a car")
elif age >= 18 and not has_licence:
    print("You need to get a driver's lincese first")
else:
    print("You are too young to drive.")

# Nested Conditionals
score = 85

if score >= 60:
    print("You got passed!")
    if score >= 90:
        print("You got an A")
    if score >= 80:
        print("You got an B!")
    if score >= 70:
        print("You got an C!")
    else:
        print("You got an D!")        
else:
    print("You failed")    
    
