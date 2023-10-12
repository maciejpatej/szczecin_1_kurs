class Human:
    plec = None
    wzrost = 0
    imie = ""

    def idz_do_roboty(self):
        kasa = 0
        for k in range(5):
            kasa += 10
        print(f"Zarobione {kasa} $$$")


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

print(id(czlowiek1), id(czlowiek2))
