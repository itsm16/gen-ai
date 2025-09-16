def some_function():
    print("Order!")
    order = yield
    while True:
        print(f"Input: {order}")
        order = yield

stall = some_function();
next(stall); # start the generator

stall.send("some input")