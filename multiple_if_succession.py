# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L \n")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N \n")
# 🚨 Don't change the code above 👆
bill = 0
#Write your code below this line 👇
if size == 'S':
  bill = 15
  if add_pepperoni == 'Y':
    bill += 2
  if extra_cheese == 'Y':
    bill += 1
  print(f"your final bill is ${bill} only")
elif size == 'M':
  bill = 20
  if add_pepperoni == 'Y':
    bill += 3
  if extra_cheese == 'Y':
    bill += 1
  print(f"your final bill is ${bill} only")
else:
  bill = 25
  if add_pepperoni == 'Y':
    bill += 3
  if extra_cheese == 'Y':
    bill += 1
  print(f"your final bill is ${bill} only")