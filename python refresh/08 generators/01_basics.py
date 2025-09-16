def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

stall = get_chai_gen();

print(next(stall))
print(next(stall))
print(next(stall))
print(next(stall))

