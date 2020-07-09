from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Add items

room['outside'].addItem(Item('Shovel', 'A wooden staff attached to a thin piece of metal.', 1));
room['foyer'].addItem(Item('Vase', 'A small ceramic vase containing a bundle of flowers', 1));
room['overlook'].addItem(Item('Rope', 'A small, and fairly short, coil of rope.', 1));
room['narrow'].addItem(Item('Sapphire', 'A shining blue sapphire.', 1));
room['treasure'].addItem(Item('Coins', 'A small pile of gold pieces.', 100));

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player("Neytorokx", room['outside']);

running = True;

while running:
    playerInput = input("Enter a command: ");
    if "north" in playerInput.split(" ")[0]:
        player.setRoom(player.getRoom().n_to);
        print("North: " + player.getRoom().getName() + " ");
        print(player.getRoom().getDesc());
        for i in player.getRoom().getItems():
            # print(player.getRoom().getItems().get(i).getDesc());
            print("(" + str(player.getRoom().getItems().get(i).getQuantity()) + ") " + player.getRoom().getItems().get(i).getName() + " - " + player.getRoom().getItems().get(i).getDesc());
    elif "south" in playerInput.split(" ")[0]:
        player.setRoom(player.getRoom().s_to);
        print("South: " + player.getRoom().getName() + " ");
        print(player.getRoom().getDesc());
        for i in player.getRoom().getItems():
            print("(" + str(player.getRoom().getItems().get(i).getQuantity()) + ") " + player.getRoom().getItems().get(i).getName() + " - " + player.getRoom().getItems().get(i).getDesc());
    elif "east" in playerInput.split(" ")[0]:
        player.setRoom(player.getRoom().e_to);
        print("East: " + player.getRoom().getName() + " ");
        print(player.getRoom().getDesc());
        for i in player.getRoom().getItems():
            print("(" + str(player.getRoom().getItems().get(i).getQuantity()) + ") " + player.getRoom().getItems().get(i).getName() + " - " + player.getRoom().getItems().get(i).getDesc());
    elif "west" in playerInput.split(" ")[0]:
        player.setRoom(player.getRoom().w_to);
        print("West: " + player.getRoom().getName() + " ");
        print(player.getRoom().getDesc());
        for i in player.getRoom().getItems():
            print("(" + str(player.getRoom().getItems().get(i).getQuantity()) + ") " + player.getRoom().getItems().get(i).getName() + " - " + player.getRoom().getItems().get(i).getDesc());
    elif "get" in playerInput.split(" ")[0]:
        if len(playerInput.split(' ')) >= 2:
            if player.getRoom().getItem(playerInput.split(" ")[1]) is not None:
                player.addItem(player.getRoom().getItem(playerInput.split(" ")[1]));
                print('Picked up (' + str(player.getRoom().getItem(playerInput.split(" ")[1]).getQuantity()) + ') ' + player.getRoom().getItem(playerInput.split(" ")[1]).getName() + '!');
            else:
                print('There is no such item in the room!');
        else:
            print('You must specify the name of the item you wish to pick up!');
    elif "drop" in playerInput.split(" ")[0]:
        if len(playerInput.split(' ')) >= 2:
            if player.getItem(playerInput.split(" ")[1]) is not None:
                print('Dropped (' + str(player.getItem(playerInput.split(" ")[1]).getQuantity()) + ') ' + player.getItem(playerInput.split(" ")[1]).getName() + '!');
                player.dropItem(player.getItem(playerInput.split(" ")[1]));
            else:
                print('There is no such item in your inventory!');
        else:
            print('You must specify the name of the item you wish to drop!');
    elif "inv" in playerInput.split(" ")[0]:
        for i in player.getItems():
            print(player.getItems().get(i).getName());
    elif "exit" in playerInput.split(" ")[0]:
        print("Exiting...");
        running = False;

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
