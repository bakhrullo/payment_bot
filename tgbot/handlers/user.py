from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from tgbot.config import Config
from tgbot.keyboards.inline import payments_kb
from tgbot.keyboards.reply import contact_btn, remove_btn
from tgbot.misc.states import UserState


async def user_start(m: Message):
    await m.answer("Assalomu alaykum 😊\nSiz Ilhom Begimqulovning rasmiy to'lov botiga tashrif buyurdingiz!"
                   "\nQaysi kursizmizga yozilmoqchisiz ?\n"
                   "1 STANDART 4 277 000 очирилган 3 277 000\n"
                   "2 PREMIUM  4 977 000 очирилган 3 777 000\n"
                   "3 VIP  50 000 000 очирилган 40 000 000", reply_markup=payments_kb)
    await UserState.get_course.set()


async def get_course(c: CallbackQuery, state: FSMContext):
    await state.update_data(course=c.data)
    await c.message.edit_text("Tolov uchun <code>8600 4545 4545 4545</code> Ilhom Begımqulov\n"
                              "Iltimos, to'lov qilib bo'lganingizdan keyin screenshotni shu yerga jo'nating! 😇")
    await UserState.next()


async def get_photo(m: Message, state: FSMContext):
    await state.update_data(photo=m.photo[-1].file_id)
    await m.answer("Iltimos, ismingizni kiriting!")
    await UserState.next()


async def get_name(m: Message, state: FSMContext):
    await state.update_data(name=m.text)
    await m.answer("☎️ Iltimos, telefon nomeringizni kiriting yoki pastdagi 'Kontaktni ulashish' tugmachasini bosing!",
                   reply_markup=contact_btn)
    await UserState.next()


async def get_number(m: Message, state: FSMContext, config: Config):
    await m.answer("Operatorlarimiz tez orada sizga aloqaga chiqishadi! 😊️", reply_markup=remove_btn)
    phone = m.contact.phone_number if m.content_type == "contact" else m.text
    data = await state.get_data()
    await m.bot.send_photo(config.tg_bot.group_id, data['photo'],
                           caption=f"👨 Ism: {data['name']}\n📱 Raqam: {phone}\n💸 Kurs: {data['course']}")


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*", chat_type="private")
    dp.register_callback_query_handler(get_course, state=UserState.get_course, chat_type="private")
    dp.register_message_handler(get_photo, state=UserState.get_photo, content_types=['photo'], chat_type="private")
    dp.register_message_handler(get_name, state=UserState.get_name, chat_type="private")
    dp.register_message_handler(get_number, state=UserState.get_number, content_types=['text', 'contact'],
                                chat_type="private")
