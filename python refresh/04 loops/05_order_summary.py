names = ["Hitesh", "Meera", "Sam"]
bills = [50, 70, 100]

for name, amount in zip(names, bills):
    print(f"Amount to be payed by {name} : {amount}")