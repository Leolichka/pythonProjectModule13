count = int(input('Введите количество билетов: '))
age = int(input('Введите возраст посетителя: '))
count1 = 0
price = 0
while count1 != count:
    if 0 <= age < 18:
        print('Для лиц моложе 18 лет билеты бесплатные')
        price = price
        count1 = count1 + 1
    elif 18 <= age <= 25:
        print('Стоимость билетов для данной категории посетителей - 990р.')
        price = price + 990
        count1 = count1 + 1
    elif age > 25:
        print('Стоимость билетов для данной категории посетителей - 1390р.')
        price = price + 1390
        count1 = count1 + 1
    age = int(input('Введите возраст посетителя: '))
if count > 3:
    price = price * 0.9
print('С Вас: ' + str(price) + 'р.')

