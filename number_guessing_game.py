import random

logo = """

  _   _                 _                                           _                                          
 | \ | |               | |                                         (_)                                         
 |  \| |_   _ _ __ ___ | |__   ___ _ __    __ _ _   _  ___  ___ ___ _ _ __   __ _    __ _  __ _ _ __ ___   ___ 
 | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|  / _` | | | |/ _ \/ __/ __| | '_ \ / _` |  / _` |/ _` | '_ ` _ \ / _ \
 | |\  | |_| | | | | | | |_) |  __/ |    | (_| | |_| |  __/\__ \__ \ | | | | (_| | | (_| | (_| | | | | | |  __/
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \__, |\__,_|\___||___/___/_|_| |_|\__, |  \__, |\__,_|_| |_| |_|\___|
                                           __/ |                             __/ |   __/ |                     
                                          |___/                             |___/   |___/                      

"""

EASY = 10
HARD = 5
guess_number = random.randint(1, 100)


def number_check(number):
    if number > guess_number:
        return 1
    elif number == guess_number:
        return 0
    else:
        return -1


def difficulty_level(difficulty_entry):
    if difficulty_entry == 'easy':
        return EASY
    elif difficulty_entry == 'hard':
        return HARD


print(logo)
print("Number guessing game between 1 and 100")
difficulty = input("Enter the difficulty 'easy' or 'hard': ")
no_of_attempts = difficulty_level(difficulty)
while no_of_attempts > 0:
    user_input = int(input("Enter your guess: "))
    result = number_check(user_input)
    if result == 0:
        print(f"You got it right the number is {user_input}")
        break
    elif result > 0:
        no_of_attempts -= 1
        print("Too high")
    elif result < 0:
        no_of_attempts -= 1
        print("Too low")
    print(f"You have {no_of_attempts} attempts remaining")
    if no_of_attempts == 0:
        print('You lost')
    else:
        print("Guess again")
