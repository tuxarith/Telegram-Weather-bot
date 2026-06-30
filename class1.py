import asyncio
from aiogram.fsm.state import State, StatesGroup

class Weather(StatesGroup):
    get_weather = State()

