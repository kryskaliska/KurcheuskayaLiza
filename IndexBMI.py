ves = int(input('Какой у Вас вес в килограммах? '))
rost = float(input('Какой у Вас рост в метрах? '))
bmi = round(ves / (rost**2))
print('Ваш индекс массы тела: ', bmi)
<<<<<<< HEAD
a = bmi - 17
scale = "16" + "="*a + str(bmi) + "="*(22 - a) + "40"
print(scale)
=======
a = bmi - 20
scale = "20" + "="*a + str(bmi) + "="*(30 - a) + "50"
print(scale)
>>>>>>> d681a2744b6dd835f52de3468c6349257cabd32a
