########## Testing conditionals ##########
#print("Welcome to the rollercoaster!")
#height = int(input("What is your height in cm? "))
#age = int(input("How old are you? "))
#bill1 = 0
#if height >= 120:
#  print("Go ahead. You can ride the rollercoaster.")
#  if age < 12:
#    bill1 = 5
#    print("Please pay $5.")
#  elif age <= 18:
#    bill1 = 7
#    print("Please pay $7.")
#  elif age >= 45 and age <= 55:
#    print("Go ahead. You can ride for free.")
#  else:
#    bill1 = 12
#    print("Please pay $12.")
#  photo = input("Do you want a photo taken? Y or N. ")
#  if photo == "Y" or photo == "y":
#    billf = bill1 + 3
#    print(f"Your final bill is ${billf}")
#  else:
#    print(f"Your final bill is ${bill1}")  
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
#height = float(input("enter your height in m: "))
#weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#bmi = round(weight / (height * height))
#bmi = int(bmi)

#if bmi < 18.5:
#    print(f"Your BMI is {bmi}, you are underweight.")
#elif bmi > 18.5 and bmi < 25:
#    print(f"Your BMI is {bmi}, you have a normal weight.")
#elif bmi > 25 and bmi < 30:
#    print(f"Your BMI is {bmi}, you are slightly overweight.")
#elif bmi > 30 and bmi < 35:
#    print(f"Your BMI is {bmi}, you are obese.")
#else:
#    print(f"Your BMI is {bmi}, you are Tais Carla.")

# 🚨 Don't change the code below 👇
#year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#if year % 4 == 0:
#    if year % 100 == 0:
#        if year % 400 == 0:
#            print("Leap year.")
#        else:
#            print("Not leap year.")
#    else:
#        print("Leap year.")
#else:
#    print("Not leap year.")

# 🚨 Don't change the code below 👇
#print("Welcome to Python Pizza Deliveries!")
#size = input("What size pizza do you want? S, M, or L ")
#add_pepperoni = input("Do you want pepperoni? Y or N ")
#extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#bill = 0
#if size == "S":
#    bill += 15
#elif size == "M":
#    bill += 20
#else:
#    bill += 25
#if add_pepperoni == "Y":
#    if size == "S":
#        bill += 2
#    else:
#        bill += 3
#if extra_cheese == "Y":
#    bill += 1
#print(f"Your final bill is: ${bill}.")

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined_names = name1 + name2
lower_case = combined_names.lower()

t = lower_case.count("t")
r = lower_case.count("r")
u = lower_case.count("u")
e = lower_case.count("e")

true = t + r + u + e

l = lower_case.count("l")
o = lower_case.count("o")
v = lower_case.count("v")
e = lower_case.count("e")

love = l + o + v + e

score = str(true) + str(love) #or score = int(str(true) + str(love))
intscore = int(score)

if (intscore < 10) or (intscore > 90):
    print(f"Your score is {intscore}, you go together like coke and mentos.")
elif (intscore >= 40) and (intscore <= 50):
    print(f"Your score is {intscore}, you are alright together.")
else:
    print(f"Your score is {intscore}.")