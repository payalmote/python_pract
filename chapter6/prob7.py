# program to find out whether a given post is talking about "Harry" or not.

post = input("enter your post: ")

if ("harry" in post.lower()):
    print("the given post is talking about harry")

else:
    print("the given post is not talking about harry")