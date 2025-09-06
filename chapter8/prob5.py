#  write a program to convert the inches into centimeters

def inch_to_cms(inch):
    return inch*2.54

inch = int(input("Enter the value in inches: "))

print(f"the corresponding value in cm = {inch_to_cms(inch)}")