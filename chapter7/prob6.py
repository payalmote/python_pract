# write a program to find factorial of a given number using while loop


n = int(input("enter the number: "))
fact = 1

for i in range (1, n+1):
    fact *= i
    i+=1
    if (i==n+1):
        break

print("the factorial of the given number is: ", fact)