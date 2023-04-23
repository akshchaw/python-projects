from art import logo, vs
import random
from game_data import data


def format_data(account):
    """Takes account data and returns the printable format"""
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return f"{account_name}. a {account_descr} from {account_country}"


def check_answer(guess, account_a, account_b):
    """Takes the user guess and checks if user is correct"""
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']
    if a_follower_count > b_follower_count:
        return guess == 'a'
    else:
        return guess == 'b'


score = 0
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)
is_correct = True
print(logo)
while is_correct:
    print(f"Compare A:{format_data(account_a)}")
    print(vs)
    print(f"Against B:{format_data(account_b)}")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    is_correct = check_answer(guess, account_a, account_b)
    if is_correct:
        score += 1
        print(f'You are right, your score is {score}')
        if guess == "b":
            account_a = account_b
        account_b = random.choice(data)
        if account_a == account_b:
            account_b = random.choice(data)
    else:
        print(f'you are wrong, your final score is {score}')
