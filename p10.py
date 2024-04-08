def findDilnuku(a, b, c, k):
    dilnuku = []

    if a % k == 0:
        dilnuku.append(a)
    if b % k == 0:
        dilnuku.append(b)
    if c % k == 0:
        dilnuku.append(c)

    return dilnuku

a = int(input("Введіть число a: "))
b = int(input("Введіть число b: "))
c = int(input("Введіть число c: "))
k = int(input("Введіть дільник k: "))

dilnuku = findDilnuku(a, b, c, k)

if dilnuku:
    print(f"Число {k} є дільником чисел:", dilnuku)
else:
    print(f"Число {k} не є дільником жодного з чисел {a}, {b}, {c}.")