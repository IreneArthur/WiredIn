import random

print('Rock-Paper-Scissors Start!')

# Prompt the user to input their choice
print('Enter your hand:')
my_hand = int(input('0: Rock, 1: Scissors, 2: Paper: '))
you_hand = random.randint(0, 2)

if my_hand == 0:
    if you_hand == 0:
        print('It\'s a tie!')
    elif you_hand == 1:
        print('You win!')
    elif you_hand == 2:
        print('You Lose!')
elif my_hand == 1:
    if you_hand == 0:
        print('You lose!')
    elif you_hand == 1:
        print('It\'s a tie!')
    elif you_hand == 2:
        print('You win!')
elif my_hand == 2:
    if you_hand == 0:
        print('You win!')
    elif you_hand == 1:
        print('You Lose!')
    elif you_hand == 2:
        print('It\'s a tie!')