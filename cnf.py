from aiogram import Bot, Dispatcher, types
from envparse import env
from db import DB

sql = DB('db.db')

env.read_envfile('.env')

token = env('TELEGRAM')

bot = Bot(token)
dp = Dispatcher(bot)

def inline(lst: list, width: int = 3, f_t: str = '') -> types.InlineKeyboardMarkup:
    kb = types.InlineKeyboardMarkup(row_width=width, width=1200)
    button_lst = []
    for item in lst:
        button_lst.append(types.InlineKeyboardButton(text=item, callback_data=f_t+item))

    kb.add(*button_lst)

    return kb

def cur(f_t: str = '') -> types.InlineKeyboardMarkup:
    return inline(['RUB', 'USD', 'EUR', 'UAH', 'BYN', 'KZT', 'GBP', 'CNY', 'CHF', 'JPY', 'CAD', 'AUD', 'PLN', 'INR', 'SEK', 'TRY', 'NOK', 'DKK', 'CZK', 'AZN', 'AMD', 'KGS', 'UZS', 'TJS', 'MDL', 'BRL', 'SGD', 'HKD', 'EGP', 'ZAR', 'BGN', 'QAR', 'AED', 'THB', 'VND', 'GEL', 'HUF', 'IDR', 'NZD', 'KRW', 'TMT', 'XDR', 'RSD', 'RON'], f_t=f_t)

cur_dict = {'RUB': 'Российский рубль', 'USD': 'Доллар США', 'EUR': 'евро', 'UAH': 'Украинская гривна', 'BYN': 'Белорусский рубль', 'KZT': 'Казахский тенге', 'GBP': 'Британский фунт', 'CNY': 'Китайская йена', 'CHF': 'Швейцарский франк', 'JPY': 'Японская иена', 'CAD': 'Канадский доллар', 'AUD': 'Австралийский доллар', 'PLN': 'Польский злотый', 'INR': 'Индийская рупия', 'SEK': 'Шведская крона', 'TRY': 'Турецкая лира', 'NOK': 'Норвежская крона', 'DKK': 'Датская крона', 'CZK': 'Чешская крона', 'AZN': 'Азербайджанский манат', 'AMD': 'Армянский драм', 'KGS': 'Киргизский сом', 'UZS': 'Узбекский сум', 'TJS': 'Таджикский сомони', 'MDL': 'Молдавский лей', 'BRL': 'Бразильский реал', 'SGD': 'Сингапурский доллар', 'HKD': 'Гонконгский доллар', 'EGP': 'Египетский фунт', 'ZAR': 'Южноафриканский ранд', 'BGN': 'Болгарский лев', 'QAR': 'Катарский риал', 'AED': 'Дирхам Объединенных Арабских Эмиратов', 'THB': 'Тайский бат', 'VND': 'Вьетнамский донг', 'GEL': 'Грузинский лари', 'HUF': 'Венгерский форинт', 'IDR': 'Индонезийская рупия', 'NZD': 'Новозеландский доллар', 'KRW': 'Южнокорейская вона', 'TMT': 'Туркменский манат', 'XDR': 'Специальные права заимствования', 'RSD': 'Cербский динар', 'RON': 'Новый румынский лей'}
start_ = "Привет\! Я был создан чтобы конвертировать валюты\,\nИспользуй команду */currency* чтобы конвертировать валюту\nИспользуй команду */cur\_rate* чтобы узнать курс валюты\nИспользуй команду */get\_abr* чтобы узнать абревиатуру валюты\nИспользуй команду */get\_full\_abr* чтобы получить список абревиатур"
