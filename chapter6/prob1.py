# program to check the greatest no. among the 4 entered by user 

n1 = int(input("enter number1: "))
n2 = int(input("enter number2: "))
n3 = int(input("enter number3: "))
n4 = int(input("enter number4: "))

if(n1>n2 and n1>n3 and n1>n4):
    print("number1 is the greatest number")
elif(n2>n1 and n2>n3 and n2>n4):
    print("number2 is the greatest number")
elif(n3>n1 and n3>n2 and n3>n4):
    print("number3 is the greatest number")
elif(n4>n1 and n4>n3 and n4>n3):
    print("number4 is the greatest number")
else:
    print("all number are equal")