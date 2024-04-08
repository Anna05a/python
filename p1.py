def numbers(num):
    if num > 0:
        return num ** 2
    else:
        return num ** 4

  
def main():
    a = float (input("Введіть перше число:"))
    b = float (input("Введіть друге число:"))
    c = float (input("Введіть третє число:"))

    a = numbers(a)
    b = numbers(b)
    c = numbers(c)

    print("Результат:")
    print("Перше число:", a)
    print("Перше число:", b)
    print("Перше число:", c)

result = main()
print(result)

