# Задача 38. Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных.
#
# Обучающийся: Шитов Олег Владимирович, разработка 4544, будни, утро, дата сдачи - 30.05.2023 (до 10:00 мск)

"""
        Управляющий модуль
"""
from view import choice_menu
from model import open_book, save_book
import model

def start(FILE_BOOK, LIST_MENU, DICT_MENU):
    while True:
        choice = choice_menu(LIST_MENU, DICT_MENU)                    # вызов функции с меню
        if choice == len(DICT_MENU):            # если выход
            if int(input('Выход? 1 - да; иное - нет: ')) == 1:
                return
        contacts = open_book(FILE_BOOK)                               # считываю телефонный справочник
        contacts = eval('model.'+DICT_MENU[choice]+'(contacts)')      # команда вызывает функцию по пункту меню
        save_book(FILE_BOOK,contacts)                                 # записываю телефонный справочник
