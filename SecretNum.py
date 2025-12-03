#Guess the secret Number Game

#The correct Number

# created and set the no. for user to guess
secretNum = 4 

# user guess set to 0 
guess = 0 

# create a while loop

while secretNum != guess:
    if guess > secretNum:
        print("Number is to high, try again!")
        guess = int(input("Enter a number between 1 and 10: "))
    if guess < secretNum:
        print("Number is to low,try again!")
        guess = int(input("Enter a number between 1 and 10: "))
else:
    print("🎉Congrats, you got it right!")






