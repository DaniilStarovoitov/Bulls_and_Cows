"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Daniil Starovoitov
email: daniil.s@seznam.cz
discord: Sweet Procrastination#6256
"""

# greetings
print('''Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.''')

# generation 4 digits
import random

def get_hidden_number():
    while True:
        hidden_number = random.randint(1000, 9999)
        if not_duplicates(hidden_number):
            return hidden_number


# check for no duplicates
def not_duplicates(num):
    if len(str(num)) == len(set(str(num))):
        return True
    else:
        return False

# game
def main():
    tries = 10
    hidden_number = get_hidden_number()

    while tries > 0:
        cows = 0
        bulls = 0
        print('-----------------------------------------------')
        guess_number = input('Enter a number: ')
        if not guess_number.isdigit():
            print('-----------------------------------------------')
            print('Only digits. Try again.')
            continue
        if not not_duplicates(int(guess_number)):
            print('-----------------------------------------------')
            print('No reapeted numbers. Try again.')
            continue
        if int(guess_number) < 1000 or int(guess_number) > 9999:
            print('-----------------------------------------------')
            print('Only 4 digits. Try again.')
            continue

        hidden_number_list = list(str(hidden_number))
        guess_number_list = list(str(guess_number))

        for h, g in zip(hidden_number_list, guess_number_list):
            if g in hidden_number_list:
                if h == g:
                    bulls += 1
                else:
                    cows += 1
        
        if bulls == 1 and cows == 1:
            print(f'You have {bulls} bull and {cows} cow')
        elif bulls == 1:
            print(f'You have {bulls} bull and {cows} cows')
        elif cows == 1:
            print(f'You have {bulls} bulls and {cows} cow')
        else:
            print(f'You have {bulls} bulls and {cows} cows')
        tries -= 1
        guesses = 10 - tries

        if bulls == 4:
            print(f'Correct, you\'ve guessed the right number\nin {guesses} guesses!')
            break
    else:
        print(f'You lose. Number was {hidden_number}')

if __name__ == '__main__':
    main()