salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
spends = []
for i in range(months):
    spends.append(spend * (1 + increase) ** i)
money_capital = sum(spends) - salary * months
r_money_capital = round(money_capital)
if r_money_capital >= money_capital:
    money_capital = r_money_capital
else:
    money_capital = r_money_capital + 1




print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:" , money_capital)
