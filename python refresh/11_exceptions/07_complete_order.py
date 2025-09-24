class InvalidChaiError(Exception): pass

def bill(flavour, cups):
    menu = {"ginger": 30, "oolong": 40}

    try:
        if flavour not in menu:
            raise InvalidChaiError("Don't have that tea")
        if not isinstance(cups, int):
            raise TypeError("Number of cups should be an integer")
        total = menu[flavour] * cups
        print(f"Your order total is Rs.{total} for {cups} cups of {flavour} tea")
    except Exception as e:
        print(e)
    finally:
        print("Thank you, visit again")

bill("mint", 2)
bill("oolong", "three")
bill("ginger", 3)