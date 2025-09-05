# break continue and pass in loops
# break statement is used to terminate the loop
# continue statement is used to skip the current iteration and move to the next iteration of the loop
# pass statement is used to do nothing, it is a null statement  

for i in range(11):
    if i == 4:
        break
    print(i)
print("loop ended")


for i in range (10):
    if i == 4:
        continue
    print(i)

for i in range (10):
    if i == 5:
        pass
    print("this is pass block") 