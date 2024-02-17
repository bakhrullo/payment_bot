from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

payments_kb = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton("1 STANDART",
                         callback_data="1 STANDART <s>4 277 000</s>  3 277 000"),
    InlineKeyboardButton("2 PREMIUM",
                         callback_data="2 PREMIUM  <s>4 977 000</s>  3 777 000"),
    InlineKeyboardButton("3 VIP",
                         callback_data="3 VIP  <s>50 000 000</s>  40 000 000"))
