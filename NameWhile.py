
#variable to store user name 
name = input ("Enter your name: ")

#while loop will run as long as the variable name
while name == "" or not name.isalpha():
    print("Invalid name")
    name= input("Enter your name:")

print (f"Hello {name}")
name= input("Enter your name: ")

#Exit out of the loop once the user has typed their
print(f"hello{name}")