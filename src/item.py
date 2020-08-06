class Item():
    def __init__(self, name, desc, quantity):
        self.name = name;
        self.desc = desc;
        self.quantity = quantity;
    
    def getName(self):
        return self.name;
    
    def getDesc(self):
        return self.desc;

    def getQuantity(self):
        return self.quantity;

    def add(self, addition):
        self.quantity += addition;
