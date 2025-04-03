from .item import Item


class Decor(Item):
    """
    Represents a Decor item with an ID number, condition, a width, and
    a length
    """
    def __init__(self, id=None, condition=0, width=0, length=0):
        """
        instatiates Decor instances; inherits 'id' and 'condition'
        attributes from Item class, and initializes 'width' and
        'length' attributes with a defaults of 0 if no value is
        passed in
        """
        super().__init__(id, condition)
        self.width = width
        self.length = length

    def __str__(self):
        """
        Returns a formatted string with an item's description
        """
        category = self.get_category()

        return (f"An object of type {category} with id {self.id}. It takes"
                f" up a {self.width} by {self.length} sized space.")
