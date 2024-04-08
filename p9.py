def integ(num):
    if isinstance(num, int):
        return True
    elif isinstance(num, float):
        return num.is_integer()
    else:
        return False

def check_integers(a, b, c):
    integers = []
    non_integers = []

    if integ(a):
        integers.append(a)
    else:
        non_integers.append(a)

    if integ(b):
        integers.append(b)
    else:
        non_integers.append(b)

    if integ(c):
        integers.append(c)
    else:
        non_integers.append(c)

    return integers, non_integers

a = float(input("Введіть число a: "))
b = float(input("Введіть число b: "))
c = float(input("Введіть число c: "))

integers, non_integers = check_integers(a, b, c)

print("Цілі числа:", integers)
print("Нецілі числа:", non_integers)