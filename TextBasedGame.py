# David Vega
# Southern New Hampshire University
# IT-140 - Intro to Scripting

def check_inventory(rooms, current_room, inventory):
    """ function is passed in rooms, current_room, and inventory.
    checks to see if the item in the current room is already in the inventory list.
    if it is, a message is displayed to user that item already exists.
    """
    if (len(inventory) - 1) == 6:
        print('CONGRATULATIONS BRODY!')
        print('YOU SAVED COOPER!')
    pass

def check_for_items(rooms, current_room, inventory):
    """Function to check to see if items is either an empty string or 'Dog Catcher'
If it neither then it checks to see if the item already exists in inventory.
if not, prompts the user if they would like to add it to inventory.
if user enters 'Yes', item is appended to inventory list and inventory list is shown. resets rooms item key to empty
string so that when user enters that room again it will not prompt them to re-add the item instead lets them know that
they already have that item if user enters 'No', then only the inventory list is displayed."""
    if rooms[current_room]['item'] != '' and rooms[current_room]['item'] != 'Dog Catcher':
        print('You see a {}'.format(rooms[current_room]['item']))
        add_item = input('Add to inventory? Yes or No? ')
        if add_item != 'Yes' and add_item != 'No':
            print("Invalid Entry - (Must enter: Yes or No)")
            add_item = input('Add to inventory? Yes or No? ')
            inventory.append(rooms[current_room]['item'])
            rooms[current_room]['item'] = ''
            print(inventory)
        elif add_item == 'Yes':
            inventory.append(rooms[current_room]['item'])
            print()
            print('Added {} to inventory!'.format(rooms[current_room]['item']))
            print('Inventory Count: {} '.format(len(inventory)))
            print('Inventory: ', inventory)
            rooms[current_room]['item'] = ''

    if rooms[current_room]['item'] == '':
        print('Room is empty.')

def show_status(rooms, current_room, inventory):
    """ function takes in rooms, current_rooms, and inventory
    prints the users current location.
    function call check_for_items() to check if the room has any items
    """
    print('Inventory Count: {}'.format(len(inventory)))
    print('You are in the {}.'.format(current_room))
    check_for_items(rooms, current_room, inventory)

    # return current_room


def user_prompt():
    """ function that requests the user's next move
    and stores it in a variable which it returns
    """
    next_move = input("Enter next move: ")
    return next_move


def move_to_room(rooms, current_room, direction, inventory):
    """function definition that takes in (3) params "rooms, "current_room," and "direction."
    Funcs purpose is to move user between rooms.
    """
    #  While loop runs the statements in its body while the current_room exists in the rooms dictionary.
    while len(inventory) != 6 or rooms[current_room]['item'] != 'Dog Catcher':
        check_inventory(rooms, current_room, inventory)
        show_status(rooms, current_room, inventory)
        if len(inventory) == 6:
            print()
            print('CONGRATULATIONS BRODY!')
            print('YOU SAVED COOPER!')
            break
        if rooms[current_room]['item'] == 'Dog Catcher':
            print('YIKES!! DOG CATCHER!!!')
            print('Cooper\'s gone.')
            print()
            print('*' * 50)
            print(' ' * 17, 'GAME OVER')
            print('*' * 50)
            print()
            break
        next_move = user_prompt()  # Func call and assigns value to next_move.
        print()
        #  IF statement checks to see if next_move contains "exit" if so the loop breaks and the game ends.
        if next_move == 'exit':
            print('Thank you for playing! Goodbye.')
            break
        #  IF statement checks to see if next_move is one of the rooms dictionary keys.
        #  if so, it will assign current_room with the value of the key it found.
        #  ELSE IF next_move is NOT in directions tuple, show "Invalid Entry" message to user.
        #  ELSE show "You can't go that way." message to user
        if next_move in rooms[current_room]:
            # show_status(rooms, current_room, inventory)  # Func call to show current_room.
            current_room = rooms[current_room][next_move]
            # check_for_items(rooms, current_room, inventory)
        elif next_move not in direction:
            print("Invalid Entry - (Must enter: North, South, East, West, or exit)")
            print()
        # elif rooms[current_room]['item'] == "Dog Catcher":
        #     print('YIKES!! DOG CATCHER!!!')
        #     print('Cooper\'s gone.')
        #     print()
        #     print('*' * 50)
        #     print(' ' * 17, 'GAME OVER')
        #     print('*' * 50)
        #     print()
        #     break
        else:
            print()
            print("You can\'t go that way.")
            print()
    else:
        print('CONGRATULATIONS BRODY!')
        print('YOU SAVED COOPER!')


def main():
    """ Function definition for the entry point to the program.
    static local variables are defined here.
    """

    #  Below print statements print the heading of the game
    print()
    print('*' * 50)
    print('            ADVENTURES OF BRODY:')
    print('        DOG CATCHER COOPER SNATCHER')
    print()
    print('  Move commands: North, South, East, West, exit')
    print('*' * 50)
    print()

    # A dictionary for the simplified dragon text game
    # The dictionary links a room to other rooms.
    rooms = {
        'Front Intake Room': {'North': 'Grooming Room', 'South': 'Large Dog Kennel', 'East': 'Yard',
                              'West': 'Supply Closet', 'item': ''},
        'Grooming Room': {'South': 'Front Intake Room', 'East': 'Clinic', 'item': 'Flea Collar'},
        'Clinic': {'West': 'Grooming Room', 'item': 'Tranquilizer Dart'},
        'Yard': {'West': 'Front Intake Room', 'North': 'Animal Control Room', 'item': 'Red Ball'},
        'Supply Closet': {'East': 'Front Intake Room', 'item': 'Thunder Shirt'},
        'Large Dog Kennel': {'North': 'Front Intake Room', 'East': 'Mess Hall', 'item': 'Tranquilizer Gun'},
        'Mess Hall': {'West': 'Large Dog Kennel', 'item': 'Canned Pumpkin'},
        'Animal Control Room': {'South': 'Yard', 'item': 'Dog Catcher'},
        'exit': None
    }
    directions = ('North', 'South', 'East', 'West', 'exit')
    current_room = 'Front Intake Room'
    inventory = []
    move_to_room(rooms, current_room, directions, inventory)

main()  # function call to begin the game. Main entry point of game play.
