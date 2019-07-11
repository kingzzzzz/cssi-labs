print(" Welcome to Z's Pluralizer ")
word = str(raw_input(" Please enter a word: "))
num = int(raw_input(" Please enter a number "))


if num == 0 or num > 1 :
    print(str(num) + " " + word + "s")

else :
    print(  str(num) + " " + word)
