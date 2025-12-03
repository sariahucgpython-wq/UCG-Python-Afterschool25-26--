# Program Description Calculates bi

#Asking user for Bill amt

bill = float(input("Enter bill amount: "))

#Asking user for no, of people

people= int(input("Enter no. of people shareing: "))

#Define tax and tip rates

tax_rate =0.0825 
tip_rate= 0.15

#formula to calculate tax, tip and total
tax=bill * tax_rate

tip=bill * tip_rate
 
total= bill + tax + tip

total= bill + tax + tip

#caculate amt each perso ows
per_person = total/people


#Printing everything

print("Restaurant Bill calculator")
print("___________________________")
print(f"Origanal Bill {bill}" )
print(f"Sale Tax:  {tax}")
print("Tip 15% {tip}")
print(f" Here is the bill {total}")
print(f"Each person's share {per_person}")


