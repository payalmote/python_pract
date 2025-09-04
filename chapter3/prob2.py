# write a program to fill in a letter template given in the question with name and date
letter = '''
dear <|name|>
you are selected
<|date|>
'''
name = input("enter name: ")
date = input("enter date: ")
print(letter.replace("<|name|>", name).replace("<|date|>", date))