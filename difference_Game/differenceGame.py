import random
import math 
level = 1  # Initial game level
col = 5  # Number of columns in the grid
row = 4  # Number of rows in the grid

# Data containing pairs of characters, one of which will appear differently in the grid
data = [['O', '0'], ['l', '1'], ['u', 'v']]
                               
def start_message(): 
    # Display the starting message and current level
    print('Enter the number of the different kanji (e.g., A1)')
    print('Level: ' + str(level))

def view_question():
    # Randomly choose a character pair and the position of the "different" character
    randomArray = data[random.randint(0, 2)]
    mistake_number = random.randint(0, (col * row) - 1)
    print("Debug: mistake number = " + str(mistake_number))  # Debug info
    print(randomArray)

    # Print column headers (A, B, C, etc.)
    print("/|" + ''.join(chr(i + ord('A')) for i in range(col)))
    print("---------")  # Separator for the grid

    # Generate and display the grid
    for i in range(row):
        print(f"{i + 1}|", end="")  # Print row header (1, 2, etc.)
        for j in range(col):
            current_position = i * col + j
            # Place the "different" character at the mistake position
            if current_position == mistake_number:
                print(randomArray[1], end="")
            else:
                print(randomArray[0], end="")
        print()  # Move to the next line for the next row
    return mistake_number  # Return the position of the "different" character

def section_message():
    # Prompt the user for input and convert it to uppercase for consistency
    choice = input('(e.g., A1): ')
    input_str = choice.upper()
    print('Debug: choice = ' + input_str)  # Debug info
    number = change_input_number(input_str)
    print('Debug: input number ' + str(number))  # Debug info
    return number  # Return the user's input as a grid position number

def change_input_number(input_str):
    # Mapping of column letters to their respective indices
    str_data = {chr(i + ord('A')): i for i in range(col)}
    
    # Validate the input format
    if len(input_str) != 2 or input_str[0] not in str_data or not input_str[1].isdigit():
        print("Invalid input. Please enter a valid position (e.g., A1).")
        return -1  # Return -1 for invalid input

    col_number = str_data[input_str[0]]  # Convert column letter to index
    row_number = int(input_str[1]) - 1  # Convert row number to zero-based index

    # Check if the row number is within valid range
    if row_number < 0 or row_number >= row:
        print("Invalid input. Please enter a valid position (1-4 for rows).")
        return -1  # Return -1 for invalid input
  
    input_number = row_number * col + col_number  # Calculate grid position as a single number
    return input_number

def is_correct_number(mistake_number, input_number):
    # Check if the user's input matches the mistake position
    return mistake_number == input_number

def view_result(is_correct):
    # Display whether the user's answer was correct or wrong
    if is_correct:
        print("Correct!")
    else:
        print("Wrong")

def change_string(number):
    # Convert the grid position number back to the corresponding grid label (e.g., A1)
    col_label = chr((number % col) + ord('A'))  # Column as a letter
    row_label = (number // col) + 1  # Row as a number
    correct_number = f"{col_label}{row_label}"
    print("The correct number is " + str(correct_number))  # Display the correct position

def play():
    # Main game loop
    start_message()  # Show start message
    mistake = view_question()  # Display the grid and get the mistake position
    input_number = section_message()  # Get user input and convert it to a grid position
    if input_number == -1:  # Handle invalid input
        print("Invalid input. Please try again.")
        return
  
    is_correct = is_correct_number(mistake, input_number)  # Check if the answer is correct
    view_result(is_correct)  # Display the result
    if input_number != mistake:  # If the answer is wrong, show the correct position
        change_string(mistake)

# Start the game
play()
