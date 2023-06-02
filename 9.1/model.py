# Задача 38. Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных.
#
# Обучающийся: Шитов Олег Владимирович, разработка 4544, будни, утро, дата сдачи - 30.05.2023 (до 10:00 мск)

"""
        Функциональный модуль
"""

def open_book(FILE_BOOK):                        # функция считывает телефонную книгу в глобальную переменную contacts
    contacts = []
    with open(FILE_BOOK, 'r', encoding='utf-8') as file:  # открываю файл из рабочей директории в режиме чтения
        show_number = 0
        for line in file:                           # читаю файл построчно
            my_str = line.split()                   # ф; и; о; телефон - всё отдельно
            show_number += 1                        # автонумератор
            str = '{:^3}'.format(show_number)       # временный накопитель строки
            for i in range(len(my_str)):
                str += '{:20}'.format(my_str[i])
            contacts.append(str)
    return(contacts)

def save_book(FILE_BOOK,contacts):                        # функция сохраняет телефонную книгу в виде txt-файла
    with open(FILE_BOOK, 'w', encoding='utf-8') as file:  # открываю файл из рабочей директории на запись
        if contacts:
            for line in contacts:
                my_str = line.split()
                str = my_str[1]+  " " + my_str[2] +" " + my_str[3] + " " + my_str[4] + "\n"
                file.write(str)                                 # запись в файл с разделителем - пробелом
        else:
            file.write("")                                 # пустой файл
    return


def show_book(contacts):                        # функция показывает содержимое справочника
    if len(contacts)==0:
        print('*** Телефонный справочник пуст! ***')
    else:
        print('\n*** Телефонный справочник: ***\n')
        for line in contacts:                   # вывод в консоль построчно
            print(line)
    return(contacts)


def my_input(desc):                     # функция производит запрос текстового поля по параметру
    while True:
        str = input(f'Введите {desc}: ').capitalize().strip()
        if str or ( not str and 'отчеств' in desc):     # у контакта отчества может и не быть
            return str
        else:
            print(f'*** Некорректный ввод! ***')


def add_contact(contacts):                      # функция добавляет контакт
    my_str = [[], [], [], []]
    my_str[0] = my_input("фамилию")
    my_str[1] = my_input("имя")
    my_str[2] = my_input("отчество")
    my_str[3] = my_input("номер телефона")
    str = '{:^3}'.format(len(contacts)+1)
    for i in range(len(my_str)):
        str += '{:20}'.format(my_str[i])
    contacts.append(str)
    print(f'\n*** Контакт добавлен: "{str}"! ***')
    return(contacts)

def find_contact(contacts):                     # функция производить поиск контактов по ключу
    key = input("Введите ключ поиска (любое поле; любой регистр): ").lower()
    if key:
        finded_contacts = []            # список под набор найденных строк
        for contact in contacts:
            if key in contact.lower():
                finded_contacts.append(contact)
        if len(finded_contacts) == 0:
            print('*** Ничего не найдено! ***')
        else:
            print(f'\n*** Найдено {len(finded_contacts)} вхождение(я/ий) ключа: ***')
            for item in finded_contacts:
                print(item)
    return(contacts)


def change_contact(contacts):                   # функция корректирует контакт
    number = int(input('Для корректировки контакта введите его порядковый номер: '))
    if 1 <= number <= len(contacts):
        choice = input('Что будем корректировать? 1 - фамилию; 2 - имя; 3 - отчество; 4 - номер телефона. Ваш выбор: ')
        if choice.isdigit() and 0 < int(choice) < 5:
            if int(choice) == 1:
                old_value = contacts[number-1][3:23]
                new_value = my_input("фамилию")
                str = contacts[number-1][0:3] + '{:20}'.format(new_value) + contacts[number-1][23::]
            elif int(choice) == 2:
                old_value = contacts[number - 1][23:43]
                new_value = my_input("имя")
                str = contacts[number - 1][0:23] + '{:20}'.format(new_value) + contacts[number - 1][43::]
            elif int(choice) == 3:
                old_value = contacts[number - 1][43:63]
                new_value = my_input("отчество")
                str = contacts[number - 1][0:43] + '{:20}'.format(new_value) + contacts[number - 1][63::]
            else:
                old_value = contacts[number - 1][63:]
                new_value = my_input("номер телефона")
                str = contacts[number - 1][0:63] + '{:20}'.format(new_value)
            if new_value!= old_value:
                contacts[number-1] = str
                print(f'*** Изменения выполнены: произведена замена "{old_value.strip()}" на "{new_value.strip()}". ***')
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
    num_cont = 0
    for i in range(len(contacts)):
        num_cont += 1
        str = '{:^3}'.format(num_cont) + contacts[i][3::]
        contacts[i] = str
    print(f'\n*** Удалён контакт: "{old.strip()}"')
    return(contacts)

def clear_book(contacts):                   # функция чистит справочник
    choice1 = input("Очистить телефонный справочник? 1 - да; иное - нет: ")
    if choice1.isdigit() and int(choice1) == 1:
        print('\n*** Cправочник очищен! ***')
        return([])