# write a program to find wheather a user name contains less than 10 characters or not 

username = input("Enter your username: ")
if len(username) < 10:
    print("Your username contains less than 10 characters.")   
else:
    print("Your username contains 10 or more characters.")
    