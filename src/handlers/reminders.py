from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

# напоминание через 10 мин, если не запросил урок
async def remind_if_lesson_did_not_send():
 pass

# цикл напоминаний, если урок был выслан
async def remind_to_watch_this():
 pass

# Если пользователь не реагирует и на предыдущее напоминание в течении 3 часов
async def choose_time_to_remind(message: types.Message):

    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="На связи Бебрис",
        callback_data="step1")
        # ,
        # types.InlineKeyboardButton(
        # text="Дальше",
        # callback_data="step1_2")
    )
    await message.answer("<b>Ты точно хочешь выучить английский?🤔 Не люблю я уговаривать. Ведь менять жизнь - это должен быть только твой выбор! Но мне так хочется, чтобы ты не забыл про это видео, что готов еще раз о нем напомнить, если ты не можешь посмотреть его сейчас.",
        reply_markup=builder.as_markup())

# 1. нажал что подписался, но не нажад перейти к уроку, статут did_not_send
# черех 10 минут напоминание

# нажал на кнопку 1 урок, поменяли статус на отправлено
# через


# @router.message()
# async def send_video(call: CallbackQuery):
#     db.set_status(user_id=call.from_user.id, status='start_watch')
#     await bot.send_video('path_to_video')
#     await ascincio.time.sleep(900)
#     if db.get_status(user_id=call.from_user.id) == 'start_watch':
#         awawit call.answer(text='Не забудь посмотреть видео)')