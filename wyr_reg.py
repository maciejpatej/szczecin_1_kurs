import re

tekst = "Python to nie tylko gad, ale także język programowania"
# wynik = re.match(r'', tekst)
wzorzec = re.compile(r'ni')
# wynik = wzorzec.search(tekst)
wynik = wzorzec.finditer(tekst)
lista_wyn = list(wynik)
print(type(wynik))
# print(f'Dopasowano: {wynik.group()}, początek: {wynik.span()[0]}, koniec: {wynik.span()[1]}')
if len(lista_wyn) > 0:
    print(f'Dopasowano: {len(lista_wyn)}')
    for w in lista_wyn:
        print(f'Dopasowano: {w.group()}, początek: {w.start()}, koniec: {w.end()}')
else:
    print(wynik)
