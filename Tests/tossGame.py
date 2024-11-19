import random

choices = ['Heads', 'Tail']

def is_correct_input():
    while True:
        try:
            your_bet = int(input("Enter your choice: 0 for Heads, 1 for Tails: "))
            if your_bet in [0,1]:   
                return your_bet
            else:
                print("Invalid choice. Please enter between 0, 1")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_coin_side():
    return random.randint(0,1)

def get_side_name(coin):
    return choices[coin]

def view_side(myChoice, compChoice):
    print(f"My bet is {myChoice}, The coin is {compChoice}")

def get_result(myChoice, compChoice):
    if myChoice == compChoice:
        return 'Win'
    else:
        return 'Lose'

def view_result(result):
    print(f"You {result}")

def play():
    bet = is_correct_input()
    coin = get_coin_side()
    compChoice = get_side_name(coin)
    myChoice = choices[bet]
    view_side(myChoice, compChoice)
    result = get_result(myChoice, compChoice)
    view_result(result)

play()  