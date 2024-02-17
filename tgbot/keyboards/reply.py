from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

contact_btn = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
    KeyboardButton("Kontaktni ulashish 📱", request_contact=True))

remove_btn = ReplyKeyboardRemove()
