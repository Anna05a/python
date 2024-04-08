def vvid():
    a = int(input("Введіть перше число a: "))
    b = int(input("Введіть друге число b: "))
    return a, b

def zamina(a, b):
    if a != b:
        max_num = max(a, b)
        a = max_num
        b = max_num
    else:
        a = 0
        b = 0
    return a, b

def main():
    a, b = vvid()
    a, b = zamina(a, b)
    print("Результат:")
    print("a =", a)
    print("b =", b)

result = main()
print(result)