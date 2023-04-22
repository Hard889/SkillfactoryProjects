tickets_count = int(input('Введите количество билетов: '))
tickets_sum = 0
print("---")

for i in range(tickets_count):
    print("билет #", i + 1)
    age = int(input("Введите возраст посетителя: "))
    if age < 18:
        print("Этот билет бесплатный")
    elif 18 <= age < 25:
        print("Этот билет стоит 990р")
        tickets_sum += 990
    else:
        print("Этот билет стоит 1390р")
        tickets_sum += 1390
    print("---")

if int(tickets_count) > 3:
    tickets_sum *= 0.9
    print("Применена скидка 10% за количество билетов")

print("Сумма за все билеты равна:", tickets_sum, "рублей")