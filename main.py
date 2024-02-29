import os
import telebot
from UI import markups
from Scraping.get_rozklad import get_rozklad_file
from UI.get_key_by_index import get_nth_key
from get_numerator_denominator_week.get_numerator_denominator_week import get_current_week_type

bot = telebot.TeleBot(token=os.getenv('TELEGRAM_API_TOKEN'))


# COMMAND START
@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Привіт, {message.from_user.first_name},'
                                      f' це офіційний телеграм бот <strong><em>Географічного факультету'
                                      f' Київського Національного Університету імені Тараса Шевченка.</em></strong>',
                     parse_mode='HTML', reply_markup=markups.main_markup())


# COMMAND MENU
@bot.message_handler(commands=['menu'])
def go_to_menu(message):
    bot.send_message(message.chat.id, text='Головне меню', reply_markup=markups.main_markup())


# COMMAND NUMERATOR
@bot.message_handler(commands=['numerator'])
def get_numerator(message):
    bot.send_message(message.chat.id, text=get_current_week_type(), reply_markup=markups.main_markup())


# COMMAND GET ROZKLAD
@bot.message_handler(commands=['rozklad'])
def get_rozklad(message):
    bot.send_message(message.chat.id, text='Оберіть курс', reply_markup=markups.select_course_markup())


@bot.message_handler(commands=['send_pdf'])
def send_rozklad_pdf(message, url=''):
    get_rozklad_file(url)
    with open("./File_system/rozklad.pdf", 'rb') as file:
        bot.send_document(message.chat.id, document=file)
    os.remove("./File_system/rozklad.pdf")
    go_to_menu(message)


@bot.message_handler(commands=['departments'])
def send_departments(message):
    bot.send_message(message.chat.id, text='Кафедри факультету:', reply_markup=markups.select_department_markup())


@bot.message_handler(commands=['departments_staff'])
def send_departments_staff(message, department_index):
    department_name = markups.departments[department_index].name
    bot.send_message(message.chat.id, text=department_name, reply_markup=markups.show_staff_markup(department_index))


# CALLBACKS
@bot.callback_query_handler(func=lambda call: True)
def numerator_callback(call):

    # NUMERATOR / GET WEEK TYPE CALLBACK
    if call.data == "numerator_callback":
        get_numerator(call.message)

    # GET ROZKLAD CALLBACK
    if call.data == "get_rozklad_callback":
        get_rozklad(call.message)

    # КУРС ОБРАНО CALLBACK, ВІДПРАВИТИ РОКЗЛАД ПДФ
    if call.data.__contains__('selected'):
        selected_course_index = call.data[-1]
        course_key = get_nth_key(markups.rozklad, int(selected_course_index))
        rozklad_link = markups.rozklad[course_key]
        send_rozklad_pdf(call.message, rozklad_link)

    # GO TO MENU CALLBACK
    if call.data == 'go_to_menu_callback':
        go_to_menu(call.message)

    # SELECT DEPARTMENT CALLBACK
    if call.data == 'select_department_callback':
        send_departments(call.message)

    # SEND STAFF CALLBACK
    if call.data.__contains__('particular_department'):
        department_index = int(call.data[-1])
        send_departments_staff(call.message, department_index)



bot.infinity_polling(timeout=5000)
