import re

tekst = "Python to nie tylko gad, ale także język programowania"
# wynik = re.match(r'', tekst)
wynik = re.search(r'nie', tekst)
# print(f'Dopasowano: {wynik.group()}, początek: {wynik.span()[0]}, koniec: {wynik.span()[1]}')
if wynik:
    print(f'Dopasowano: {wynik.group()}, początek: {wynik.start()}, koniec: {wynik.end()}')
else:
    print(wynik)