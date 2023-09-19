import math
import os
import random

os.system('cls')

# "1. Längdcheck för Gröna Lund (gör ett program som kollar längd och godkänner eller nekar besökare)"
# accepted_height = 170 
# customer_height = float(input("Hello dear customer, enter your height "))
# if customer_height >= accepted_height:
#     print("You can pass")
# elif customer_height < accepted_height:
#     print("You're too short!")

"2. Förbättra välkomstprogrammet (nu med koll att man skriver in rätt typ av värden). Använd try"

# print("Hello!")

# user_name = input("Enter your name ")
    
# while True:
#     try: 
#         user_age = int(input("Enter your age "))
#         break
        
#     except:
#         print("You made a misstake entering your age, try again!")
#         continue


"3. Förbättra BMI-kalkylatorn (se till att stoppa användaren från att skriva in fel)"
# print ("Hello dear user, it's my first BMI calculator made on Python") 

# while True:
#     try:
#         weight = float(input("Enter your weight in kgs "))
#         break

#     except:
#         print("You made a misstake while entering your weight, try again!")
#         continue

# while True:
#     try:
#         height = float(input("Enter your height in meters "))
#         break

#     except:
#         print("You made a misstake while entering your height, try again!")
#         continue


# answer = weight/(height**2)

# print ("Your BMI is", answer)


"4. Skapa ett program som beräknar arean på en cirkel (r*r*pi)"

# pi = math.pi

# circel_radius = float(input("Hi! This program can calculate cirkel's area, please enter the radius in cm! "))

# answer = pi*(circel_radius**2)

# print("The area of your circle is", answer)

"5. Gör en miniräknare som kan räkna med alla fyra räknesätt"

# firstValue = float(input("Write first number "))
# secondValue = float(input("Write second number "))
# action = input("Choose an action between '+', '-', '/', '*'")
# answer = 0
# if action == "+" :
#     answer = firstValue + secondValue
# elif action == "-": 
#     answer = firstValue - secondValue
# elif action == "/":
#     answer = firstValue / secondValue
# elif action == "*":
#     answer = firstValue * secondValue

# print (answer)

"6. Tärning med random.randint()"

#number = random.randint(1, 6)
#print(number)

"7. Gör ett program som kastar så många tärningar som användaren väljer"

#times_to_cast_dice = int(input("Write times you want to cast a dice "))

#for x in range(0, times_to_cast_dice):
    #number = random.randint(1,6)
    #print(number)



