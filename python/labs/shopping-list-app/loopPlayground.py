print("Welcome to Z's Loop Playground")

myString = raw_input("Give me a string loop through: ")

#Create a program that will print each letter in the string individually
#using a for loop

letterNUm = 1

for character in myString:
    print("This is letter number %s " % (letterNUm))
    letterNum = letterNum + 1
    print(character)
