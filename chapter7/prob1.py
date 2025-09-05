# write a program to print multiplication table of a given number using for loop

no = int(input("enter the number: "))

for i in range(11):
    print(f"{no} x {i} = {no*i}")
    i+=1
