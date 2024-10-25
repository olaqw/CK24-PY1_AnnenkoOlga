salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0  # Ввод переменной

for month in range(months):
    money_capital += spend - salary
    spend = spend + (increase * spend)  # Траты за каждый месяц

money_capital = round(money_capital)  # Округление

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
