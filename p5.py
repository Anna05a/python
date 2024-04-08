def cords():
    x = float(input("Введіть координату X точки A: "))
    y = float(input("Введіть координату Y точки A: "))
    return x, y

def vyzn(x, y):
    if x == 0 and y == 0:
        print("Точка A розташована в початку координат")
    elif x == 0:
        print("Точка A розташована на вісі Y")
    elif y == 0:
        print("Точка A розташована на вісі X")
    elif x > 0 and y > 0:
        print("Точка A розташована в першому квадраті")
    elif x < 0 and y > 0:
        print("Точка A розташована в другому квадраті")
    elif x < 0 and y < 0:
        print("Точка A розташована в третьому квадраті")
    elif x > 0 and y < 0:
        print("Точка A розташована в четвертому квадраті")

def main():
    x, y = cords()
    vyzn(x, y)

result = main()
print(result)
