from uuid import uuid4


class Item:
    """
    Represents an item with an ID number and a condition
    """
    def __init__(self, id=None, condition=0):
        """
        instatiates Item instances; has attributes 'id', which is
        initialized as a random UUID if no value is passed in, and
        'condition', initialized with 0 if no value is passed in
        """
        self.id = id if id is not None else uuid4().int
        self.condition = condition

    def get_category(self):
        """
        Returns an item's category name as a string
        """
        category = type(self).__name__

        return category

    def __str__(self):
        """
        Returns a formatted string with an item's description
        """
        return f"An object of type {self.get_category()} with id {self.id}."

    def condition_description(self):
        """
        Returns a string description of an item's condition
        """
        conditions = {
            0: "Poor",
            1: "Fair - major wear & tear",
            2: "Fair - minor wear & tear",
            3: "Good",
            4: "Open Box",
            5: "Brand New"
        }

        return conditions[self.condition]
