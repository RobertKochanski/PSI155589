def ex3(text, letter):
    result = ""
    for x in text:
        if x != letter:
            result += x
    return result


print(ex3("ala ma kota", 'a'))
