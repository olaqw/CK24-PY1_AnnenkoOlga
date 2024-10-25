money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
months = 0  # Ввод переменной

while money_capital > (spend - salary):
    money_capital -= spend - salary
    spend = spend + (increase * spend)  # Траты за каждый месяц
    months += 1

print("Количество месяцев, которое можно протянуть без долгов:", months)
