def pass_reff(list1=[]):
    list1.extend([22, 33])
    print("lista wewnątrz funkcji", list1)


def ff(b):
    global a
    global cyfra
    a = 10
    cyfra = a + b
    return cyfra

a = None
cyfra = None

# print(ff(90))
print(a)
print(cyfra)

list1 = [12, 76, 90]
pass_reff(list1)
print(list1)
