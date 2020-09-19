ves = int(input('Какой у Вас вес в килограммах? '))
rost = float(input('Какой у Вас рост в метрах? '))
BMI = round(ves / (rost**2))
print('Ваш индекс массы тела: ', bmi)
a = bmi - 20
scale = "20" + "="*a + str(bmi) + "="*(30-a) + "50"