print("Welcome to Sam's Function Cardio")
# num1 = int(raw_input("Give me a side 1 length: "))
# num2 = int(raw_input("Give me a side 1 length: "))
# num3 = int(raw_input("Give me a side 1 length: "))
#
# def is_triangle(s1,s2,s3):
#     sum1 = s1 + s2
#     sum2 = s2 + s3
#     sum3 = s1 + s3
#
#     if sum1 > s3 and sum2 > s1 and sum3 > s2:
#         print("You have a triangle")
#         return True
#     else:
#         print("No triangle for you!")
#     return False
#
# is_triangle(num1, num2, num3)
#

# This is the reverse string Challenge

# word = str(raw_input("Give me a Word "))
#
# def my_function(x):
#   return x[::-1]
#
# print("This is your word backwards " + my_function(word))

This is the Dice Challenge
import random
game_start = raw_input("Would you like to roll the dice? ")

def dice_roll():
    print("Your number is: " + str(random.randint(1,6)))
    global play_again
    play_again = raw_input("Would you like to play again? ")

if game_start == "yes":
    dice_roll()
    while play_again == "yes":
        dice_roll()
elif game_start == "no":
    print("Game Over ")
else:
    print("Input not recognized ")





# import random
#
# def dice_roll():
#     while True:
#         print("Your number is: " + str(random.randint(1,6)))
#         play_again = raw_input("Would you like to play again? ")
#         while play_again != 'yes':
#             if play_again == 'no':
#                 return print("Game Over ")
#             else:
#                 print("Input not recognized")
#                 play_again = raw_input("Would you like to play again? ")
#
# def main():
#     game_start = raw_input("Would you like to roll the dice? ")
#     if game_start == 'yes':
#         dice_roll()
#     else:
#         print('too bad')
#
# if __name__ == '__main__':
#     main()
