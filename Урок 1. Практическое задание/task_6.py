"""
Задание 6.

Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня,
на который результат спортсмена составит не менее b километров.
Программа должна принимать значения параметров a и b
 и выводить одно натуральное число — номер дня.

Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
"""
first_day_res = int(input('Результат за 1й день тренировок в км:  '))
expected_res = int(input('Ожидаемый результат тренировок в км:  '))
day_n = 1
while first_day_res < expected_res:
    day_n += 1
    first_day_res *= 1.1
    print(f'{day_n}-й день: {"%.2f" % first_day_res}')
print(f'Результат: на {day_n}-й день спортсмен достиг результата — не менее'
      f' {expected_res} км.')





