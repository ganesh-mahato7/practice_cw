# a=[1,2,3,4]
# i=0
# while a:
#     if i==3:
#      break
#     print(a[i])
#     i=i+1

# a=[1,2,3,4]
# i=0
# while i<4:
#     print(a[i])
#     i=i+1

# a=[1,2,3,4]
# i=0
# while i>=0 and i<4:
#     print(a[i])
#     i=i+1

# a=[1,2,3,4]
# i=0
# while i in range(5):
#     if i==4:
#         break
#     print(a[i])
#     i=i+1

# a=[1,2,3,4]
# i=0
# while i in range(4):
#     print(a[i])
#     i=i+1

# a=[1,2,3,4]
# i=0
# while i<len(a):
#     if a[i]==1 or a[i]==3:
#         i=i+1
#         continue
#     else:
#      print(a[i])
#     i=i+1

# MOBILE BANKING ATEMPTS LEFT
 
password=1234
attempts=3
while attempts>0:
    user_pass=input("Enter your valid password:")
    if user_pass==password :
        print('Welcome')
        break
    elif user_pass!=password :
        attempts=attempts-1
        print(f"you have {attempts} left")
    if attempts==0:
        print("you are blocked")
        break