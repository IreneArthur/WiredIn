import random

def start_message():
    print('Rock-Paper-Scissors Start!')

def get_player():
    print('Enter your hand:')
    my_hand = int(input('0: Rock, 1: Paper, 2: Scissors: '))
    return my_hand

def get_computer():
    comp_hand = random.randint(0, 2)
    return comp_hand

def view_result(hand_diff):
    if (hand_diff == -1 or hand_diff == 2):
        print('You lose!')
    elif(hand_diff == 1 or hand_diff == -2):
        print('You Win!')
    elif hand_diff == 0 :
        print('it\'s a Draw')

def get_hand_name(hand_number):
    if hand_number == 0:
        return 'Rock'
    elif hand_number == 1:
        return 'Paper'
    elif hand_number == 2:
        return 'Scissors'
    else:
        return 'unknown'
    return choice

def view_hand(player, computer):
    playerChoice = get_hand_name(player)
    compChoice = get_hand_name(computer)
    print(f"Your choice is {playerChoice} and the computer\'s choice is {compChoice} so")

start_message()
playersHand = get_player()
computersHand = get_computer()
hand_diff = playersHand - computersHand
view_hand(playersHand, computersHand)
view_result(hand_diff)