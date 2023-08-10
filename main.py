########## Testing conditionals ##########
#print("Welcome to the rollercoaster!")
#height = int(input("What is your height in cm? "))
#age = int(input("How old are you? "))
#if height >= 120:
#  print("Go ahead. You can ride the rollercoaster.")
#  if age < 12:
#    print("Please pay $5.")
#  elif age <= 18:
#    print("Please pay $7.")
#  elif age > 18 and age <= 21:
#    print("Please pay $10")
#  else:
#    print("Please pay $12.")
#else:
#  print("Sorry. But you can't ride the rollercoaster.")

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

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(weight / (height * height))
#bmi = int(bmi)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi > 18.5 and bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi > 25 and bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi > 30 and bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are Tais Carla.")