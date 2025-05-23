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


# 5. Determine room price based on guest type and season:
# If guest is "member":
# If season is "peak" → Rs. 4000
# Else → Rs. 3000
# If guest is "non-member":
# If season is "peak" → Rs. 5000
# Else → Rs. 3500
# Take guest type and season as input and print the room price using nested if-else.


# guest=input("Type 'yes' if you are member of the Hotel " ).lower()
# entry=int(input("Enter the month of entry as number : "))
# if(entry>=1 and entry<=6):
#     print("Peak Season")
#     season="peak_season"
# elif(entry>6 and entry<=12):
#     print("Non-Peak Season : ")
#     season="non_peak_season"
    
    
# if(guest=="yes"):
#     if(season=="peak_season"):
#         print("Price is 4000")
#     else:
#         print("price is 3000")
# else:
#     if(season=="non_peak_season"):
#         print("price is 5000")
#     else:
#         print("price is 3500")

#12. A school decided to replace the desks in three classrooms. Each desk sits two students. 
# Given the number of students in each class, print the smallest possible number of desks that can be purchased. 
# The program should read three integers: the number of students in each of the three
# classes, a, b and c respectively. 
# Hint. In the first test there are three groups. The first group has 20 students and thus needs 10 desks. The second group has 21 students, so they can get by with no fewer than 11 desks. 11 desks are also enough for the third
# group of 22 students. So, we need 32 desks in total.

# import math

# class_a = int(input("Enter the number of students in 1st class: "))
# class_b = int(input("Enter the number of students in 2nd class: "))
# class_c = int(input("Enter the number of students in 3rd class: "))

# desks_a = math.ceil(class_a / 2)
# desks_b = math.ceil(class_b / 2)
# desks_c = math.ceil(class_c / 2)

# total_desks = desks_a + desks_b + desks_c
# print("Total number of desks that can be purchased:", total_desks)

# 13. N students take K apples and distribute them among each other evenly. 
# The remaining (the indivisible) part remains in the basket. How many apples will each single student get?
# How many apples will remain in the basket? The program reads the numbers N and K. It should print the two answers for the
# questions above.

# N=int(input("Enter the number of student : "))
# K=int(input("Enter the number of Apple : "))

# apples_per_student = K // N
# apples_remaining = K % N

# print("Each student will get:", apples_per_student, "apples")
# print("Apples remaining in the basket:", apples_remaining)

# 14. Wtite a program to check whether a person is eligible for voting or not.
# (accept age from user)
# age=int(input("enter your age:"))
# nationality=input("enter your nationality:").strip().lower()
# if age>=18 and nationality == "nepali":
#     print("you are eligible to vote")
# else:
#     print("you are not eligible to vote")

# 15. Write a program to weather a number (accepted from user) is divisible by 2 and 3 both.
a=int(input("Enter a number:"))
if a%2==0 and a%3==0 :
    print(f"the number {a} is divisible by 2 and 3")
else:
    print(f"the number {a} is not divisible by 2 and 3")