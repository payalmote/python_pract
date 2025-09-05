# write a program to check weather the given number is prime or not

num = int(input("enter the number: "))

for i in range(2, num):
    if (num%i==0):
        print("not a prime number!")
    else:
        print("prime number!")
    break
