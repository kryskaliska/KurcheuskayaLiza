ves = int(input('Какой у Вас вес в килограммах? '))
rost = float(input('Какой у Вас рост в метрах? '))
BMI = round(ves / (rost**2))
print('Ваш индекс массы тела: ', BMI)
a = BMI - 20
scale = "20" + "="*a + str(BMI) + "="*(30-a) + "50"