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
#print("Welcome to the Love Calculator!")
#name1 = input("What is your name? \n")
#name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#to begin i gotta combine the names so it's easier to count later on
#names = name1 + name2

#now i gotta turn the name to lower case so i can start counting
#names = names.lower()

#time to start counting the letters and compare it to TRUE
#t = names.count("t")
#r = names.count("r")
#u = names.count("u")
#e = names.count("e")

#here we gather the full quantity
#true = t + r + u + e

#time to start counting the letters and compare it to LOVE
#l = names.count("l")
#o = names.count("o")
#v = names.count("v")
#e = names.count("e")

#here we gather the full quantity
#love = l + o + v + e

#combining total score
#score = int(str(true) + str(love))
#gotta convert SCORE to INT
#finalscore = int(score)

#time to print the results
#if (score < 10) or (score > 90):
#    print(f"Your score is {score}, you go together like coke and mentos.")
#elif (score >= 40) and (score <= 50):
#    print(f"Your score is {score}, you are alright together.")
#else:
#    print(f"Your score is {score}.")

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[Alaaaan]
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#Write your code below this line 👇
option1 = input('''
Okay, adventurer! You're at a crossroad with a map and you have two options, to turn left or right.
The instruction on the map is not clear enough and you have to make a choice.
To turn RIGHT or LEFT. What will you do?
''').lower()

if option1 == 'right':
  print('''
  You may go ahead, adventurer. Try your luck!
  ''')
  option2 = input('''
  As you go walking down the street you chose, you find a bridge.
  The river seems quiet and unharmful. You have to cross this river so you may get closer to the treasure.
  According to the map you had three options: to cross using the BRIDGE, SWIM to the other side or take the BOAT.
  What will you do?
  ''').lower()
  if option2 == 'boat':
    print('''
    You paddle to the other side safely
    ''')
    option3 = input('''
    As you arrive at the other side the map tells you to go straight on the road you find.
    At the end of the road you find a suspicious house, as described in the map.
    You see three doors: a BLACK door, a WHITE door and BROWN door.
    According to the map two of these doors have deadly traps behind them and it's not clear which doors have traps.
    Which door will you choose?
    ''').lower()
    if option3 == "black":
      print('''
      Congratulations, adventurer. You found the treasure and a safe haven.
      ''')
    elif option3 == "white":
      print('''
      Attatched to the door is an explosive and you explode to pieces. Game over! Start again!
      ''')
    elif option3 == "brown":
      print('''
      Behind this door you unleash an army of zombies and get eaten to death. Game over! Start again!
      ''')
    else:
      print('''
      By doing nothing you realize that the air is poisonous and choke to death. Game over! Start again!
      ''')
  elif option2 == 'swim':
    print('''
    You're attacked by piranas and die. Game over! Start again!
    ''')
  elif option2 == 'bridge':
    print('''
    As you decide to cross and walk towards the bridge, a mysterious fog covers the bridge making it impossible to see anything ahead.
    You suddenly fall into the river and get eaten by piranas. Game over! Start again!
    ''')
  else:
    print('''
    You stay on the beach, rest and a group of cannibals eat you. Game over! Start again!
    ''')
  
else:
  print('''
  Game over. Start Again!
  ''')
  