from .item import Item


class Electronics(Item):
    def __init__(self, id=None, condition=0, type="Unknown"):
        super().__init__(id, condition)
        self.type = type

    def __str__(self):
        category = self.get_category()
        return (f"An object of type {category} with id {self.id}. This is a"
                f" {self.type} device.")
