class Human2:

    def __init__(self, wzrost: float, plec: str, imie="Andrzej"):
        self.plec = plec
        self.wzrost = wzrost
        self.imie = imie
        self.kolorOczu = 'niebieski'

    def idz_do_roboty(self):
        kasa = 0
        for _ in range(5):
            kasa += 10
        print(f"Zarobione {kasa} $$$ przez {self.imie}")
        return kasa

    def stan_konta(self):
        pass

