# Jeremiah Velez

items = []


def instructions():
    #  show main menu and possible commands
    print('Defeat the Titan Text Adventure Game')
    print('You must collect all 6 items to defeat the Titan, or be crushed to pieces!')
    print('To travel around the map, enter travel North, travel South, travel East, or travel West.')
    print("To add items to your inventory, enter add 'item name'.")


def player_status():
    # show current inventory
    print('Inventory:', items)
    # print(player_placement)


def main():
    rooms = {
        'Your House': {'South': 'Grocery Store', 'North': 'Shoe Store', 'East': 'Hardware Store', 'West': 'Town Pool'},
        'Town Pool': {'East': 'Your House', 'Item': 'Water Gun'},
        'Shoe Store': {'East': 'Gym', 'South': 'Your House', 'Item': 'Shoes'},
        'Gym': {'West': 'Shoe Store', 'Item': 'Barbell'},
        'Hardware Store': {'West': 'Your House', 'North': 'Junkyard', 'Item': 'Bucket'},
        'Junkyard': {'South': 'Hardware Store', 'Item': 'Metal Scrap'},
        'Grocery Store': {'North': 'Your House', 'East': 'Park', 'Item': 'Spinach'},
        'Park': {'West': 'Grocery Store', 'Item': 'Titan'}  # VILLAIN
    }
    user_input = None
    player_placement = list(rooms.keys())[0]
    while user_input != 'Park':
        # while the player is in Your House
        while player_placement == list(rooms.keys())[0]:
            player_status()
            user_input = input('Which direction would you like to go?')
            # If the player moves south move to the Grocery Store
            if user_input == 'travel South':
                player_placement = rooms[player_placement]['South']
                print('You are in the', player_placement)
                break
            # If the player moves a direction with no rooms, tell them they can't go that way
            elif user_input == 'travel North':
                player_placement = rooms[player_placement]['North']
                print('You are in the', player_placement)
                break
            elif user_input == 'travel East':
                player_placement = rooms[player_placement]['East']
                print('You are in the', player_placement)
                break
            elif user_input == 'travel West':
                player_placement = rooms[player_placement]['West']
                print('You are in the', player_placement)
                break
            # If the player does not have a valid input, tell them Invalid Input
            else:
                print('Invalid input!')

        # While the player is in Town Pool
        while player_placement == list(rooms.keys())[1]:
            if 'Water Gun' not in items:
                print("You see a Water Gun")
            player_status()
            user_input = input('What will you do?')
            if user_input == 'add Water Gun':
                items.append(rooms[player_placement]['Item'])
            # If the player moves East
            elif user_input == 'travel East':
                player_placement = rooms[player_placement]['East']
                print('You are in the', player_placement)
                break
            # If the player moves a direction with no rooms, tell them they can't go that way
            elif user_input == 'travel North':
                print("You can't go that way!")
                break
            elif user_input == 'travel West':
                print("You can't go that way!")
                break
            elif user_input == 'travel South':
                print("You can't go that way!")
                break
            # If player enters anything invalid
            else:
                print('Invalid input!')

        # While the player is in Shoe Store
        while player_placement == list(rooms.keys())[2]:
            if 'Shoes' not in items:
                print("You see Shoes")
            player_status()
            user_input = input('What will you do?')
            if user_input == 'add Shoes':
                items.append(rooms[player_placement]['Item'])
            # If the player moves East
            elif user_input == 'travel East':
                player_placement = rooms[player_placement]['East']
                print('You are in the', player_placement)
                break
            # If player moves South
            elif user_input == 'travel South':
                player_placement = rooms[player_placement]['South']
                print('You are in the', player_placement)
            # If the player moves a direction with no rooms, tell them they can't go that way
            elif user_input == 'travel North':
                print("You can't go that way!")
                break
            elif user_input == 'travel West':
                print("You can't go that way!")
                break
            # If player enters anything invalid
            else:
                print('Invalid input!')

        # While the player is at Gym
        while player_placement == list(rooms.keys())[3]:
            if 'Barbell' not in items:
                print("You see a Barbell")
            player_status()
            user_input = input('What will you do?')
            if user_input == 'add Barbell':
                items.append(rooms[player_placement]['Item'])
            # If the player moves West
            elif user_input == 'travel West':
                player_placement = rooms[player_placement]['West']
                print('You are in the', player_placement)
                break
            # If the player moves a direction with no rooms, tell them they can't go that way
            elif user_input == 'travel North':
                print("You can't go that way!")
                break
            elif user_input == 'travel East':
                print("You can't go that way!")
                break
            elif user_input == 'travel South':
                print("You can't go that way!")
                break
            # If player enters anything invalid
            else:
                print('Invalid input!')

        # While the player is at Hardware Store
        while player_placement == list(rooms.keys())[4]:
            if 'Bucket' not in items:
                print("You see a Bucket")
            player_status()
            user_input = input('What will you do?')
            if user_input == 'add Bucket':
                items.append(rooms[player_placement]['Item'])
            # If the player moves West
            elif user_input == 'travel West':
                player_placement = rooms[player_placement]['West']
                print('You are in the', player_placement)
                break
            # If the player moves North
            elif user_input == 'travel North':
                player_placement = rooms[player_placement]['North']
                print('You are in the', player_placement)
                break
            # If the player moves a direction with no rooms, tell them they can't go that way
            elif user_input == 'travel East':
                print("You can't go that way!")
                break
            elif user_input == 'travel South':
                print("You can't go that way!")
                break
            # If player enters anything invalid
            else:
                print('Invalid input!')

        # While the player is at Junkyard
        while player_placement == list(rooms.keys())[5]:
            if 'Metal Scrap' not in items:
                print("You see Metal Scrap")
            player_status()
            user_input = input('What will you do?')
            if user_input == 'add Metal Scrap':
                items.append(rooms[player_placement]['Item'])
            # If the player moves South
            elif user_input == 'travel South':
                player_placement = rooms[player_placement]['South']
                print('You are in the', player_placement)
                break
            # If the player moves a direction with no rooms, tell them they can't go that way
            elif user_input == 'travel North':
                print("You can't go that way!")
                break
            elif user_input == 'travel East':
                print("You can't go that way!")
                break
            elif user_input == 'travel South':
                print("You can't go that way!")
                break
            # If player enters anything invalid
            else:
                print('Invalid input!')

        # While the player is at Grocery Store
        while player_placement == list(rooms.keys())[6]:
            if 'Spinach' not in items:
                print("You see Spinach")
            player_status()
            user_input = input('What will you do?')
            if user_input == 'add Spinach':
                items.append(rooms[player_placement]['Item'])
            # If the player moves East
            elif user_input == 'travel East':
                player_placement = rooms[player_placement]['East']
                if 'Spinach' in items and 'Water Gun' in items and 'Bucket' in items and 'Metal Scrap' in items and 'Shoes' in items and 'Barbell' in items:
                    print('You run into the Titan fully prepared for battle... CONGRATULATIONS! YOU WON!')
                else:
                    print('You ran into the Titan unprepared! He crushes you!')
            # If the player moves North
            elif user_input == 'travel North':
                player_placement = rooms[player_placement]['North']
                print('You are in the', player_placement)
                break
            # If the player moves a direction with no rooms, tell them they can't go that way
            elif user_input == 'travel East':
                print("You can't go that way!")
                break
            elif user_input == 'travel South':
                print("You can't go that way!")
                break
            # If player enters anything invalid
            else:
                print('Invalid input!')


instructions()
main()
