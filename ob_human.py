class Human:
    plec = None
    wzrost = 0
    imie = ""

    def idz_do_roboty(self):
        kasa = 0
        for _ in range(5):
            kasa += 10
        print(f"Zarobione {kasa} $$$ przez {self.imie}")
        return kasa

    def stan_konta(self):
        pass


czlowiek1 = Human()
czlowiek1.imie = "Tomek"
czlowiek1.wzrost = 176
czlowiek1.plec = 'm'
print(czlowiek1.imie)
print(czlowiek1.wzrost)
print(czlowiek1.plec)

czlowiek2 = Human()
czlowiek2.imie = "Marta"
czlowiek2.wzrost = 166
czlowiek2.plec = 'k'
czlowiek2.idz_do_roboty()
print(czlowiek2.imie)
print(czlowiek2.wzrost)
print(czlowiek2.plec)
marta_konto = czlowiek2.idz_do_roboty()
tomek_konto = czlowiek1.idz_do_roboty()
print(marta_konto)
print(tomek_konto)
print(id(czlowiek1), id(czlowiek2))
print("Razem mają na koncie:", marta_konto + tomek_konto)
