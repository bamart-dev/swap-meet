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

    def get_by_id(self, id):
        for item in self.inventory:
            if id is item.id:
                return item

        return None

    def swap_items(self, other_Vendor, my_item, their_item):
        # if our item is in our inv AND their item is in their inventory:
        #  return True
        # if our tiem is not in our inv OR their item is not in their inv:
        #  return False
        if my_item in self.inventory and their_item in other_Vendor.inventory:
            self.inventory.remove(my_item)
            other_Vendor.inventory.append(my_item)

            other_Vendor.inventory.remove(their_item)
            self.inventory.append(their_item)

            return True
        else:
            return False
