class Human2:

    def __init__(self, wzrost: float, plec: str, imie="Andrzej"):
        """
        Klasa human opisuje człowieka
        :param wzrost: typ float
        :param plec: typ str
        :param imie: typ str
        """
        self.plec = plec
        self.wzrost = wzrost
        self.imie = imie
        self.kolorOczu = 'niebieski'

    def idz_do_roboty(self):
        """
        Metoda symulująca pracę i zarabianie
        :return: wynagrodzenie w typie int
        """
        kasa = 0
        for _ in range(5):
            kasa += 10
        print(f"Zarobione {kasa} $$$ przez {self.imie}")
        return kasa

    def stan_konta(self):
        pass

