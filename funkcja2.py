def lista(x, items=[]):
    items.append(x)
    return items


while True:
    print("""siemka! Wybierz opcje:
            1. 🤪 liczby
            2. 🤡 teksty
            3. 💩 obojętnie co
    """)
    wynik = []
    opcja = int(input("wybierz opcje (0-3)"))
    if opcja == 1:
        wybor = int(input("Jaką liczbę wstawić?:"))
        wynik = lista(wybor)
        print(wynik)
    elif opcja == 2:
        wybor = input("Jaki tekst wstawić do listy?:")
        wynik = lista(wybor)
        print(wynik)
    elif opcja == 3:
        wybor = input("Co wstawić do listy?:")
        wynik = lista(wybor)
        print(wynik)
    elif opcja == 0:
        wynik.clear()
        break
    else:
        print("niepoprawny znak 💩💩💩")

