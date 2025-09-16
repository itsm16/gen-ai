def give_quantity_for_chai(tea, milk, sugar):
    print(f"{tea} spoons tea")
    print(f"{milk}ml milk")
    print(f"{sugar} spoons sugar")

give_quantity_for_chai(2, 300, 2); # positional

give_quantity_for_chai(tea=3, milk=400, sugar=4);   # keywords


def special_chai(*args, **kwargs):
    print("Essentials: ", args)
    print(f"Extras: {kwargs}")

special_chai("200ml milk", sugar="2 spoons")


def chai_report():
    return 100, 20 # sold, remaining
sold, remaining = chai_report();
print(f"Sold: {sold}, \nRemaining: {remaining}")