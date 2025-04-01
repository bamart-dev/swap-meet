from uuid import uuid4

# id attribute -unique int by default, but can pass in int value
# get_category() method - returns a string holding the name of the class

class Item:
    def __init__(self, id=None):
        self.id = id if id is not None else uuid4().int

    def get_category(self):
        category = type(self).__name__

        return category

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
