# Задача 38. Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных.
# С модулями.
# Обучающийся: Шитов Олег Владимирович, разработка 4544, будни, утро, дата сдачи - 30.05.2023 (до 10:00 мск)

"""
        Главный модуль
"""

FILE_BOOK = 'phone_book.txt'                                      # файл с телефонным справочником
LIST_MENU =  '1 - показать справочник;  2 - добавить контакт;     3 - найти контакт;        4 - изменить контакт;   '
LIST_MENU += '5 - удалить контакт;      6 - очистить справочник;  7 - сохранить справочник; 8 - выход'
DICT_MENU = { 1:'show_book',            2:'add_contact',          3:'find_contact',         4:'change_contact',\
              5:'del_contact',          6:'clear_book',           7:'save_book', 8:'exit_book' }  # набор функций

from controller import start

if __name__ == '__main__':
    print("\n*** ТЕЛЕФОННЫЙ СПРАВОЧНИК ***")
    start(FILE_BOOK, LIST_MENU, DICT_MENU)                              # вызов функции с меню
    print("*** До новых встреч! ***")