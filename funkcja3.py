def product(first: int, *args) -> int:
    result = first
    for x in args:
        result = result * x
    return result


print(product(10))
print(product(10, 20))
print(product(10, 2, 4, 6))


def make_table(**kwargs):
    """Funkcja wypisuje tabele z danymi osobowymi"""
    for key, value in kwargs.items():
        print(f'{key} = {value}')


make_table(name='Jan', surname='Kowalski', age=32)
make_table(name='Anna', surname='Nowak', age=23, city='Poznań')
make_table(name='Anna', city='Poznań')
