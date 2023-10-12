"""
chcemy stwierdzić, czy co najmniej jeden element na
liście ma wynik True (czyli jest w typie bool)
zadbaj o wyświetlenie wyników.
Dopisz po ilu iteracjach odnalazł się TRUE
"""

items = [0, None, 0.0, True, 0, 7]
found = None
licznik = 0
for i in items:
    print("skanuje itemy...", i)
    licznik += 1
    if i:
        found = True
        break
if found:
    print('Znalazłem TRUE!')

print('na pozycji', licznik)
