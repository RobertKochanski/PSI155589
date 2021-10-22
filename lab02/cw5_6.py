class Calculator:
    def add(self, x, y):
        return x + y

    def diffetence(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def devide(self, x, y):
        if y == 0:
            return "Nie dziel przez zero"
        return x / y


print(Calculator().add(3, 7))
print(Calculator().diffetence(7, 3))
print(Calculator().multiply(3, 7))
print(Calculator().devide(10, 2))


class ScienceCalculator(Calculator):
    def pow(self, x, y):
        return x ** y


print(ScienceCalculator().pow(2, 4))
