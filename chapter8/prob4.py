# write a program to print the following pattern using recursion

def star (n):
    if (n==0):
        return
    print ("*" * n)
    star(n-1)

print(star(10))