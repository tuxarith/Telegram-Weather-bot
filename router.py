#========================================================================================================================================================
                                     #Packages
import asyncio
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import message, Message, FSInputFile
from func import main_reply_keyboard, main_inline_keyboard
import os
from aiogram.fsm.state import State
from aiogram.fsm.context import FSMContext
from class1 import Weather
import aiohttp
from dotenv import load_dotenv
#========================================================================================================================================================


load_dotenv("apiweather.env")
apiweather_token = os.getenv("API")

router = Router()

#========================================================================================================================================================
                             #Commands

@router.message(Command("start"))
async def start(message: Message):
    photo = FSInputFile('photo/j24.jpg')

    await message.answer_photo(photo=photo, reply_markup=main_reply_keyboard())

    await message.answer(f'Привет {message.from_user.first_name}! Я бот-погодник ', reply_markup=main_inline_keyboard() )


@router.message(Command("weather"))
async def weather(message: Message):
    args = message.text.split(maxsplit=1)

    if len(args) < 2:
        await message.answer("Укажите город: /weather Москва")
        return

    city = args[1]

    url = (
        f"http://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={apiweather_token}&units=metric")


    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:

            if res.status != 200:
                await message.answer("Город указан неверно!")
                return

            data = await res.json()

    temp = data["main"]["temp"]

    await message.answer(f"Сейчас погода в {city}: {temp}°C")


    if temp >= 18:
        await message.answer("Тепло ☀️")

    elif temp >= 0:
        await message.answer("Прохладно 🍂")

    else:
        await message.answer("Холодно ❄️")


@router.message(Command("info"))
async def info(message: Message):
    await message.answer("Этот бот был сделан человеком tuxarchx, данный бот предоставляет получение погоды по городу")

@router.message(Command("commands"))
async def commands(message: Message):
    photo = FSInputFile('photo/cat.jpg')
    await message.answer_photo(photo=photo,caption='------Команды-------\n\n'
                         f'/weather "Город" - Получить погоду какого-то города\n'
                         f'/info - информация о боте\n'
                         f'/commands - все команды')
#========================================================================================================================================================




#========================================================================================================================================================
                        #Callback
@router.callback_query(lambda c: c.data == 'commands')
async def get_callback_commands(callback):
    photo = FSInputFile('photo/cat.jpg')
    await callback.message.answer_photo(photo=photo, caption=f'------Команды-------\n\n'
                         f'/weather "Город" - Получить погоду какого-то города\n'
                         f'/info - информация о боте\n'
                         f'/commands - все команды')
    await callback.answer()

@router.callback_query(lambda c: c.data == 'info')
async def get_callback_info(callback):
    photo = FSInputFile("photo/#Cuteness.jpg")

    await callback.message.answer_photo(photo=photo, caption="Этот бот был сделан человеком tuxarchx, данный бот предоставляет получение погоды по городу")

    await callback.answer()
#========================================================================================================================================================



#========================================================================================================================================================
                                        #F

@router.message(F.text == "Узнать погоду")
async def fsm_weather(message: Message, state: FSMContext):
    await state.set_state(Weather.get_weather)
    await message.answer("Отправьте название Города!")

@router.message(Weather.get_weather)
async def get_weather(message: Message, state: FSMContext):
    args = message.text.split(maxsplit=1)



    city = args[0]

    url = (
        f"http://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={apiweather_token}&units=metric")


    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:

            if res.status != 200:
                await message.answer("Город указан неверно!")
                return

            data = await res.json()

    temp = data["main"]["temp"]

    await message.answer(f"Сейчас погода в {city}: {temp}°C")


    if temp >= 18:
        await message.answer("Тепло ☀️")

    elif temp >= 0:
        await message.answer("Прохладно 🍂")

    else:
        await message.answer("Холодно ❄️")

    await state.clear()




#========================================================================================================================================================





# :)