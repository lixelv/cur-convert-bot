from aiogram import Bot, Dispatcher, types
from envparse import env
from db import DB

sql = DB('db.db')

env.read_envfile('.env')

token = env('TELEGRAM')

bot = Bot(token)
dp = Dispatcher(bot)

def inline(lst: list, width: int = 6, f_t: str = '') -> types.InlineKeyboardMarkup:
    kb = types.InlineKeyboardMarkup(row_width=width, width=1200)
    button_lst = []
    for item in lst:
        button_lst.append(types.InlineKeyboardButton(text=item, callback_data=f_t+item))

    kb.add(*button_lst)

    return kb

def cur_(f_t: str = '') -> types.InlineKeyboardMarkup:
    return inline(['RUB', 'USD', 'EUR', 'UAH', 'BYN', 'KZT', 'GBP', 'CNY', 'CHF', 'JPY', 'CAD', 'AUD', 'PLN', 'INR', 'SEK', 'TRY', 'NOK', 'DKK', 'CZK', 'AZN', 'AMD', 'KGS', 'UZS', 'TJS', 'MDL', 'BRL', 'SGD', 'HKD', 'EGP', 'ZAR', 'BGN', 'QAR', 'AED', 'THB', 'VND', 'GEL', 'HUF', 'IDR', 'NZD', 'KRW', 'TMT', 'XDR', 'RSD', 'RON'], f_t=f_t)

start_ = "Привет\! Я был создан чтобы конвертировать валюты\," \
         "\nИспользуй команду */currency* чтобы конвертировать валюту"
