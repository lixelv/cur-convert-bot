cnf.py:
```py
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

```
cur_parse.py:
```py
import requests

data = requests.get('https://www.cbr-xml-daily.ru/latest.js').json()

data = data["rates"]
data.update({'RUB': 1.0})

val_lst = data.keys()
print(val_lst)

cur_from = input('Выберете валюту, из которой вы конвертируете: ').upper()
val_from = float(input('Введите кол-во валюты: '))
cur_to = input('Выберете валюту, в которую конвертируете: ').upper()

result = (data[cur_to]/data[cur_from])*val_from

print(f'{result:.6g} {cur_to}')

```
db.py:
```py
import sqlite3


class DB:
    def __init__(self, db_name):
        self.connect = sqlite3.connect(db_name)
        self.cursor = self.connect.cursor()
        self.do("""
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY,
    name TEXT,
    state INTEGER DEFAULT 0,
    data TEXT,
    date DATETIME DEFAULT CURRENT_TIMESTAMP
    );""")

    def do(self, query: str, values=()) -> None:
        self.cursor.execute(query.replace('%s', '?'), values)
        self.connect.commit()

    def read(self, query: str, values=(), one=False) -> tuple:
        self.cursor.execute(query.replace('%s', '?'), values)
        return self.cursor.fetchall() if not one else self.cursor.fetchone()

    def user_exists(self, user_id: int) -> bool:
        return bool(self.read('SELECT id FROM user WHERE id = ?;', (user_id,)))

    def add_user(self, user_id: int, user_name: str):
        self.do('INSERT INTO user(id, name) VALUES(?, ?);', (user_id, user_name))

    def set_state(self, user_id: int, state: int) -> None:
        self.do('UPDATE user SET state = ? WHERE id = ?;', (state, user_id))

    def state(self, user_id: int) -> bool:
        return self.read('SELECT state FROM user WHERE id = ?;', (user_id,), one=True)[0]

    def set_data(self, user_id: int, data: str) -> None:
        self.do('UPDATE user SET data = ? WHERE id = ?;', (data, user_id))

    def get_data(self, user_id: int) -> str:
        return self.read('SELECT data FROM user WHERE id = ?;', (user_id,), one=True)[0]


```
main.py:
```py
import requests
from aiogram import executor
from cnf import *


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if not sql.user_exists(message.from_user.id):
        sql.add_user(message.from_user.id, message.from_user.username)

    await message.answer(start_, parse_mode='MarkdownV2')

@dp.message_handler(commands=['c', 'cur', 'currency'])
async def cur(message: types.Message):
    await message.answer('Выберете *валюту*, из которой вы конвертируете: ', reply_markup=cur_(f_t='_'), parse_mode='MarkdownV2')
    sql.set_state(message.from_user.id, 1)

@dp.callback_query_handler(lambda call: sql.state(call.from_user.id) == 1)
async def cur_from(call: types.CallbackQuery):
    sql.set_data(call.from_user.id, call.data.replace('_', ''))
    await call.message.edit_text('Выберете *валюту*, в которую конвертируете: ', reply_markup=cur_(), parse_mode='MarkdownV2')
    # await call.message.delete()
    sql.set_state(call.from_user.id, 2)

@dp.callback_query_handler(lambda call: sql.state(call.from_user.id) == 2)
async def cur_to(call: types.CallbackQuery):
    data = sql.get_data(call.from_user.id)
    sql.set_data(call.from_user.id, f'{data}_{call.data}')
    await call.message.edit_text(f'Введите кол\-во *валюты:*', parse_mode='MarkdownV2')
    # await call.message.delete()
    sql.set_state(call.from_user.id, 3)

@dp.message_handler(lambda message: sql.state(message.from_user.id) == 3)
async def get_cur(message: types.Message):
    try:
        message.text = float(message.text.split(' ')[0].replace(' ', '').replace(',', '.'))
    except Exception as e:
        print(e)
        await message.answer('Некорректный ввод, попробуйте еще раз')
        return None

    data = requests.get('https://www.cbr-xml-daily.ru/latest.js').json()
    data = data["rates"]
    data.update({'RUB': 1.0})
    sub_data = sql.get_data(message.from_user.id)
    sub_data = sub_data.split('_')
    result = (data[sub_data[1]] / data[sub_data[0]]) * message.text
    await message.answer(f'`{message.text}` {sub_data[0]} \= `{result:.6g}` {sub_data[1]}', parse_mode='MarkdownV2')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

```
