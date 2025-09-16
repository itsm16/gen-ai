def process_order(item, quantity):
    try:
        price = {"masala": 20}[item]
        cost = price * quantity
        print(f"Total cost is {cost}")
    except KeyError:
        print("Sorry that tea isn't on menu")
    except TypeError:
        print("Quantity should be in number")

process_order("masala", 2)

