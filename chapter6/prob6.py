# write a program to claculate the grade of student from his marksfrom the from the followin schema
# 90-100 : Ex
# 80-90 : A
# 70-80 : B
# 60-70 : C
# 50-60 : D
# <50 : F

marks = int(input("enter your marks: "))

if (marks>=90 and marks <=100):
    print("your grade is excelelent")

elif(marks>=80 and marks<=90):
    print("your grade is A")

elif(marks>=70 and marks<=80):
    print("your grade is b") 

elif(marks>=60 and marks<=70):
    print("your grade is c")

elif(marks>=50 and marks<=60):
    print("your grade is d")
elif(marks<50):
    print("your grade is f")
     

