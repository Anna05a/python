def calculate_formula(x, a, b):
    y = ((x**4 - x**2 - b)/(x - b ))* ((x**3 - x - a)/(x - a))
    return y

a = -10
b = -20
x = -30

y = calculate_formula(x, a, b)
print("a =", a, ", b =", b, ", x =", x, ", y =", y)
