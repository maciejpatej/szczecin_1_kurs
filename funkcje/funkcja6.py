def add_up(x, y):
    return x + y


print(add_up(2, 5))

add_up1 = lambda x, y: x + y
print(add_up1(2, 5))

names = ["Tomek", "Piotrek", "Adam"]
print(tuple(filter(lambda x: len(x) == 4, names)))
print(sorted(names, key=lambda x: len(x), reverse=True))
