from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

payments_kb = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton("1 STANDART",
                         callback_data="1 STANDART 4 277 000 очирилган 3 277 000"),
    InlineKeyboardButton("2 PREMIUM",
                         callback_data="2 PREMIUM  4 977 000 очирилган 3 777 000"),
    InlineKeyboardButton("3 VIP",
                         callback_data="3 VIP  50 000 000 очирилган 40 000 000"))
