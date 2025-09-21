class TeaLeaf:
    def __init__(self, age):
        self._age = age # industry standard 
        # using _ before some var that this shouldn't be changed
        # " or that it should have getter setter "
        # python also knows _ and treats it like "age" only not "_age"

    @property
    def age(self): # this method should be named age 
        # and python also treats it as "age"
        return self._age + 2

    @age.setter
    def age(self, age):
        if 1 <= age <= 5:
            self._age = age
        else:
            raise ValueError("Tea age should be between 1 - 5 yrs")
        
leaf = TeaLeaf(2)

# leaf.age = 6 #gives error

print(leaf.age)


            
    