

class Vendor:
    """
    Represents a vendor with a list of inventory items
    """
    def __init__(self,inventory = None):
        """
        instatiates Vendor instances; has attribute 'inventory', which
        initialized as an empty list if no value is passed in.
        """
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self,item):
        """
        Adds item to a vendor's inventory list
        """
        self.inventory.append(item)
        return item

    def remove(self,item):
        """
        Removes an item from a vendor's inventory list if the item is
        present and returns the item; otherwise returns False
        """
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_id(self, id):
        """
        Returns an item by ID number; returns None if no item matches
        the provided ID number
        """
        for item in self.inventory:
            if id is item.id:
                return item

        return None

    def swap_items(self, other_Vendor, my_item, their_item):
        """
        Swaps given item from one vendor's inventory list with an item
        from another vendor's inventory list and returns True. If
        either list is missing the given item, method returns False
        """
        if my_item in self.inventory and their_item in other_Vendor.inventory:
            self.inventory.remove(my_item)
            other_Vendor.inventory.append(my_item)

            other_Vendor.inventory.remove(their_item)
            self.inventory.append(their_item)

            return True
        else:
            return False

    def swap_first_item(self, other_Vendor):
        """
        Swaps the first item in two vendor's inventory lists and
        returns True; if either inventory list is empty, method returns
        False
        """
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
        """
        Returns a list of items in the same category; if none match,
        returns an empty list
        """
        category_list = []
        for item in self.inventory:
            if item.get_category() == category:
                category_list.append(item)

        return category_list

    def get_best_by_category(self, category):
        """
        Returns the best condition item in a vendor's inventory. If no
        item matches the given category, method returns None
        """
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
        """
        Swaps the best item in a given category between two vendor's
        inventories, based on respective priority, and return True. If
        either inventory does not have an item in that category,
        method returns False
        """
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)

        if not my_best_item or not their_best_item:
            return False

        self.inventory.remove(my_best_item)
        self.inventory.append(their_best_item)
        other_vendor.inventory.remove(their_best_item)
        other_vendor.inventory.append(my_best_item)

        return True
