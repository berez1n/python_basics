"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""

sec_value = int(input('Введите время в секундах:  '))
hour_value = sec_value // 3600
min_value = sec_value // 60
print(f'Время в формате ч:м:с: {hour_value} : {min_value} : {sec_value}')



