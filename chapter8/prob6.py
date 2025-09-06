
def rem(l , word):
    n=[]
    for item in l:
        if not (word == item):
            n.append(item.strip(word))
    return n

l = ["Payal", "Prajwal", "Sachin", "an", "Rohan"]

print(rem(l, "an"))