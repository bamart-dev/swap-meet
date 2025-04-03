from .item import Item


class Electronics(Item):
    """
    Represents an Electronics item with an ID number, condition, and
    a type
    """
    def __init__(self, id=None, condition=0, type="Unknown"):
        """
        instatiates Electronics instances; inherits 'id' and
        'condition' attributes from Item class, and initializes a
        'type' attribute with a default of 'Unknown' if no value is
        passed in
        """
        super().__init__(id, condition)
        self.type = type

    def __str__(self):
        """
        Returns a formatted string with an item's description
        """
        category = self.get_category()
        return (f"An object of type {category} with id {self.id}. This is a"
                f" {self.type} device.")
