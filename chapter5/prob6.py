# create an empty dictionary. allow 4 friends to enter their favirate language as value and use key 
# use their name. assume their names are unique


d = {}
name = input("enter your name: ")
lang = input("enter the language: ")
d.update({name:lang})

name = input("enter your name: ")
lang = input("enter the language: ")
d.update({name:lang})

name = input("enter your name: ")
lang = input("enter the language: ")
d.update({name:lang})

name = input("enter your name: ")
lang = input("enter the language: ")
d.update({name:lang})

print(d)