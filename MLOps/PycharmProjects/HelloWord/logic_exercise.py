person_name = input("Enter your name: ")
print(f"You entered {person_name}")

name_length = len((person_name))
print(f"Name length is: {name_length}")

if name_length<3:
    print("Name must be atleast 3 characters long")
elif name_length>50:
    print("Name must be less than 50 characters long")
else:
    print("Name looks perfectly good")

