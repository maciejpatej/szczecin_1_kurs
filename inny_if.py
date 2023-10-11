x = 0

match x:
    case []:
        print("pusta lista")
    case [1]:
        print("lista z jednym elementem", x)
    case [1, 2]:
        print("lista z dwoma elementami", x)
    case [1, 2, 3]:
        print("lista z trzema elementami", x)
    case _:
        print("Inny przypadek...")


if x is None:
    print("Pusta lista")
elif x == [1]:
    print("Lista z jednym elementem o wartości 1")
elif x == [1, 2]:
    print("Lista z dwoma elementami: 1 i 2")
elif x == [1, 2, 3]:
    print("Lista z trzema elementami: 1, 2 i 3")
else:
    print("Inna lista")

