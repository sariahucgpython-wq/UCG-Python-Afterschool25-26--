bill = float(input("Enter bill amount: "))
people=int(input("Enter Howmanypeople amount:"))
tax_rate=1.0825
bill_after=str((bill*tax_rate/people))
print("your bill is "+ bill_after)
