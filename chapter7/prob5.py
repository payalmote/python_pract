# write a program to sum first n natural numbers using while loop

n = int(input("enter the number: "))
i=1
sum = 0
while (i<=n):
    sum = sum + i
    i+=1
print("the sum is: ", sum)