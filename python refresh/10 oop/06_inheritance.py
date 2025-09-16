class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type}")

class MasalaChai(BaseChai): # inheritance
    def add_spices(self):
        print("Adding cardamom, ginger")

class ChaiShop: # composition
    chai_cls = BaseChai

    def __init__(self):
        self.chai = self.chai_cls("Regular")
