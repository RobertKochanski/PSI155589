def ex1(a_list, b_list):
    x = [i for i in a_list if i % 2 == 0]
    y = [i for i in b_list if i % 2 == 1]
    return x + y


list_a = (0, 1, 2, 3, 4, 5, 6, 7)
list_b = (00, 11, 22, 33, 44, 55)

list_c = ex1(list_a, list_b)
print(list_c)
