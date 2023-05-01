# Плановый показатель,фактический показатель, вес показателей по привлечению и перевод факта в kpi
promo_plan = 10
promo_fact = 5
promo_kpi_value = 0
promo_kpi = promo_fact/promo_plan
# Плановый показатель,фактический показатель, вес показателей по оттоку и перевод факта в kpi
outflow_plan = 10
outflow_fact = 5
outflow_kpi_value = 1
outflow_kpi = outflow_fact/outflow_plan
# Стандартный размер премии (kpi = 100), фактический общий размер премии и премии по двум отдельным направлениям
normal_bonus = 28000
fact_bonus = 0
fact_promo_bonus = 0
fact_outflow_bonus = 0
# Стандартный размер ЗП и фактический размер ЗП
fact_salary = 0
# Кол-во рабочих дней в месяце, кол-во "дэй-оффов", кол-вол отпускных дней за месяц
work_days_plan = 0
dayoffs = 0
vacation_days = 0
# Итог ЗП до вычета налогов и после вычета налогов
before_tax_salary = 0
final_salary = 0

# Запрашиваем input всех параметров у пользователя
print('Чтобы расчитать точную заработную плату - следуйте инструкциям программы. От вас потребуется лишь ввести параметры задачи. :)')
promo_plan = int(input(f'Введите плановый показатель по привлечению (кол-во подключений): '))
promo_fact = int(input(f'Введите фактический показатель по привлечению на конец месяца (кол-во подключений): '))
promo_kpi_value = float(input(f'Введите вес показателя по привлечению, где 0.3 = 30%, а 1 = 100%: '))
outflow_plan = int(input(f'Введите плановый показатель по оттоку. Если по оттоку не работали - введите 0: '))
if int(outflow_plan) > 0:
    outflow_fact = int(input(f'Введите фактический показатель по оттоку: '))
    outflow_kpi_value = float(input(f'Введите вес показателя по оттокув процентах, где 0.3 = 30%, а 1 = 100%: '
                                    f'введите 0, если не работали по оттоку'))
else: print('Отмена участия оттока в прогнозе')
work_days_plan = int(input(f'Введите общее количество рабочий дней: '))
dayoffs = int(input(f'Введите количество day-off за месяц: '))
vacation_days = int(input(f'Введите количество отпускных дней за месяц: '))
weekends = int(input(f'Введите количество дней за свой счёт: '))

# Проводим расчёты KPI по привлечению
promo_kpi = float(promo_fact/promo_plan)
print(f'Ваш KPI по привлечению: {promo_kpi}')

# Проводим расчёты KPI по оттоку, если отток есть (>0)
if int(outflow_plan) > 0:
    outflow_kpi = float(outflow_fact/outflow_plan)
    print(f'Ваш KPI по оттоку: {outflow_kpi}')
else:
    print('Ваш KPI по оттоку: 0')

# Проводим расёт премиальной части по привлечению
if promo_kpi >= 1.2:
    fact_promo_bonus = (normal_bonus)*int(promo_kpi_value)*1.2
    print (f'Ваша премиальная часть по ПРИВЛЕЧЕНИЮ в этом месяце: {fact_promo_bonus}')
elif promo_kpi >= 0.9:
    fact_promo_bonus = ((promo_kpi)*((normal_bonus)*(promo_kpi_value)))
    print (f'Ваша премиальная часть по ПРИВЛЕЧЕНИЮ в этом месяце: {fact_promo_bonus}')
else:
    fact_promo_bonus = 0
    print(f'Ваша премиальная часть по ПРИВЛЕЧЕНИЮ в этом месяце: {fact_promo_bonus}')

# Проводим расчёт премиальной части по оттоку
if outflow_kpi >= 1.2:
    fact_outflow_bonus = (normal_bonus)*int(outflow_kpi_value)*1.2
    print (f'Ваша премиальная часть по ОТТОКУ в этом месяце: {fact_outflow_bonus}')
elif outflow_kpi >= 0.9:
    fact_outflow_bonus = ((outflow_kpi)*((normal_bonus)*(outflow_kpi_value)))
    print (f'Ваша премиальная часть по ОТТОКУ в этом месяце: {fact_outflow_bonus}')
else:
    fact_outflow_bonus = 0
    print(f'Ваша премиальная часть по ОТТОКУ в этом месяце: 0')

# Складываем две части премии и вычисляем негативные корректировки в премию на отпуска,дэй-офыы и дни за свой счёт
fact_bonus = (fact_outflow_bonus)+(fact_promo_bonus)

if dayoffs >0:
    dayoffs_correction = ((normal_bonus)-(int(((fact_outflow_bonus)+(fact_promo_bonus))*(((work_days_plan)-(dayoffs))/(work_days_plan)))))
elif dayoffs == 0:
    dayoffs_correction = 0

if vacation_days >0:
    vacation_correction = ((normal_bonus)-(int(((fact_outflow_bonus)+(fact_promo_bonus))*(((work_days_plan)-(vacation_days))/(work_days_plan)))))
elif vacation_days == 0:
    vacation_correction = 0

if weekends >0:
    weekends_correction = ((normal_bonus)-(int(((fact_outflow_bonus)+(fact_promo_bonus))*(((work_days_plan)-(weekends))/(work_days_plan)))))
elif weekends == 0:
    weekends_correction = 0


# Этот код включает негативное влияние дэй-оффов и отпуска на оклад (фактически не истинно)
#
#if dayoffs >0:
#   dayoffs_correction_salary = (fact_salary-((fact_salary)*(int((work_days_plan)-(dayoffs))/(work_days_plan))))
#elif dayoffs == 0:
#   dayoffs_correction_salary = 0
#
#if vacation_days >0:
#    vacation_correction_salary = (fact_salary-((fact_salary)*(int((work_days_plan)-(vacation_days))/(work_days_plan))))
#elif vacation_days == 0:
#    vacation_correction_salary = 0


# Вычисляем негативные корреектировки в оклад на отпуска, дэй-оффы и дни за свой счёт
fact_salary = 40000
if weekends >0:
    weekends_correction_salary = (fact_salary-((fact_salary)*(int((work_days_plan)-(weekends))/(work_days_plan))))
elif weekends == 0:
    weekends_correction_salary = 0



fact_salary = (fact_salary)-(weekends_correction_salary)
fact_bonus = (fact_bonus)-(dayoffs_correction)-(vacation_correction)-(weekends_correction)
print (f'Фактический оклад (до вычета налогов): {fact_salary}')
print (f'Фактическая премия (до вычета налогов): {fact_bonus}')

final_salary = (((fact_salary)+(fact_bonus))*0.87)
print(f'ФИНАЛЬНЫЙ размер ЗП после вычета налогов: {final_salary}')

close_programm = int(input(f'Введите что угодно, чтобы закрыть :) '))





