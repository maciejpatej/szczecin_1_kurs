a = 'helló'
b = a.encode('cp1252')
print(b)
print(a)
print(b.decode('cp1252'))

x = 123.456
y = 1234.456

print(format(x, '0.2f'))
print(format(x, '0.1f'))
print(format(x, '6.1f'))
print(format(y, '6.1f'))
print(format(x, '!<10.2f'))

napis = "Tomek"
print(format(napis, '<10'))
print(format(napis, '-<10'))

name = 'IBM'
shares = 50
price = 549.10

r = '{:>10s} {:10d} {:10.2f}'.format(name, shares, price)
print(r)

import os
import pathlib as path

# names = os.listdir('venv/bin')
# for name in names:
#     print(name)

for filename in path.Path('').glob('*.txt'):
    print(filename)
