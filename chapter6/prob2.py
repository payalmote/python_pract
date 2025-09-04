# write a program to find out weather a student is pass or fail if it requires 40% and atleast 33% in eah
#subject to pass. assume 3 subject and take marks as an input from user

sub1 = int(input("enter ur marks for sub1: "))
sub2 = int(input("enter ur marks for sub2: "))
sub3 = int(input("enter ur marks for sub3: "))

total_percentage = (100*(sub1+sub2+sub3)/300)

if (total_percentage>=40 and sub1>=33 and sub2>=33 and sub3>=33):
    print("pass")

else:
    print("fail")