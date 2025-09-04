# write a program to detect spam comment

p1 = "make a lots of money"
p2 = "click this"
p3 = "subscribe this"
p4 = "buy this now"

message = input("enter comment: ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)): print("this is a spam comment")

else:
    print("this comment is not spam!")