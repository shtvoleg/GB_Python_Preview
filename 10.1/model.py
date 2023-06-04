# Задача 38. Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных.
# (с модулями)
# Обучающийся: Шитов Олег Владимирович, разработка 4544, будни, утро, дата сдачи - 06.06.2023 (до 10:00 мск)

"""
        Функциональный модуль
"""

FILE_BOOK = 'phone_book.txt'
def open_book(FILE_BOOK):                                   # функция считывает телефонную книгу
    contacts = []
    with open(FILE_BOOK, 'r', encoding='utf-8') as file:    # открываю файл из рабочей директории в режиме чтения
        for line in file:                                   # читаю файл построчно
            my_str = line.split(',')                        # фио; телефон
            contacts.append([my_str[0],my_str[1].rstrip()])
    return(contacts)


def save_book(contacts):                          # функция сохраняет телефонную книгу в виде txt-файла
    with open(FILE_BOOK, 'w', encoding='utf-8') as file:    # открываю файл из рабочей директории на запись
        if contacts:
            for line in contacts:
                file.write(line[0]+','+line[1]+'\n')             # запись в файл с разделителем - запятой
        else:
            file.write("")                                  # нет данных -> пустой файл
    return(contacts)


def show_book(contacts):                                    # функция показывает содержимое справочника
    if contacts:
        for i,line in enumerate(contacts,1):                   # вывод в консоль построчно
            print('{:>3}'.format(i)+'   '+'{:<50}'.format(line[0])+line[1])
    else:
        print('*** Телефонный справочник пуст! ***')
    return(contacts)


def my_input(desc):                     # функция производит запрос текстового поля по параметру
    while True:
        str = input(f'Введите {desc}: ').capitalize().strip()
        if str or ( not str and 'отчеств' in desc):     # у контакта отчества может и не быть
            return str
        else:
            print(f'*** Некорректный ввод! ***')


def add_contact(contacts):                               # функция добавляет контакт
    my_str = [[], [], [], []]
    my_str[0] = my_input("фамилию")
    my_str[1] = my_input("имя")
    my_str[2] = my_input("отчество")
    my_str[3] = my_input("номер телефона")
    str = my_str[0]+' '+my_str[1]+' '+my_str[2]
    contacts.append([str, my_str[3]])
    print(f'\n*** Контакт добавлен: "{str}"! ***')
    return(contacts)

def find_contact(contacts):                             # функция производит поиск контактов по ключу в любом поле
    key = input("Введите ключ поиска (любое поле; любой регистр): ").lower()
    if key:
        finded_contacts = []                            # список под набор найденных значений
        for contact in contacts:
            if key in contact[0].lower() or key in contact[1].lower() :
                finded_contacts.append(contact)
        if finded_contacts:
            print(f'\n*** Найдено {len(finded_contacts)} вхождение(я/ий) ключа: ***')
            for i,item in enumerate(finded_contacts,1): # вывод в консоль построчно
                print('{:>3}'.format(i) + '   ' + '{:<50}'.format(item[0]) + item[1])
        else:
            print('*** Ничего не найдено! ***')
    return(contacts)


def change_contact(contacts):                   # функция корректирует контакт
    number = int(input('Для корректировки контакта введите его порядковый номер: '))
    if 1 <= number <= len(contacts):
        choice = input('Что будем корректировать? 1 - фамилию; 2 - имя; 3 - отчество; 4 - номер телефона. Ваш выбор: ')
        if choice.isdigit() and 0 < int(choice) < 5:
            int_choice = int(choice)
            if 0 < int_choice < 4:
                my_str = contacts[number-1][0].split()
                old_value = my_str[int_choice-1]
                my_str[int_choice-1] = my_input("новое значение")
                str = my_str[0] + ' ' + my_str[1] + ' ' + my_str[2]
                contacts[number-1][0] = str
                print(f'*** Изменения выполнены: произведена замена "{old_value.strip()}" на "{my_str[int_choice-1].strip()}". ***')
            else:
                old_value = contacts[number-1][1]
                new_value = my_input("новое значение")
                contacts[number-1][1] = new_value
                print(f'*** Изменения выполнены: произведена замена "{old_value.strip()}" на "{new_value}". ***')
        else:
            print(f'*** Недопустимый выбор: "{choice}"! ***')
    else:
        print(f'*** Такого порядкового номера ("{number}") - нет! ***')
    return(contacts)


def del_contact(contacts):                  # функция удаляет контакт
    number = int(input('Для удаления контакта введите его порядковый номер: '))
    if number < 1 or number > len(contacts):
        print(f'*** Недопустимый номер: "{number}"! ***')
        return(contacts)
    old = contacts.pop(number-1)
    print('\n*** Удалён контакт: ' + '{:>3}'.format(number) + '   ' + '{:<50}'.format(old[0]) + old[1])
    return(contacts)

def clear_book(contacts):                   # функция чистит справочник
    choice1 = input("Очистить телефонный справочник? 1 - да; иное - нет: ")
    if choice1.isdigit() and int(choice1) == 1:
        print('\n*** Cправочник очищен! ***')
        return([])