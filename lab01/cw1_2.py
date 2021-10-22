lipsum = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"

imie = "Robert"
nazwisko = "Kochański"

litera_1 = imie[2]
litera_2 = nazwisko[3]

ile_i = 0
ile_n = 0

for x in lipsum:
    if x == litera_1:
        ile_i += 1

for x in lipsum:
    if x == litera_2:
        ile_n += 1

print(f"W tekście jest {ile_i} liter {litera_1} oraz {ile_n} liter {litera_2}")