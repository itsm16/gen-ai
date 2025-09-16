# Tuples - immutable

masala_spices = ("cardamom", "cloves", "cinnamon");

(spice1, spice2, spice3) = masala_spices;

print(f"spices contain: {spice1}, {spice2}, {spice3}");


ginger_ratio, cardamom_ratio = 2,1

print(f"ginger to cardamom ratio is - {ginger_ratio} : {cardamom_ratio}");

ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio;

print(f"ginger to cardamom ratio is - {ginger_ratio} : {cardamom_ratio}");

# membership

check = "ginger" in masala_spices;
print(f"To check if ginger exists in masala spices: {check}");
