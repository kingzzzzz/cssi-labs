print(" Welcome to Z's Calculator ! ")

num1 = int(raw_input("Give me a number: "))
num2 = int(raw_input("Give me a number: "))

def myAddFucntion(add1, add2):
    sum = add1 + add2
    return sum

print("Here is the sum: " + str(myAddFucntion(num1,num2)))
