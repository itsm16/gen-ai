class Chai:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
    
obj = Chai(2,3)
print(obj.add())

class NewChai:
    @staticmethod
    def add(a, b):
        return a + b

added = NewChai.add(4,6)
print(added)

