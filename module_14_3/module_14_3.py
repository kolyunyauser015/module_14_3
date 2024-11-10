from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import description_products
import confid_info
import keyboards

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.",
                         reply_markup=keyboards.start_kb)


@dp.message_handler(text="Рассчитать")
async def main_menu(message):
    await message.answer("Выберите опцию", reply_markup=keyboards.calories_kb)


@dp.callback_query_handler(text="formulas")
async def get_formulas(call):
    await call.message.answer("10*вес(кг) + 6.25 * рост(см) + 5 * возраст(г) + 5")
    await call.message.answer("Выберите опцию", reply_markup=keyboards.calories_kb)
    await call.answer()


@dp.callback_query_handler(text="calories")
async def set_age(call):
    await call.message.answer("Введите свой возраст:")
    await call.answer()
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(first=message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(second=message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_colories(message, state):
    await state.update_data(third=message.text)
    data = await state.get_data()
    calc_colories = 10 * int(data['first']) + 6.25 * int(data['second']) + 5 * int(data['third']) + 5
    await message.answer(f"Ваша норма калорий: {calc_colories}")
    await state.finish()


@dp.message_handler(text="Купить")
async def get_buying_list(message):
    for number in range(1, 5):
        await message.answer(f"Название: Product{number} | Описание: " +
                             description_products.text_product[f'product_{number}'] +
                             f"| Цена: {number * 100}")
        with open(f'module_14_3/product_photo/p{number}.jpg', 'rb') as ph:
            await message.answer_photo(ph)
    await message.answer("Выберите продукт для покупки", reply_markup=keyboards.catalog_kb)


@dp.callback_query_handler(text="product_buying")
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
