f = open("poem.txt")
content = f.read()
if ("Twinkle" in content):
    print("The word twinkle is in the content")

else:
    print("The word twinkle is not in the content")

f.close()