class Matematyka:

    @staticmethod
    def dodaj(a, b):
        return a + b

    @staticmethod
    def odejmij(a, b):
        return a - b

    def pomnoz(self, a, b):
        return a * b


wynik1 = Matematyka.dodaj(5, 3)
# wynik2 = Matematyka.pomnoz(Matematyka, 3, 4)

print(wynik1)
# print(wynik2)
