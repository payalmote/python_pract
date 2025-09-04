import os

# specify the directory you want to list
# '.' means current directory
directory = '/'

try:
    print(f"Contents of directory: {directory}\n")
    for item in os.listdir(directory):
        print(item)
except FileNotFoundError:
    print("Directory not found!")
except PermissionError:
    print("You don’t have permission to access this directory.")
