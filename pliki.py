# f = open('tekst.txt', encoding='utf-8')
# text = f.read()
# print(text)
# f.close()
#
# f = open('baza.dat', 'r')
# text = f.read(15)
# print(text)
# f.close()

# f = open('slice.dat', 'a')
# f.write(text)
# f.close()

with open("slice.dat", 'r') as f:
    print(f.readline())
    print(f.readline())
    print(f.readline())


