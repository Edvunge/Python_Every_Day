print("Hello World!")

# Strings
name = "Alex"

# Integer (Whole Numbers)
age = 25

# Float (decimal number)
height = 9.5

# Boolean
is_student = True

print("Hey my name is " + name)
print("Hey my name is ", name)

print(name[-1])

msg = "Hello world!"
print(msg.upper())
print(msg.lower())
print(msg.capitalize())
print(msg.replace("l", "L"))
print("World" in msg)
print(len(msg))


greeting1 = "Hello"
greeting2 = "hello"

if greeting1 == greeting2:
    print("They are the same")
else:
    print("They are different")


# Type conversion
age_str = "30"
age_num = int(age_str)
print(type(age_num))
print(type(age_str))

price_float = 29.99
price_int = int(price_float)