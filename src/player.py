# Write a class to hold player information, e.g. what room they are in
# currently.

from item import Item

class Player():

    def __init__(self, name, room):
        self.name = name;
        self.room = room;
        self.playerItems = {};

    def setRoom(self, room):
        self.room = room;

    def getRoom(self):
        return self.room;

    def addItem(self, item):
        if self.getItem(item.getName()) is not None:
            self.playerItems.get(item.getName()).add(item.getQuantity());
        else:
            self.playerItems[item.getName()] = item;

    def dropItem(self, item):
        if self.getItem(item.getName()) is not None:
            self.playerItems.pop(item.getName());
        else:
            print('Player does not have a(n) + ' + item.getName() + '!');

    def getItem(self, name):
        return self.playerItems.get(name);

    def getItems(self):
        return self.playerItems;