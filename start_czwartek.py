from ludzie import ob_human2 as ob
from funkcje import funkcja1 as f1
from kurnik import kury

czlowiek3 = ob.Human2(176.4, 'k', "Ania")
czlowiek3.idz_do_roboty()

print(f1.ksero())

ptak1 = kury.Orzel('orzeł bielik', 100)
ptak1.lataj()
ptak1.wydaj_odglos()
ptak2 = kury.Kura("kura nioska", 1)
ptak2.lataj()
ptak2.produkcja_jaja(5)
ptak2.wydaj_odglos()
