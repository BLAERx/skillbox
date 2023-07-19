# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000
month = 0
student_income = educational_grant
months_expenses = 0
money_needs = 0

while month < 10:
    if month == 0:
        months_expenses = expenses
    elif month >= 1:
        months_expenses *= 1.03
    month += 1
    diference = round(months_expenses-student_income, 2)
    money_needs += diference

print('Студенту надо попросить', money_needs, 'рублей')


# while month < 10:
#     if month == 0:
#         months_expenses = expenses
#     elif month >= 1:
#         months_expenses *= 1.03
#     month += 1
#     diference = round(months_expenses-student_income, 2)
#     money_needs += diference
#     print('Расходы в', month, 'месяце:', diference, ', Итого за', month, 'мес.:', round(money_needs,2))
#
# print('Студенту надо попросить', money_needs, 'рублей')

