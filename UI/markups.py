from telebot import types

from Model.Department import Department
from Scraping.get_departments import get_departments
from Scraping.get_rozklad import get_rozklad

rozklad: dict = get_rozklad()
departments: [Department] = get_departments()


def main_menu_button(markup):
    markup.add(types.InlineKeyboardButton('Головне меню', callback_data='go_to_menu_callback'))


def main_markup():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Отримати розклад', callback_data='get_rozklad_callback'))
    markup.row(types.InlineKeyboardButton('Чисельник чи знаменник?', callback_data='numerator_callback'),
               types.InlineKeyboardButton('Кафедри факультету', callback_data='select_department_callback'))

    return markup


def select_course_markup():
    markup = types.InlineKeyboardMarkup()
    index = 0
    for course, link in rozklad.items():
        button = types.InlineKeyboardButton(text=course, callback_data=f'selected_course_{index}')
        markup.add(button)
        index += 1

    main_menu_button(markup)
    return markup


def select_department_markup():
    markup = types.InlineKeyboardMarkup()
    index = 0
    for department in departments:
        button = types.InlineKeyboardButton(text=department.name, callback_data=f'particular_department_{index}')
        markup.add(button)
        index += 1

    main_menu_button(markup)
    return markup


def show_staff_markup(department_index):
    markup = types.InlineKeyboardMarkup()
    for staff in departments[department_index].get_staff:
        button = types.InlineKeyboardButton(text=staff.name, callback_data='staff_callback')
        markup.add(button)

    main_menu_button(markup)
    return markup