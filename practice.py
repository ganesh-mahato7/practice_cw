#1.Write a Python Program to Swap Two Variables
# a=int(input("Enter 1st number"))
# b=int(input("Enter 2nd number"))
# (a,b)=(b,a)
# print(a,b)

# 2. You are developing a simple ticket booking system for a movie theatre.
# The ticket price depends on the age of the person and whether they have a membership card.
# If the person is under 12, the ticket is free. If the person is
# oetween 12 and 60: If they have a membership card, the ticket costs Rs. 150 If not, the ticket costs Rs. 200.
# If the person is above 60, they get a senior citizen discount, and the ticket costs Rs. 100.
# Write a Python program using nested if-else to calculate and print the ticket price based on the user's age
# and membership status.

# age=int(input("Enter your age : "))

# if(age>0):
#     if(age<12):
#         print("You can have the free ticket : ")
#     elif(age>=12 and age<=60):
#         member=input("Enter yes if you are membership : ").lower()
#         if(member=="yes"):
#             print("Your ticket price is Rs 150")
#         else:
#             print("Your ticket price is Rs 200")
#     elif(age>60):
#         print("Your ticket price is Rs 100")
#     else:
#         print("Enter a valid age ")

#3. A utility company charges different rates based on electric usage  :
# If usage < 100 units → Rs. 5 per unit|
# If usage is between 100-300 units:
# First 100 units: Rs. 5
# Next units: Rs. 8
# If usage > 300 units:
# First 100: Rs. 5
# Next 200: Rs. 8
# Remaining: Rs. 10
# Write a Python program using nested if-else to calculate the total bill

# usage=float(input("Enter the amount of unit you consumed : "))
# if usage < 100:
#     total = usage * 5

# elif usage <= 300:
#     first_100 = 100 * 5
#     remaining = (usage - 100) * 8
#     total = first_100 + remaining

# else:
#     first_100 = 100 * 5
#     next_200 = 200 * 8
#     remaining = (usage - 300) * 10
#     total = first_100 + next_200 + remaining

# print(f"Your total charge is Rs. {total}")

    
# 4. Speed rules:
# <= 60 → No fine
# 61-80:
# If license is available → Rs. 500 fine
# Else → Rs. 1000 fine
# Take speed and license status as input and calculate fine.

# speed=float(input("Enter the speed"))
# if(speed<=60):
#     print("No fine !!")
# elif(speed>=61 and speed<=80):
#     lisence=input("Type yes if you have licence").lower()
#     if(lisence=="yes"):
#         print("Your fine is Rs. 500")
#     else:
#         print("Your fine is Rs 1000")
