milk = True;
black_tea = False;

if served := milk and black_tea:
    print("Tea can be served")
else:
    print("Need both")

print("--------------------------------------------------------------------")

available_tea = ["lemon tea", "ginger tea"];

# if (request := input("Enter the tea: ")) in available_tea:
#     print("Tea is available")
# else:
#     print("Not")


while flavour := input("Enter flavour: ") not in available_tea:
    print("Tea not available")
    break
else:
    print("Maybe available")