# Задача 38. Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных.
#
# Обучающийся: Шитов Олег Владимирович, разработка 4544, будни, утро, дата сдачи - 30.05.2023 (до 10:00 мск)

BOOK_MENU = 'book_menu.txt'                 # файл с описанием меню
FILE_BOOK = 'phone_book.txt'                # файл с телефонной книгой
DICT_MENU = { 1:'show_book', 2:'add_contact', 3:'find_contact', 4:'change_contact', 5:'del_contact', \
              6:'clear_book', 7:'save_book', 8:'exit_book' }            # набор функций, соответствующих набору меню

def choice_menu():                     # функция выводит меню с книгой, проверяет выбор и возвращает выбранный пункт
    while True:                        # цикл с проверкой выбора
        try:
            choice = int(input(f"{list_menu}Выберите пункт меню: "))
            if 1 <= choice <= len(DICT_MENU):
                return choice
            else:
                print(f'*** Некорректный выбор: "{choice}". Попробуйте ещё раз! ***')
        except ValueError:
            print('*** Некорректный выбор. Попробуйте ещё раз! ***')

def open_book():                        # функция считывает телефонную книгу в глобальную переменную contacts
    global contacts
    contacts = []
    with open(FILE_BOOK, 'r', encoding='utf-8') as file:  # открываю файл из рабочей директории в режиме чтения
        num_cont = 0
        for line in file:               # построчно
            my_str = line.split()       # разделение строки на ф, и, о, телефон - отдельно
            num_cont += 1
            str = '{:^3}'.format(num_cont)      # автонумерация
            for i in range(len(my_str)):
                str += '{:20}'.format(my_str[i])    # сбор строки по формату, с нумерацией
            contacts.append(str)
    return

def save_book():                        # функция сохраняет телефонную книгу в виде txt-файла
    global contacts
    with open(FILE_BOOK, 'w', encoding='utf-8') as file:  # открываю файл из рабочей директории на запись
        for line in contacts:
            my_str = line.split()
            str = my_str[1]+  " " + my_str[2] +" " + my_str[3] + " " + my_str[4] + "\n"     # запись в файл с разделителем - пробелом
            file.write(str)
    return

def find_contact():                     # функция производить поиск контактов по ключу
    global contacts
    key = input("Введите ключ поиска: ").lower()
    if key:
        finded_contacts = []            # список под набор найденных строк
        for contact in contacts:
            if key in contact.lower():
                finded_contacts.append(contact)
        if len(finded_contacts)==0:
            print('*** Ничего не найдено! ***')
        else:
            print(f'*** Найдено {len(finded_contacts)} вхождение(я/ий) ключа: ***')
            for item in finded_contacts:
                print(item)
    return

def show_book():                        # функция показа содержимого телефонной книги
    global contacts
    open_book()
    print('\nСодержимое телефонного справочника:')
    if len(contacts)==0:
        print('*** Телефонный справочник пуст! ***')
    else:
        print()
        for line in contacts:
            print(line)
    print()
    return

def my_input(desc):             # функция производит запрос поля
    while True:
        try:
            str = input(f'Введите {desc}: ').capitalize().strip()
            if str:
                return str
            else:
                print(f'*** Некорректный ввод! ***')
        except ValueError:
            print(f'*** Некорректный ввод! ***')

def add_contact():                      # функция добавления контакта
    global contacts, change
    my_str = [[], [], [], []]
    my_str[0] = my_input("фамилию")
    my_str[1] = my_input("имя")
    my_str[2] = my_input("отчество")
    my_str[3] = my_input("телефона")
    str = '{:^3}'.format(len(contacts)+1)
    for i in range(len(my_str)):
        str += '{:20}'.format(my_str[i])
    contacts.append(str)
    save_book()
    print(f'*** Контакт добавлен: "{str}"! ***')
    return

