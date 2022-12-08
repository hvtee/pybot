from config import *
import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup as BS4

bot = telebot.TeleBot(TOKEN, parse_mode=None)
URL_weather = 'https://world-weather.ru/pogoda/belarus/minsk/'


def get_weather(url, time):
    req_weather = requests.get(url)
    soup = BS4(req_weather.text, 'html.parser')
    if time == 'now':
        weather_time = []
        weather_time.append(soup.find('div', class_='pane').find('td', class_='weather-day').text)
        weather_time.append(
            soup.find('div', class_='pane').find('td', class_='weather-day').find_next('td', class_='weather-day').text)
        weather_time.append(
            soup.find('div', class_='pane').find('td', class_='weather-day').find_next('td',
                                                                                       class_='weather-day').find_next(
                'td', class_='weather-day').text)
        weather_time.append(
            soup.find('div', class_='pane').find('td', class_='weather-day').find_next('td',
                                                                                       class_='weather-day').find_next(
                'td', class_='weather-day').find_next('td', class_='weather-day').text)

        weather_temp = []
        weather_temp.append(soup.find('div', class_='pane').find('td', class_='weather-temperature').find('span').text)
        weather_temp.append(
            soup.find('div', class_='pane').find('td', class_='weather-temperature').find('span').find_next('td',
                                                                                                            class_='weather-temperature').text)
        weather_temp.append(
            soup.find('div', class_='pane').find('td', class_='weather-temperature').find('span').find_next('td',
                                                                                                            class_='weather-temperature').find_next(
                'td', class_='weather-temperature').text)
        weather_temp.append(
            soup.find('div', class_='pane').find('td', class_='weather-temperature').find('span').find_next('td',
                                                                                                            class_='weather-temperature').find_next(
                'td', class_='weather-temperature').find_next('td', class_='weather-temperature').text)

        return [weather_time, weather_temp]
    elif time == 'today':
        weather_temp_day = soup.find('div', class_='day-temperature').text
        weather_temp_night = soup.find('div', class_='night-temperature').text
        weather_month = soup.find('div', class_='month').text
        weather_date = soup.find('div', class_='numbers-month').text
        return [weather_temp_day, weather_temp_night, weather_month, weather_date]
    elif time == 'tomorrow':
        weather_temp_day = soup.find('div', class_='day-temperature').find_next('div', class_='day-temperature').text
        weather_temp_night = soup.find('div', class_='night-temperature').find_next('div',
                                                                                    class_='night-temperature').text
        weather_month = soup.find('div', class_='month').find_next('div', class_='month').text
        weather_date = soup.find('div', class_='numbers-month').find_next('div', class_='numbers-month').text
        return [weather_temp_day, weather_temp_night, weather_month, weather_date]


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"Howdy, how are you doing, {message.chat.first_name}")
    bot.send_message(message.chat.id, '/start\n/main')


@bot.message_handler(commands=['main'])
def main(message):
    inline_main = types.InlineKeyboardMarkup()
    main_get_info = types.InlineKeyboardButton(text='Get info', callback_data='get_info')
    main_get_weather = types.InlineKeyboardButton(text='Get weather', callback_data='get_weather')
    main_test_buttons = types.InlineKeyboardButton(text='Test buttons', callback_data='test_buttons')

    inline_main.add(main_get_info, main_get_weather, main_test_buttons)
    bot.send_message(message.chat.id, 'Choose option: ', reply_markup=inline_main)


@bot.callback_query_handler(func=lambda call: True)
def get_main_answer(call):
    if call.data == 'get_info':
        inline_get_info = types.InlineKeyboardMarkup()
        get_id = types.InlineKeyboardButton(text='ID', callback_data='id')
        get_first_name = types.InlineKeyboardButton(text='First name', callback_data='first_name')
        get_last_name = types.InlineKeyboardButton(text='Last name', callback_data='last_name')
        get_user_name = types.InlineKeyboardButton(text='User name', callback_data='user_name')

        inline_get_info.add(get_first_name, get_last_name, get_user_name, get_id)
        bot.send_message(call.message.chat.id, 'Choose info type: ', reply_markup=inline_get_info)
    elif call.data == 'get_weather':
        inline_get_weather = types.InlineKeyboardMarkup()
        get_weather_now = types.InlineKeyboardButton(text='Now', callback_data='weather_now')
        get_weather_today = types.InlineKeyboardButton(text='Today', callback_data='weather_today')
        get_weather_tomorrow = types.InlineKeyboardButton(text='Tomorrow', callback_data='weather_tomorrow')

        inline_get_weather.add(get_weather_now, get_weather_today, get_weather_tomorrow)
        bot.send_message(call.message.chat.id, 'Choose time: ', reply_markup=inline_get_weather)
    elif call.data == 'test_buttons':
        inline_test_func = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton(text='Button1', callback_data='1')
        item2 = types.InlineKeyboardButton(text='Button2', callback_data='2')

        inline_test_func.add(item1, item2)
        bot.send_message(call.message.chat.id, 'Choose button: ', reply_markup=inline_test_func)
    elif call.data == 'id':
        bot.send_message(call.message.chat.id, f'Your id is: {call.message.chat.id}')
    elif call.data == 'first_name':
        bot.send_message(call.message.chat.id, f'Your first name is: {call.message.chat.first_name}')
    elif call.data == 'last_name':
        bot.send_message(call.message.chat.id, f'Your last name is: {call.message.chat.last_name}')
    elif call.data == 'user_name':
        bot.send_message(call.message.chat.id, f'Your user name is: {call.message.chat.username}')
    elif call.data == '1':
        bot.send_message(call.message.chat.id, 'You clicked Button1')
    elif call.data == '2':
        bot.send_message(call.message.chat.id, 'You clicked Button2')
    elif call.data == 'weather_now':
        weather = get_weather(URL_weather, 'now')
        bot.send_message(call.message.chat.id, f'Time: {weather[0][0]}, temperature: {weather[1][0]}')
        bot.send_message(call.message.chat.id, f'Time: {weather[0][1]}, temperature: {weather[1][1]}')
        bot.send_message(call.message.chat.id, f'Time: {weather[0][2]}, temperature: {weather[1][2]}')
        bot.send_message(call.message.chat.id, f'Time: {weather[0][3]}, temperature: {weather[1][3]}')
    elif call.data == 'weather_today':
        weather = get_weather(URL_weather, 'today')
        bot.send_message(call.message.chat.id,
                         f'{weather[3]} {weather[2]}: day temperature is {weather[0]}, night temperature is {weather[1]}')
    elif call.data == 'weather_tomorrow':
        weather = get_weather(URL_weather, 'tomorrow')
        bot.send_message(call.message.chat.id,
                         f'{weather[3]} {weather[2]}: day temperature is {weather[0]}, night temperature is {weather[1]}')


@bot.message_handler(content_types=['text'])
def replyes(message):
    if message.text.lower() in ['привет', 'здравствуй', 'дарова', 'хэй']:
        bot.reply_to(message, f'И тебе привет, {message.chat.first_name}!')
    elif message.text.lower() in ['как дела?', 'как дела', 'ты как', 'ты как?', 'что как', 'что как?']:
        bot.reply_to(message, f'Хорошо, работаю вот!')
        bot.reply_to(message, f'А у тебя как дела?')
    elif message.text.lower() in ['хорошо', 'неплохо', 'нормально', 'не очень', 'плохо']:
        bot.reply_to(message, f'ты молодец, {message.chat.first_name}, помни об этом!')


print('Bot started')
bot.infinity_polling(none_stop=True)
