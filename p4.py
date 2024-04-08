def vvid():
    x = int(input("Введи число X: "))
    y = int(input("Введи число Y: "))
    if x == y:
        print("ЧИСЛА НЕ МАЮТЬ БУТИ РІВНІ")
        return(vvid())
    else:
        return x, y
    
def BilshiMenshi(x, y):
    m = min(x, y)
    b = max(x, y)
    new_m = (x + y) / 2
    new_b = x * y * 2
    return new_m, new_b


def main():
    x, y = vvid()

    new_x, new_y = BilshiMenshi(x, y)
    
    print("Менше з цих двох чисел: ", new_x)
    print("Більше з цих двох чисел: ", new_y)

result = main()

print(result)
