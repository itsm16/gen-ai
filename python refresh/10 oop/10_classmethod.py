class ChaiOrder:
    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_dict(cls, order_data):
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"],
        )
    
    @classmethod
    def from_str(cls, order_data):
        # tea_type, sweetness, size = order_data.split("-")
        # return cls ()

        res = order_data.split("-")
        return cls(res[0], res[1], res[2])
        


obj = ChaiOrder.from_dict({"tea_type":"oolong", "sweetness":"med", "size":"lg"})
obj1 = ChaiOrder.from_str("oolong-med-large")
obj2 = ChaiOrder("Oolong", "medium", "v-lg")

print(obj.__dict__)
print(obj1.__dict__)
print(obj2.__dict__)
