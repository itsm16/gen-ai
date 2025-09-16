class Car:
    type = "manual";

Car.engine = "V8"
Car.type = "Automatic"

# print(Car.type)


some_car = Car();
other_car = Car();
some_car.type = "Manual";

print(other_car.type)
print(some_car.type)
