from .item import Item


class Decor(Item):
    def __init__(self, id=None, condition=0, width=0, length=0):
        super().__init__(id, condition)
        self.width = width
        self.length = length

    def __str__(self):
        category = self.get_category()

        return (f"An object of type {category} with id {self.id}. It takes"
                f" up a {self.width} by {self.length} sized space.")
