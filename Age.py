#program Name: Age in Months and Days
#To calculate the user's age in months and days


#Get user's age
age_years = int (input( "Enter you age in years:"))

#Convert to months and days
months = age_years * 12
days = age_years * 365

#Display result 
print("_______________________________")
print("You are" months," months old.")
print("That's about", days,"days!")
print("_______________________________")


