ves = int(input('Какой у Вас вес в килограммах? '))
rost = float(input('Какой у Вас рост в метрах? '))
bmi = round(ves / (rost**2))
print('Ваш индекс массы тела: ', bmi)
a = bmi - 17
scale = "16" + "="*a + str(bmi) + "="*(22 - a) + "40"
print(scale)