def change_contact():                   # функция корректировки контакта
    global contacts
    number = int(input('Для корректировки контакта введите его порядковый номер: '))
    if 1 <= number <= len(contacts):
        choice = int(input('Что будем корректировать? 1 - фамилию; 2 - имя; 3 - отчество; 4 - номер телефона. Ваш выбор: '))
        if 1 <= choice <= 4:
            new_value = input('Введите новое значение: ')
            if choice == 1:
                old_value = contacts[number-1][3:23]
                str = contacts[number-1][0:3] + '{:20}'.format(new_value) + contacts[number-1][23::]
            elif choice == 2:
                old_value = contacts[number - 1][23:43]
                str = contacts[number - 1][0:23] + '{:20}'.format(new_value) + contacts[number - 1][43::]
            elif choice == 3:
                old_value = contacts[number - 1][43:63]
                str = contacts[number - 1][0:43] + '{:20}'.format(new_value) + contacts[number - 1][63::]
            else:
                old_value = contacts[number - 1][63:]
                str = contacts[number - 1][0:63] + '{:20}'.format(new_value)
            if new_value!= old_value:
                contacts[number-1] = str
                print(f'*** Изменения выполнены! Произведена замена "{old_value.strip()}" на "{new_value.strip()}" ***')
            change = True
        else:
            print(f'*** Недопустимый выбор: "{choice}"! ***')
    else:
        print(f'*** Такого порядкового номера ("{number}") - нет! ***')
    for contact in contacts:
        print(contact)
    return

def del_contact():                  # функция удаления контакта
    global contacts
    number = int(input('Для удаления контакта введите его порядковый номер: '))
    if number < 1 or number > len(contacts):
        print(f'*** Недопустимый номер: "{choice}"! ***')
        return
    old = contacts.pop(number-1)
    num_cont = 0
    for i in range(len(contacts)):
        num_cont += 1
        str = '{:^3}'.format(num_cont) + contacts[i][3::]
        contacts[i] = str
    print(f'*** Удалён контакт: "{old.strip()}"')
    save_book()
    return

def clear_book():                   # функция очистки содержимого телефонной книги
    global contacts
    while True:                     # цикл с проверкой выбора
        try:
            choice = int(input("Очистить телефонный справочник? 1 - да; 0 - нет: "))
            if choice==1:
                if int(input('Вы уверены ? 1 - да; иное - нет: '))==1:
                    with open(FILE_BOOK, 'w', encoding='utf-8') as file:  # открываю файл из рабочей директории в режиме записи
                        file.write('')
                        contacts = []
            print('*** Телефонный справочник очищен! ***')
            return
        except ValueError:
            print('*** Некорректный выбор. Попробуйте ещё раз! ***')

contacts = []
change = False
with open(BOOK_MENU, 'r', encoding='utf-8') as file:    # открываю файл с меню из рабочей директории в режиме чтения
    list_menu = file.read()                             # считываю содержимое файла
open_book()
while True:
    choice = choice_menu()
    if choice == len(DICT_MENU):
        if change:
            save_book()
        print("*** До новых встреч! ***")
        break
    x = eval(DICT_MENU[choice]+'()')                    # вывод меню

# Пример применения:
# 1 - показать справочник;   2 - добавить контакт;   3 - найти контакт;   4 - изменить контакт;   5 - удалить контакт;   6 - очистить справочник;   7 - сохранить справочник;   8 - выход
# Выберите пункт меню: 1

# Содержимое телефонного справочника:

#  1 Иванов              Игорь               Павлович            9276843597          
#  ...
#  6 Чурсина             Ирина               Владимировна        91786245841         

# 1 - показать справочник;   2 - добавить контакт;   3 - найти контакт;   4 - изменить контакт;   5 - удалить контакт;   6 - очистить справочник;   7 - сохранить справочник;   8 - выход
# Выберите пункт меню: 6
# Очистить телефонный справочник? 1 - да; 0 - нет: 1
# Вы уверены ? 1 - да; иное - нет: 1
# *** Телефонный справочник очищен! ***
# 1 - показать справочник;   2 - добавить контакт;   3 - найти контакт;   4 - изменить контакт;   5 - удалить контакт;   6 - очистить справочник;   7 - сохранить справочник;   8 - выход
# Выберите пункт меню: 8
# *** До новых встреч! ***