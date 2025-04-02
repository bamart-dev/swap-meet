from uuid import uuid4

# id attribute -unique int by default, but can pass in int value
# get_category() method - returns a string holding the name of the class

class Item:
    def __init__(self, id=None, condition=0):
        self.id = id if id is not None else uuid4().int
        self.condition = condition

    def get_category(self):
        category = type(self).__name__

        return category

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."

    def condition_description(self):
        conditions = {
            0: "Poor",
            1: "Fair - major wear & tear",
            2: "Fair - minor wear & tear",
            3: "Good",
            4: "Open Box",
            5: "Brand New"
        }

        return conditions[self.condition]
