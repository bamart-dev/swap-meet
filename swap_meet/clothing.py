from .item import Item


class Clothing(Item):

    def __init__(self, id=None, condition=0, fabric="Unknown"):
        super().__init__(id, condition)
        self.fabric = fabric if fabric != "Unknown" else "Unknown"

    def __str__(self):
        category = self.get_category()
        return (f"An object of type {category} with id {self.id}. It is made "
                f"from {self.fabric} fabric.")
