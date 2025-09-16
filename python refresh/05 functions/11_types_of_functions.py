# recursive

def pour_chai(n):
    print(n)
    if n == 0:
        return "all poured"
    return pour_chai(n-1)

print(pour_chai(3));

# lambda (anonymous functions)

chai_types = ["light", "kadak", "ginger", "kadak"]
strong_chai = list(filter(lambda chai: chai == "kadak", chai_types))
print(strong_chai)