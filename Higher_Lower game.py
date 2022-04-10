import random
from game_logo import higher_lower_logo
from game_logo import vs_logo
from game_data import data


def get_account():
    """Get a random account and return it."""
    return random.choice(data)


def get_details(account):
    """Gets the details of the account passed in and returns it in a printable format"""
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}."


def get_result(guess , firstAccount , secondAccount):
    """Check if the user's answer is correct"""
    if account1['follower_count'] > account2['follower_count']:
        answer = 'a'
    else:
        answer = 'b'
    return guess == answer

account2 = get_account()
score = 0
currently_playing = True

while currently_playing:
    print(higher_lower_logo)
    account1 = account2
    account2 = get_account()

    while account2 == account1:
        account2 = get_account()
        
    print(f"Compare A: {get_details(account1)}")
    print(vs_logo)
    print(f"Against B: {get_details(account2)}")
    
    # Ask user to select an option
    guess = input("\nWho has more followers? Type 'A' or 'B': ").lower()

    # check if the user's option is correct
    is_correct = get_result(guess , account1 , account2)


    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        currently_playing = False
        print(f"Sorry that's wrong. Final Score: {score}")
        
