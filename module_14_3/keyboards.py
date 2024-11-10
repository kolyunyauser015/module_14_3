from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


start_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='Рассчитать'),
               KeyboardButton(text='Информация')]],
    resize_keyboard=True)
start_kb.add(KeyboardButton(text='Купить'))


calories_kb = InlineKeyboardMarkup(resize_keyboard=True)
button_1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_2 = InlineKeyboardButton(text='Формулы расчета', callback_data='formulas')
calories_kb.add(button_1)
calories_kb.insert(button_2)


catalog_kb = InlineKeyboardMarkup(resize_keyboard=True, row_width=4)
button_product_1 = InlineKeyboardButton(text='Product1', callback_data="product_buying")
button_product_2 = InlineKeyboardButton(text='Product2', callback_data="product_buying")
button_product_3 = InlineKeyboardButton(text='Product3', callback_data="product_buying")
button_product_4 = InlineKeyboardButton(text='Product4', callback_data="product_buying")
catalog_kb.add(button_product_1)
catalog_kb.insert(button_product_2)
catalog_kb.insert(button_product_3)
catalog_kb.insert(button_product_4)
