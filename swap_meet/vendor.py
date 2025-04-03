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

    def swap_first_item(self, other_Vendor):
        # second way: if not self.inventory or not other_Vendor.inventory:
        if self.inventory == [] or other_Vendor.inventory == []:
            return False

        else:
            first_item_vendor = self.inventory[0]
            first_item_other_vendor = other_Vendor.inventory[0]

            if first_item_vendor and first_item_other_vendor:
                self.inventory.remove(first_item_vendor)
                other_Vendor.inventory.append(first_item_vendor)

                other_Vendor.inventory.remove(first_item_other_vendor)
                self.inventory.append(first_item_other_vendor)

                return True

    def get_by_category(self, category):
        category_list = []
        for item in self.inventory:
            if item.get_category() == category:
                category_list.append(item)

        return category_list

    def get_best_by_category(self, category):
        best_by_category_list = []

        for item in self.inventory:
            if item.get_category() == category:
                best_by_category_list.append(item)

        if not best_by_category_list:
            return None

        best_condition = best_by_category_list[0].condition
        best_condition_item = best_by_category_list[0]

        for item in best_by_category_list:
            if item.condition > best_condition:
                best_condition = item.condition
                best_condition_item = item

        return best_condition_item

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        # my_prio = Electronics
        # their_prio = Clothing
        # swap best Clothing from my inventory with the best Electronic from
        #   their inventory
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)

        if not my_best_item or not their_best_item:
            return False

        self.inventory.remove(my_best_item)
        self.inventory.append(their_best_item)
        other_vendor.inventory.remove(their_best_item)
        other_vendor.inventory.append(my_best_item)

        return True










            # if best_by_category_list:
            #   compare here
            # else:
