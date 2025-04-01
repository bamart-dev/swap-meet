class Vendor:
    # inventory attribute, can be passed in or left as default (default is
    #   empty list)
    # add() method - adds an item to inventory list and returns item added
    # remove() method - remove an item from inventory list if the item is
    #   present, else return False
    def __init__(self,inventory = None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self,item):
        self.inventory.append(item)
        return item

    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
