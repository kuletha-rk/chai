#If the bill was $150.00, split between 5 people, with 12% tip. 
print("welcome to the tip calculator!")
bill_total = input("What was the total bill?: \n")
tip = input("what percentage tip would you like to give? 10, 12 or 15?\n")

bill_with_tip = int(bill_total) * 1.12

people = input("How many people to split the bill ?\n")
average = int(bill_with_tip)/int(people)
round(average, 2)
average = "{:.2f}".format(average)
# ten = int(bill_total) * .10
# twelve = int(bill_total) * .12
# fifteen = int(bill_total) * .15
print(f"Each person should pay ${average} amount!")


#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
