import requests
from time import sleep
from aiogram import executor
from cnf import *
import signal
import os

def signal_handler(sig, frame):
    print("Выход...")
    os.kill(os.getpid(), signal.SIGTERM)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if not sql.user_exists(message.from_user.id):
        sql.add_user(message.from_user.id, message.from_user.username)

    await message.answer(start_, parse_mode='MarkdownV2')

@dp.message_handler(commands=['cr', 'c-r', 'c_r', 'currate', 'cur-rate', 'cur_rate'])
async def cur_rate(message: types.Message):
    await message.answer('Выберете абревиатеру *валюты*:', reply_markup=cur(), parse_mode='MarkdownV2')
    sql.set_state(message.from_user.id, 4)

@dp.message_handler(commands=['c', 'cur', 'currency'])
async def _cur_(message: types.Message):
    await message.answer('Выберете абревиатеру *валюты*, из которой вы конвертируете:', reply_markup=cur(f_t='_'), parse_mode='MarkdownV2')
    sql.set_state(message.from_user.id, 1)
    
@dp.message_handler(commands=['get_abbreviations', 'get_abr'])
async def get_abbreviations(message: types.Message):
    await message.answer('Выберете абревиатеру *валюты*, название которой вы хотите получить:', reply_markup=cur(f_t='_'), parse_mode='MarkdownV2')
    sql.set_state(message.from_user.id, 5)
    
@dp.message_handler(commands=['get_full_abbreviations', 'get_full_abr'])
async def get_full_abbreviations(message: types.Message):
    msg = ''
    for cur in cur_dict.keys():
        msg += f"`{cur}` - `{cur_dict[cur]}`"

@dp.callback_query_handler(lambda call: sql.state(call.from_user.id) == 1)
async def cur_from(call: types.CallbackQuery):
    sql.set_data(call.from_user.id, call.data.replace('_', ''))
    await call.message.edit_text('Выберете абревиатеру *валюты*, в которую конвертируете:', reply_markup=cur(), parse_mode='MarkdownV2')
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
    sql.set_state(message.from_user.id, 0)

@dp.callback_query_handler(lambda call: sql.state(call.from_user.id) == 4)
async def get_cur_rate(call: types.CallbackQuery):
    data = requests.get('https://www.cbr-xml-daily.ru/latest.js').json()
    data = data["rates"]
    data.update({'RUB': 1.0})
    result = (1 / data[call.data])
    await call.message.edit_text(f'`1` {call.data} \= `{result:.6g}` RUB', parse_mode='MarkdownV2')
            
@dp.callback_query_handler(lambda call: sql.state(call.from_user.id) == 5)
async def call_get_abbreviations(call: types.CallbackQuery):
    currency = call.data
    await call.message.edit_text(f'`{currency}` - `{cur_dict[currency]}`', parse_mode='MarkdownV2')
    sql.set_state(call.from_user.id, 0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    while True:
        try:
            executor.start_polling(dp, skip_updates=True)
            
        except Exception as e:
            print(e)
            sleep(240)