def print_the_next_number(start):
    print(start + 1)
    if start >= 10:
        return 'Idź na kawę!'
    return print_the_next_number(start + 1)


print(print_the_next_number(5))


def countdown(n):
    if n == 0:
        print("liftoff!")
    else:
        print(n)
        return countdown(n-1)

countdown(3)


# funkcja odliczania, która rekurencyjnie obsłuży start rakiety
# - countdown od liczby całkowitej n, aż osiągniemy 0, na końcu komunikat START