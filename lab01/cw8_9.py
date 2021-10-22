lista_krotek = [
    (155589, "Robert Kochański"),
    (155620, "Mateusz Baran"),
    (155420, "Jarosław Krupicki")
]
print(type(lista_krotek))
print(type(lista_krotek[1]))

dictionary = dict(lista_krotek)
print(type(dictionary))
print(dictionary)

dictionary["wiek"] = 21
dictionary["email"] = "nr_indeksu@student.uwm.edu.pl"
dictionary["rok_urodzenia"] = 1999
dictionary["adres"] = "..."

print(dictionary)
