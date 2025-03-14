salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0
months_2 = months

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
while months_2:
    money_capital += spend - salary
    spend += spend*increase
    months_2 -= 1

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital, 2))
