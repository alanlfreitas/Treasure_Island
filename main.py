########## Testing conditionals ##########
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("How old are you? "))
if height >= 120:
  print("Go ahead. You can ride the rollercoaster.")
  if age < 12:
    print("Please pay $5.")
  elif age <= 18:
    print("Please pay $7.")
  elif age > 18 and age <= 21:
    print("Please pay $10")
  else:
    print("Please pay $12.")
else:
  print("Sorry. But you can't ride the rollercoaster.")

# 🚨 Don't change the code below 👇
#number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
##rest = number % 2
##if (rest == 0):
##    print("This is an even number.")
##else:
##    print("This is an odd number.")
##if number % 2 == 0:
##    print("This is an even number.")
##else:
##    print("This is an odd number.")