from aiogram.dispatcher.filters.state import StatesGroup, State


class UserState(StatesGroup):
    get_course = State()
    get_photo = State()
    get_name = State()
    get_number = State()
