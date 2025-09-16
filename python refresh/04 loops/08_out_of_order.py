# flavours = ["Ginger", "Out of Stock", "Lemon", "Discontinued", "Tulsi"]

# for flavour in flavours:
#     if flavour == "Out of Stock":
#         continue
#     if flavour == "Discontinued":
#         break
#     print(f"{flavour} found")

# print("Out of the loop")

staff = [("Amit", 16), ("Zara", 17), ("Raj", 15)]

for name, age in staff:
    if age >= 18:
        print(f"{name} is eligible to manage staff")
        break
else:
    print("No one")