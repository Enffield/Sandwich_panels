while True:
    print(f'---Рассчет сэндвич панелей---\n')

    print('Если необходимо рассчитать мин.вату ставим - "+". '
          '\nЕсли ПИР/пенополистирол - "-".\n')

    work = 0
    while True:
        n = str(input('Введите значение: '))
        if n == '+':
            work += 660
            print('Для просчета была выбрана мин.вата.\n')
            break

        elif n == '-':
            work += 560
            print('Для просчета был выбран ПИР/пенополистирол.\n')
            break
        print('Значение введено неверно, попробуйте еще раз.\n')

    while True:
        try:
            metr = float(input('Введите м2:                         ').replace(',', '.'))
            pogmetr = float(input('Введите пог.м:                      ').replace(',', '.'))
            napolnenie = float(input('Введите толщину наполнения в мм:    ').replace(',', '.'))
            price_metall = [float(input('Введите цену за металл(пог.м -> 1): ').replace(',', '.')),
                            float(input('Введите цену за металл(пог.м -> 2): ').replace(',', '.'))]
            price_napolnenie = float(input('Введите цену за наполнение(м3):     ').replace(',', '.'))
        except ValueError:
            print('\nОшибка -> для расчета стоимости должны вводиться только - цифры'
                  '\nРазделитель - точка(".") или запятая(",")\n')
        else:
            break

    sum_metall_front = pogmetr * price_metall[0]
    sum_metall_back_front = pogmetr * price_metall[1] + sum_metall_front
    sum_napolnenie = metr * (napolnenie * 0.001) * price_napolnenie
    sum_work = metr * work
    sum_kley = metr * 0.7 * 395

    sandwich = sum_metall_back_front + sum_napolnenie + sum_work + sum_kley

    print('\nСтоимость за металл:            ', round(sum_metall_back_front, 1),
          '\nСтоимость за наполнение:        ', round(sum_napolnenie, 1),
          '\nСтоимость за работу:            ', round(sum_work, 1),
          '\nСтоимость за клей:              ', round(sum_kley, 1),
          '\nЗапас - 10 000')

    print(f'\nЦена за сэндвич панель(и): {round(sandwich, 3):.3f}')

    price = 0
    while True:
        try:
            price = float(input('\nВведите стоимость за перемещение: ').replace(',', '.')) + sandwich
        except ValueError:
            print('\nОшибка -> для расчета стоимости должны вводиться только - цифры'
                  '\nРазделитель - точка(".") или запятая(",")')
        else:
            break

    print(f'\nЦена за все: {round(price, 3):.3f}(за м2: {round(price / metr, 3):.3f})')

    price_1 = price * 0.1 + price
    price_2 = price * 0.2 + price
    price_3 = price * 0.3 + price

    print(f'\nВарианты выставления счета для клиента: '
          f' \n1. +10% - {round(price_1, 3):.3f}(за м2: {round(price_1 / metr, 3):.3f} '
          f'| Дельта : {round(price_1 - price, 3):.3f}'
          f' \n2. +20% - {round(price_2, 3):.3f}(за м2: {round(price_2 / metr, 3):.3f} '
          f'| Дельта : {round(price_2 - price, 3):.3f}'
          f' \n3. +30% - {round(price_3, 3):.3f}(за м2: {round(price_3 / metr, 3):.3f} '
          f'| Дельта : {round(price_3 - price, 3):.3f}')

    a = input('\nНажмите "Ввод" для еще одного просчета ')
    print('\n---------------------------------------------------\n')
