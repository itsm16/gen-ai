# Dictionary
# all properties of set exist in dictionary

chai_order = dict(type= "Masala Chai", size="Large", sugar=2)
print(chai_order)

chai_recipe = {} # another way
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(chai_recipe)
del chai_recipe["base"];
print(chai_recipe)

# membership 

print("sugar" in chai_recipe);



chai_order = {"type": "Ginger Chai", "size": "Medium"}
keys = chai_order.keys()
values = chai_order.values();
items = chai_order.items();
print(keys);
print(values);
print(items);  # printed as tuple

popped = chai_order.popitem();
print(f"popped: {popped}");

extra_spices = {"cardamom": "crushed", "ginger": "sliced"}
chai_recipe.update(extra_spices);
print(f"updated: {chai_recipe}");

# chai_note = chai_order["note"] 
# # this doesn't exist
# print(f"note: {chai_note}"); # gives error so instead we use get()

customer_note = chai_order.get("note", "No note"); 
print(customer_note);


