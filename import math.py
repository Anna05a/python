import math

# Завдання 1
def square_power():
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    c = float(input("Введіть третє число: "))
    
    def power(num):
        if num >= 0:
            return num ** 2
        else:
            return num ** 4
    
    result_a = power(a)
    result_b = power(b)
    result_c = power(c)
    
    print("Результати піднесення до квадрату або четвертої ступеня:")
    print("a:", result_a)
    print("b:", result_b)
    print("c:", result_c)

    square_power()


# Завдання 2
def closest_point():
    x1, y1 = map(float, input("Введіть координати точки A (x1, y1): ").split())
    x2, y2 = map(float, input("Введіть координати точки B (x2, y2): ").split())
    
    def distance(x, y):
        return math.sqrt(x ** 2 + y ** 2)
    
    distance_a = distance(x1, y1)
    distance_b = distance(x2, y2)
    
    if distance_a < distance_b:
        print("Точка A знаходиться ближче до початку координат.")
    elif distance_b < distance_a:
        print("Точка B знаходиться ближче до початку координат.")
    else:
        print("Точки A і B розташовані на однаковій відстані від початку координат.")

closest_point()

# Завдання 3
def triangle_check():
    angle1 = float(input("Введіть перший кут трикутника (в градусах): "))
    angle2 = float(input("Введіть другий кут трикутника (в градусах): "))
    angle3 = 180 - angle1 - angle2
    
    if angle1 > 0 and angle2 > 0 and angle3 > 0:
        print("Такий трикутник існує.")
        if angle1 == 90 or angle2 == 90 or angle3 == 90:
            print("Трикутник є прямокутним.")
        else:
            print("Трикутник не є прямокутним.")
    else:
        print("Такий трикутник не існує.")

triangle_check()


# Завдання 4
def replace_numbers():
    x = float(input("Введіть перше число x: "))
    y = float(input("Введіть друге число y: "))
    
    if x != y:
        smaller = min(x, y)
        larger = max(x, y)
        x = (smaller + larger) / 2
        y = larger * 2
    else:
        x = y = 0
    
    print("Замінені значення:")
    print("x:", x)
    print("y:", y)

    replace_numbers()


# Завдання 5
def point_location():
    x, y = map(float, input("Введіть координати точки A (x, y): ").split())
    
    if x == 0 and y == 0:
        print("Точка розташована в початку координат.")
    elif x == 0:
        print("Точка розташована на осі Y.")
    elif y == 0:
        print("Точка розташована на осі X.")
    elif x > 0 and y > 0:
        print("Точка розташована в першому квадранті.")
    elif x < 0 and y > 0:
        print("Точка розташована в другому квадранті.")
    elif x < 0 and y < 0:
        print("Точка розташована в третьому квадранті.")
    else:
        print("Точка розташована в четвертому квадранті.")

        point_location()


# Завдання 6
def replace_equal_numbers():
    a = int(input("Введіть перше ціле число a: "))
    b = int(input("Введіть друге ціле число b: "))
    
    if a != b:
        greater = max(a, b)
        a = b = greater
    else:
        a = b = 0
    
    print("Замінені значення:")
    print("a:", a)
    print("b:", b)

    replace_equal_numbers()


# Завдання 7
def count_negative():
    a = float(input("Введіть перше число a: "))
    b = float(input("Введіть друге число b: "))
    c = float(input("Введіть третє число c: "))
    
    count = sum(n < 0 for n in [a, b, c])
    print("Кількість негативних чисел:", count)

    count_negative()


# Завдання 8
def count_positive():
    a = float(input("Введіть перше число a: "))
    b = float(input("Введіть друге число b: "))
    c = float(input("Введіть третє число c: "))
    
    count = sum(n > 0 for n in [a, b, c])
    print("Кількість додатніх чисел:", count)

    count_positive()


# Завдання 9
def count_integer():
    a = float(input("Введіть перше число a: "))
    b = float(input("Введіть друге число b: "))
    c = float(input("Введіть третє число c: "))
    
    count = sum(n.is_integer() for n in [a, b, c])
    print("Кількість цілих чисел:", count)

    count_integer()


# Завдання 10
def divisor_check():
    a = float(input("Введіть перше число a: "))
    b = float(input("Введіть друге число b: "))
    c = float(input("Введіть третє число c: "))
    k = float(input("Введіть число k для перевірки як дільника: "))
    
    divisors = [n for n in [a, b, c] if n % k == 0]
    
    print("Число", k, "є дільником чисел:", divisors)

    divisor_check()

