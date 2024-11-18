import random

hands = ['Rock', 'Scissors', 'Paper']
results = {'win': 'You win!', 'lose': 'You lose!', 'draw': 'It\'s a draw'}

def start_message():
    print('Rock-Paper-Scissors Start!')

def get_player():
    print('Enter your choice:')
    input_message = ''
    for index, hand in enumerate(hands):
        input_message += f"{index}: {hand}, "
    input_message = input_message[:-2]  # Remove the last comma and space
    while True:
        try:
            choice = int(input(input_message + " : "))
            if choice in [0, 1, 2]:
                return choice
            else:
                print("Invalid choice. Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_computer():
    return random.randint(0, 2)    

def get_hand_name(hand_number):
    return hands[hand_number]

def view_hand(player, computer):
    print('Your choice is ' + get_hand_name(player))
    print('Computer\'s choice is ' + get_hand_name(computer))

def get_result(hand_diff):
    if (hand_diff == -1 or hand_diff == 2):
        return 'lose'
    elif(hand_diff == 1 or hand_diff == -2):
        return 'win'
    elif hand_diff == 0 :
        return 'draw'
    
def view_result(result):
    print(results[result])
def play():
    start_message()
    while True:
        playersHand = get_player()
        computersHand = get_computer()
        hand_diff = playersHand - computersHand
        view_hand(playersHand, computersHand)
        result = get_result(hand_diff)
        
        view_result(result)
        
        if result != 'draw':  # Exit the loop if the result is not a draw
            break

play()