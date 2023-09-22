total_cost = 0
tickets = int(input("Введите колличество билетов: "))
for age in range(tickets):
    age = int(input("Введите возвраст посетителя: "))
    if age < 18:
        total_cost  += 0
    elif 18<= age <= 25:
        total_cost  += 990
    elif age > 25:
        total_cost  += 1390
if tickets == 0:
    print("Проходят только дети!")
else:
    print("Колличество билетов: ", tickets)
if tickets > 3:
    discount = total_cost / 100 * 10
    print("Скидка составляет:", "%.2f" % discount, "руб.")
    print("К оплате с учетом скидки:", "%.2f" % (total_cost - discount), "руб.")
if tickets < 4:
    Nodiscount = total_cost
    print("К оплате:", "%.2f" % Nodiscount, "руб.")


