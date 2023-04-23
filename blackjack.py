import random


def deal_card():
    """
    Returns a random card from deck
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    """
    Take the list of cards and returns the score calculated from the cards
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    """
    Evaluate the result of the game
    """
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, computer has blackjack"
    elif user_score == 0:
        return "Win, user has blackjack"
    elif user_score > 21:
        return "Lose, user went over"
    elif computer_score > 21:
        return "Win, computer went over"
    elif user_score > computer_score:
        return "user wins"
    else:
        return "computer wins"


def play_game():
    is_game_over = False
    user_cards = []
    computer_cards = []
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"User cards: {user_cards}, user_score: {user_score}")
        print(f"Computer first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Computer cards: {computer_cards}, computer score: {computer_score}")
    print(compare(user_score, computer_score))
    play_another_game = input('Do you want to play another game: y or n: ')
    if play_another_game == 'y':
        print("\033[H\033[J")
        play_game()


play_game()
