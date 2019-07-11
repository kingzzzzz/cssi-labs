
import random

print("Welcome to Z's Random Playground! ")
print("This is Z's virtual dice! ")

die1 = random.randint(1,6)
die2 = random.randint(1,6)

sum = die1  + die2

if die1 == die2:
     print("The sum of your two dice is %s" % (sum))
     print("You got Double's! Thus you must Roll again")
else:
     print("The sum of your two dice is %s "% (sum))
     print("Thus it is Next player's turn")
