import os
def my_delete():

    imenno = input('Что именно хотите удалить папку или файл?')
    if imenno == 'папку':
        delete = input('Введите название папки, которые хотите удалить:')
        os.rmdir(delete)
    elif imenno == 'файл':
        delete2 = input('Введите название файла, которые хотите удалить:')
        os.remove(delete2)
def my_modul():
    path = '.'
    rez = sorted(os.listdir(path))
    for n, item in enumerate(rez):
        print(n + 1, item)

def viktory():
    import random
    scientists = ['Менделеева Д.И.', 'Ломоносова М.В.', 'Вернадского В.И.', 'Карла Линнея', 'Павлова И.П.', 'Флеминга',
                  'Мечникова И.И.', 'Дроздова Н.Н.', 'Бутлерова А.М.', 'Кучерова М.Г']
    date_rod = ['08.02.1834', '19.11.1711', '28.02.1863', '23.02.1707', '26.09.1849', '06.08.1881', '15.05.1845',
                '20.06.1937', '15.09.1828', '03.06.1850']
    print(scientists)
    result = random.sample(scientists, 5)
    print(result)
    balls = 0
    minus = 0
    while True:
        for i in result:
            if i == scientists[0]:
                birth = input(f'Дата рождения {scientists[0]} (в формате [дд.мм.гггг])?')
                if birth == date_rod[0]:
                    print('Верно')
                    balls += 1
                else:
                    print('Неверно: восьмого февраля 1834')
                    minus += 1
            if i == scientists[1]:
                birth = input(f'Дата рождения {scientists[1]} (в формате [дд.мм.гггг])?')
                if birth == date_rod[1]:
                    print('Верно')
                    balls += 1
                else:
                    print('Неверно: девятнадцатого ноября 1711')
                    minus += 1
            if i == scientists[2]:  # год рождения 1863
                birth = input(f'Дата рождения {scientists[2]} (в формате [дд.мм.гггг])?')
                if birth == date_rod[2]:
                    print('Верно')
                    balls += 1
                else:
                    print('Неверно: двадцать восьмого февраля 1863')
                    minus += 1
            if i == scientists[3]:
                birth = input(f'Дата рождения {scientists[3]} (в формате [дд.мм.гггг])?')
                if birth == date_rod[3]:
                    print('Верно')
                    balls += 1
                else:
                    print('Неверно: двадцать третье мая 1707')
                    minus += 1
            if i == scientists[4]:
                birth = input(f'Дата рождения {scientists[4]} (в формате [дд.мм.гггг])?')
                if birth == date_rod[4]:
                    print('Верно')
                    balls += 1
                else:
                    print('Неверно: двадцать шестого сентября 1849')
                    minus += 1
            if i == scientists[5]:
                birth = input(f'Дата рождения {scientists[5]}?(в формате [дд.мм.гггг])')
                if birth == date_rod[5]:
                    print('Верно')
                    balls += 1
                else:
                    print('Неверно: шестого августа 1881')
                    minus += 1
            if i == scientists[6]:
                # год рождения 1711
                birth = input(f'Дата рождения {scientists[6]}?(в формате [дд.мм.гггг])')
                if birth == date_rod[6]:
                    print('Верно')
                    balls += 1
                else:
                    print('Неверно: пятнадцатого мая 1845')
                    minus += 1
            if i == scientists[7]:
                birth = input(f'Дата рождения у {scientists[7]}?(в формате [дд.мм.гггг])')
                if birth == date_rod[7]:
                    print('Верно')
                    balls += 1
                else:
                    print('Неверно: двадцатого июня 1937')
                    minus += 1
            if i == scientists[8]:
                birth = input(f'Дата рождения {scientists[8]}?(в формате [дд.мм.гггг])')
                if birth == date_rod[8]:
                    print('Верно')
                    balls += 1
                else:
                    print('Неверно: пятнадцатого сентября 1828')
                    minus += 1
            if i == scientists[9]:
                birth = input(f'Дата рождения у {scientists[9]}?(в формате [дд.мм.гггг])')
                if birth == date_rod[9]:
                    print('Верно')
                    balls += 1
                else:
                    print('Неверно: третье июня 1850')
                    minus += 1
        zan = (input('Хотите ли начать викторину занова?'))
        if zan == 'Да':
            print('Продолжаем')
        elif zan != 'Да':
            print('До встречи')
            break
    print(f'Количество верных ответов: {balls}')
    print(f'Количество неверных ответов: {minus}')
    print(f'Процент верных ответов: {balls * 100 / 5}')
    print(f'Процент неверных ответов: {minus * 100 / 5}')


def bank_account():
    chet = 0
    spisok_pok = []
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню банковского счета')
        if choice == '1':
            pop = int(input('На какую сумму хотите пополнить счет'))
            chet += pop
        elif choice == '2':
            pok = int(input('Введите сумму покупки'))
            if pok > chet:
                print('недостаточно средств')
            else:
                pok < chet
                kakie = str(input('Название покупки'))
                chet -= pok
                spisok_pok.append(kakie)
        elif choice == '3':
            print('Список покупок:', spisok_pok)
            print(chet)
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')