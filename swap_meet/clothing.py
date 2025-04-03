from .item import Item


class Clothing(Item):
    """
    Represents a Clothing item with an ID number, condition, and fabric
    """
    def __init__(self, id=None, condition=0, fabric="Unknown"):
        """
        instatiates Clothing instances; inherits 'id' and 'condition'
        attributes from Item class, and initializes a 'fabric'
        attribute with a default of 'Unknown' if no value is passed in
        """
        super().__init__(id, condition)
        self.fabric = fabric if fabric != "Unknown" else "Unknown"

    def __str__(self):
        """
        Returns a formatted string with an item's description
        """
        category = self.get_category()
        return (f"An object of type {category} with id {self.id}. It is made "
                f"from {self.fabric} fabric.")
