# write a program to greet all the person name sorted in a list 'l' and which start with 's'
# l = ["Harry", "Soham", "Sachin", "Rahul"]

l = ["Harry", "Soham", "Sachin", "Rahul"]

for name in l:
    if name.startswith("S"):
        print("Hello "+ name)