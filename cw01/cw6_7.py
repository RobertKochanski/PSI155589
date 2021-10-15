lista1 = []
for x in range(1, 11):
    lista1.append(x)
# print(lista1)
lista2 = []
for x in range(len(lista1) + 1):
    if x > 5:
        lista2.append(x)
        lista1.remove(x)
# print(lista1)
# print(lista2)
for x in lista2:
    lista1.append(x)
print(lista1)
lista1.insert(0, 0)
print(lista1)

lista3 = lista1
print(lista3)
lista3.sort(reverse=True)
print(lista3)
