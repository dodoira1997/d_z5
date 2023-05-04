import os
import shutil
import prob
while True:
    print('1.создатьпапку')
    print('2.удалить(файл / папку')
    print('3.копировать(файл / папку')
    print('4.просмотр содержимого рабочей директории')
    print('5.посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7.просмотр информации об операционной системе')
    print('8.создатель программы')
    print('9.играть в викторину')
    print('10.мой банковский счет')
    print('11.смена рабочей директории')
    print('12. выход')
    messenger = input('Выберете пункт меню')
    if messenger == '1':
        creature = input('Введите название папки:')
        if not os.path.exists(creature):
            os.mkdir(creature)
    elif messenger == '2':
        prob.my_delete()
    elif messenger == '3':
        copy_star = input('Введите название  файл, которое хотите копировать:')
        new_copy = input('Введите новое название файла:')
        shutil.copy(copy_star, new_copy)
    elif messenger == '4':
        prob.my_modul()
    elif messenger == '9':
        prob.viktory()
    elif messenger == '10':
        prob.bank_account()
    elif messenger == '12':
        break
