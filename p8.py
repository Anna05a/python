def DodatniNum(a, b, c):
    chyslo = 0
    if a > 0:
        chyslo += 1
    if b > 0:
        chyslo += 1
    if c > 0:
        chyslo += 1
    return chyslo

def main():
    a = int(input("Введіть число a: "))
    b = int(input("Введіть число b: "))
    c = int(input("Введіть число c: "))

    result = DodatniNum(a, b, c)
    print("Кількість додатних чисел серед a, b, c:", result)

result = main()
print(result)