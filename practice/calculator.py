def main() -> None:

    print("Добро пожаловать в калькулятор!")

    while True:
        try:
            num1 = float(input("Введите первое число: "))
            break
        except ValueError:
            print("Ошибка: введите корректное число.")
    while True:
        try:
            num2 = float(input("Введите второе число: "))
            break
        except ValueError:
            print("Ошибка: введите корректное число.")

    operations = ['+', '-', '*', '/']
    while True:
        operation = input("Введите операцию (+, -, *, /): ")
        if operation in operations:
            break
        else:
            print("Ошибка: введите допустимую операцию (+, -, *, /).")

    result: float
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Ошибка: деление на ноль.")
            return
        result = num1 / num2

    print(f"Результат: {num1} {operation} {num2} = {result}")


if __name__ == "__main__":
    main()