# Number Guessing Game

import random

numbers=[1,2,3,4,5,6,7,8,9]

computer_number=random.choice(numbers)

while True:
    my_choice = int(input("Enter one number from 1 to 9: "))

    if my_choice==computer_number:
        print("Congratulations!! You are right.")

        break

    else:
        print("You are wrong!")

