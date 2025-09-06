import random
'''
Snake drinks Water → Snake wins
Gun kills Snake → Gun wins
Water douses Gun → Water wins
Same choice = Draw
sanke = 1; water = -1; gun = 0
'''

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
youDict = {'s': 1, 'w':-1, 'g':0}
you = youDict[youstr]
reverseDict = {1: 'sanke', -1 : 'water', 0:'gun'}

print(f"you chose {reverseDict[you]}\ncomputer choice {reverseDict[computer]}")

if (computer==you):
    print("tie!")
else:
    if (computer==-1 and you==1):
        print ("you win!")

    elif (computer==-1 and you==0):
        print ("computer win!")

    elif (computer==1 and you==-1):
        print ("computer win!")
        
    elif (computer==1 and you==0):
        print ("you win!")
        
    elif (computer==0 and you==-1):
        print ("you win!")    

    elif (computer==0 and you==1):
        print ("computer win!")

    else:
        print("something went wrong")