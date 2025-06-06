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
# a=int(input("Enter a number:"))
# if a%2==0 and a%3==0 :
#     print(f"the number {a} is divisible by 2 and 3")
# else:
#     print(f"the number {a} is not divisible by 2 and 3")
    

# for i in range(5,10,1):
#     print(i,"ram")
# a=[1,2,3,4]
# for i in range(-1,-5,-1):
#     print(i,'=',a[i])


# b=int(input("enter a number:"))
# for i in range(1,11):
#     a=b*i
#     print(b,'*',i,'=',a)

# a=[1,2,3,4]
# for i in range(1,4,2):
#     print(a[i])
    
# library=['python','maths','software design']
# for i in library:
#     if i=='maths':
#         print('hello')
#         print(i,"book was found")
#         break
#     print(i)

# password1="helloworld"
# b=0
# for i in range(3,0,-1):
#     password=input("enter your password:")
#     if password==password1:
#         print('you are welcome')
#         break
#     elif(password!=password1):
#         b=b+1
#     print(3-b,'attempts left')
#     if b==3:
#         print('you have been blocked')
    
    
# username='admin'
# password=1234
# for i in range(3):
#     user_input=input("enter a vaslid username:")
#     passw=int(input("enter a valid password:"))
#     if username==user_input and password==passw:
#         print("you are welcome")
#         break
#     else:
        
# a=[1,2,3,"d",4,5,"a"]
# integers=[]
# string=[]
# for a in a:
#     if type(a)==int:
#         integers.append(a)
#     elif type(a)==str:
#         string.append(a)
# print("integer", integers)
# print("string", string)

# for i in range(5,10,1):
#     print(i," ram ")

# a=[1,2,3,4]
# for i in a:
#     if(i==1):
#         continue
#     if(i==3):
#         continue
#     print(i)

# num=int(input("Enter a number : "))
# for i in range(1,11,1):
#     print(num, "x", i, " = ", num*i)

# actual="4444"
# c=0
# for i in range(0,3):
#     password=input("Enter your Password : ").lower()
#     if(password==actual):
#         print("Welcome !!!")
#         break
#     elif(password!=actual):
#         c=c+1
#         if(c==3):
#             print("You are Blocked !!")
#             break
#         print("You have ",3-c, "attempt left")
        
        
        
#Given list is [1,2,3,"d",4,5,"a"] separate the elements based on their datatypes.


# given=[1,2,3,"d",4,5,"a"]
# integer=[]
# string=[]

# for i in given:
#     if(isinstance(i,int)):
#         integer.append(i)
#     else:
#         string.append(i)

# print(integer)
# print(string)
        
#    Finding Even Number from a list list- 1, 2,3,4,5,6,7,8]
# given=[1,2,3,4,5,6,7,8]

# for i in given:
#     if(i%2==0):
#         print(i)

# Write a Python program that asks the user to enter a word, and then uses a loop to count how many vowels are in that word.

# word=input("Enter a word : ").lower()
# vowel=['a','e','i','o','u']
# c=0
# for i in word:
#     if i in vowel:
#         c=c+1
# print("There are",c, "vowel in",word)
    



# Write a program that records attendance from a list of students and also displays the list of students who were absent.

# total=['suman','ganesh','aayush','chirayu','bikalpa','yanish','rupak','prasanga']
# present=[]
# absent=[]

# for i in total :
#     print(i)
#     attendance=input("Enter yes if this student is present : ").lower()
#     if(attendance=="yes"):
#         present.append(i)
#     else:
#         absent.append(i)
        
# print("Present Students are : ",present)
# print("Absent Students are : ",absent)
    





# Write a Python program that simulates attendance tracking for a list of students over multiple dates.
# The program should:
#   Store a predefined list of student names (['ram' , 'sita', 'hari']).
#   Store a list of attendance dates (['2025-01-10', '2025-01-11']).
#   Ask the user for each student on each date whether they are present (yes or no).
#   Count and store how many days each student was present.
#   Print the final attendance record showing each student's total number of present days.


# students = ['ram', 'sita', 'hari']
# dates = ['2025-01-10', '2025-01-11']

# # Dictionary to store attendance counts
# attendance_record = {student: 0 for student in students}

# for i in dates:
#     print(f"Attendance for date: {i}")
#     for j in students:
#         response = input(f"Is {j} present on {i}? (yes/no): ").strip().lower()
#         if response == 'yes':
#             attendance_record[j] += 1


# print("\nFinal Attendance Record:")
# for j, count in attendance_record.items():
#     print(f"{j}: {count} day(s) present")

# softwarica_building_floor=['floor1','floor2','floor3']
# room_in_each_floor=['room1','room2','room3']
# for i in softwarica_building_floor:  
#     if i == 'floor1' :
#      continue           
# for j in room_in_each_floor: 
#     if i=='floor2' and j in ['room2','room3'] or \
#         i == 'floor3' and j in ['room1','room3']:
#          continue
#     print(i,'=',j)                        
    
    
# for row  in range(6):
#     for colum in range(4):
#         if(colum==0 or colum==4)and (row!=0):
#             print('*',end='')
#         elif(colum==1 or colum==2 or colum==3) and (row==0 or row==3):
#          print('*', end='')
#         else:
#             print(end=" ")
#     print()
    
    
# for row in range(7):
#     for colum in range(4):
#         if(colum==0) and (row!=0 and row!=7):
#             print('*',end='')
#         elif(colum==1 ) and (row==0 or row==7):
#          print('*', end=' ')
#         elif(colum==2 ) and (row==0 or row==4 or row==6):
#          print('*', end=' ')
#         elif(colum==3 ) and (row==0 or row==6 or row==4 or row==5):
#          print('*', end=' ')
#         else:
#             print(end="  ")
#     print()
    


# rows = 7
# cols = 4

# s = {
#     (0, 0),(0, 1),(0, 2),
#     (1, 0),         
#     (2, 0),         
#     (3, 0),(3, 1),(3, 2),
#                   (4, 2),
#                   (5, 2),
#     (6, 0), (6,1),(6, 2),
# }


# for row in range(rows):
#     for col in range(cols):
#         if (row, col) in s:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()  



























# rows=7
# cols=4

# a={
#     (0, 0),(0, 1),(0, 2),
#     (1, 0),        (1, 2),
#     (2, 0),       (2, 2),
#     (3, 0), (3, 1),(3, 2),
#     (4, 0),       (4, 2),
#     (5, 0),       (5, 2),
#     (6, 0),       (6, 2),
# }

# for row in range(rows):
#     for col in range(cols):
#         if (row,col) in a:
#             print('*', end=" ")
#         else:
#             print(" ", end=" ")
#     print()



