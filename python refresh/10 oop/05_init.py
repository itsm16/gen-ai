class ChaiOrder:
    def __init__(self, type_, size):
        self.type = type_;
        self.size = size;

    def summary(self):
        return f"Type: {self.type}, Size: {self.size}"

someChai = ChaiOrder("Oolong", "100ml");

print(someChai.summary())