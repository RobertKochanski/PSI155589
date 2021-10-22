def temp_calc(value, temperature_type):
    if temperature_type == "Fahrenheit" or temperature_type == 1:
        return value * 1.8 + 32
    if temperature_type == "Rankine" or temperature_type == 2:
        return (value + 273.15) * 1.8
    if temperature_type == "Kelvin" or temperature_type == 3:
        return value + 273.15
    else:
        return "Błędna wartość. Podana wartość: " + str(temperature_type)


print("1.Fahrenheit, 2.Rankine, 3.Kelvin")
print(temp_calc(1, 1))
