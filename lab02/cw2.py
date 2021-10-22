def ex2(data_text):
    length = len(data_text)
    letters = []
    for letter in data_text:
        letters.append(letter)
    big_letters = str.upper(data_text)
    small_letters = str.lower(data_text)

    dictionary = {"length": length, "letters": letters, "big_letters": big_letters, "small_letters": small_letters}
    return dictionary


test = ex2("Dog")
print(test)
