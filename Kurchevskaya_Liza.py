a = 'Не знаю, как там в Лондоне, я не была. Может, там собака — друг'\
' человека. А у нас управдом — друг человека!'
print(a)
b = len(a)
print('1. Посчитать количество символов. ' +'Количество символов: '+ str(b))
c =a[::-1]
print('2. Развернуть строку. ' +'Результат переворачивания исходной строки: '+c)
print('3. Сделать каждое слово с большой буквы ' +'В результате получим: '+ a.title())
print('4. Сделать весь текст прописными буквами ' +'В результате получим: '+ a.upper())
d = 'нд'
dd = 'ам'
ddd = 'о'
print('5. Посчитать число вхождений \"нд\", \"ам\", \"о\" в строку. '+ 'В строке \"нд\" : ',a.count(d),',  \"ам\" : ',a.count(dd),', \"о\" : ',a.count(ddd))
print('6. Самостоятельные задачи')  
print('Сделать весь текст строчными буквами ' +'В результате получим: '+ a.lower())
print('Перевести символы нижнего регистра в верхний, а верхнего - в нижний. ' +'В результате получим: ' +a.swapcprint('Перевести символы нижнего регистра в верхний, а верхнего - в нижний' +'В результате получим: ' +a.swapcase())
k = 'Не знаю, как там в Лондоне, я не была. Может, там собака — друг человека. А у нас, {}, управдом — друг человека!'.format('Миша')
print(k)