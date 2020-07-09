# Implement a class to hold room information. This should have name and
# description attributes.

from item import Item

class Room():
    
    def __init__(self, name, desc):
        self.name = name;
        self.desc = desc;
        self.roomItems = {};

    def getName(self):
        return self.name;

    def getDesc(self):
        return self.desc;

    def addItem(self, item):
        if self.getItem(item.getName()) is not None:
            self.roomItems.get(name).add(item.getQuantity());
        else:
            self.roomItems[item.getName()] = item;
        # self.items.insert(len(self.items), item);

    def getItem(self, name):
        return self.roomItems.copy().get(name);
        

    def getItems(self):
        return self.roomItems;