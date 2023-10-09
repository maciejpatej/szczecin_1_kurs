wiek = 2023 - 1983
str1 = ' to jest tekst 1\n'
str2 = f'wiek = {wiek}\n'
str3 = f"""
**************************
* to też wiek {wiek}      * 
* ale ma specjalne opcje *
* i tu kolejne teksty... * 
**************************"""

print(str1, str2, str3)

tekst = "Kurs Pythonr"
print(tekst.lower())
print(tekst.count("r"))
print(len(tekst))
print(tekst[5])
print(tekst[0:4] + 'y')
print(tekst[:4])
print(tekst[4:])
print(tekst[:10:2])

stary_format = 'Hello %s!'
print(stary_format % "Tomek")

sredni_format = 'Hello {}!'
print(sredni_format.format('TOMEK'))
print(str1, "tu jakiś tekst....", str2)

