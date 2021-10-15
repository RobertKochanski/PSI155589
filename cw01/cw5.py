imie = "Robert"
nazwisko = "Kochański"

imie = imie[::-1].lower()
nazwisko = nazwisko[::-1].lower()

print(imie[0].upper() + imie[1::] + " " + nazwisko[0].upper() + nazwisko[1::])