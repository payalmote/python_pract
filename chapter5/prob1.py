# write a program to create dictionary of hindo words with values as their english translation.
# provide user with an option to look up


dict_hindi = {
    "namasker":"hello", "alvida":"bye", "yeh":"this", "voh":"that"
}
print("available hindi words", dict_hindi.keys())

word = input("enter word to translate: ")

print("english translation: ", dict_hindi.get(word))