# Set

essential_spices = {"cardomom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger"}

print(f"Union: {essential_spices | optional_spices}");

print(f"Intersection: {essential_spices & optional_spices}");

print(f"only essentials: {essential_spices - optional_spices}")

print("cardomom" in essential_spices);