# write a program which finds out weather a given name is present in a list or not

usernames = ['payal', 'sneha', 'riya', 'komal', 'priya']

name = input("enter the name to check: ")

if(name in usernames):
    print("name is present in the list")
else:
    print("name is not present in the list")