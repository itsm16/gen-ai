# Mutable - list, dictionary

ingredients = ["water", "milk", "black tea"];

for x in ingredients:
    print(f"{x}, ")

ingredients.append("sugar");

print(ingredients)

items_one = ["a", "b", "c"];
items_two = ["d", "e"]

items_one.extend(items_two);
print(items_one);

items_one.reverse();
print(items_one);

items_one.sort();
print(items_one);

items_one.insert(2, "2c");
print(items_one);

popped = items_one.pop();
print(f"popped: {popped}");
print(items_one);

sugar_levels = [1, 2, 3, 4, 5];
print(f"Max and min levels are: {max(sugar_levels)} and {min(sugar_levels)}")


# operator overloading

list_one = ["water", "milk"]
list_two = ["ginger"];
print(list_one + list_two);

print(list_two * 3);


#bytearray

