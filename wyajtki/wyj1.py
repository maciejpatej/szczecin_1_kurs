def mnozenie(a, b):
    try:
        return a * b
    except TypeError:
        return "błędnie podane dane"


def mnozenie2(a, b):
    try:
        return int(a) * int(b)
    except Exception as e:
        return f"błędnie podane dane, wystąpił błąd: {e.args}"


# print(mnozenie(2, 2))
# print(mnozenie(2, '2'))
# print(mnozenie('2', '2'))
# print(mnozenie(3, 34))

print(mnozenie2(3, 3))
print(mnozenie2(3, '3'))
print(mnozenie2('a', 'b'))

