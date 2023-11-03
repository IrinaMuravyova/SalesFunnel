import time
from aiogram import types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from loader import db, router_reminders
from aiogram.types import URLInputFile
from config import video_lessons, texts_for_lessons


async def check_status_and_remind(callback: types.CallbackQuery):
    # print("BEFORE the sleep statement")
    time.sleep(10) # 600
    # print("AFTER the sleep statement")
    if db.get_status_from_user(id=callback.from_user.id) == 1:
        print(f"db.get_status_from_user(id=callback.from_user.id)={db.get_status_from_user(id=callback.from_user.id)}")
        builder = InlineKeyboardBuilder()
        builder.add(
            types.InlineKeyboardButton(
            text=" 30 минут",
            callback_data="remind30min"),
            types.InlineKeyboardButton(
            text=" 1 час",
            callback_data="remind1hour"),
            types.InlineKeyboardButton(
            text=" 2 часа",
            callback_data="remind2hour"),
            types.InlineKeyboardButton(
            text=" 3 часа",
            callback_data="remind3hour"))
        
        await callback.message.answer(text="🚀 <b>Не откладывай просмотр этого видео!</b>"
                                            "\n\nИначе можешь упустить<b> шанс заговорить на английском🇺🇸🇬🇧</b>"
                                            "\n\n<i>Если сейчас не подходящий момент, дай знать</i>" 
                                            "\n\n<b>и я напомню тебе позже,</b> чтобы ты не пропустил этот важный урок." 
                                            "\n\nГОТОВ?")
        await callback.message.answer(text="Напомнить через: ",
                                      reply_markup=builder.as_markup())
        # time.sleep(10) # загушка поменять
    else:
        db.set_status(status_id=2, id = callback.from_user.id)
        await remind_to_watch_this(callback)

@router_reminders.callback_query(F.data.in_(["remind30min", "remind1hour", "remind2hour", "remind3hour"]))
async def sent_lesson(callback: types.CallbackQuery):
    callback.message.delete
    match callback.data:
        case "remind30min": 
            period_of_remider = "30 минут"
            time_sleep = 5 #1800
        case "remind1hour": 
            period_of_remider = "1 час"
            time_sleep = 3600
        case "remind2hour": 
            period_of_remider = "2 часа"
            time_sleep = 7200
        case "remind3hour": 
            period_of_remider = "3 часа"
            time_sleep = 10800

    await callback.message.answer(text="🕐 Отлично! "
                                "\n\n<b>Я напомню тебе о видео через </b>" + f"<b>{period_of_remider}</b>")
    time.sleep(time_sleep)

    video_from_url = URLInputFile(video_lessons[db.get_video_id_from_user(id = callback.from_user.id)-1])
    callback.message.video
    await callback.message.answer_video(
        video= video_from_url,
        caption=" "
    )

    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
            text="Следующий урок",
            callback_data="next_lesson")
        )
    text = "🔔 Это НАПОМИНАНИЕ: время учить английский!\n\n<b>Видео уже ждет тебя! 🎥 </b>\n\nДля максимального результат приготовь тетрадь и ручку! 📒✍️"
    await callback.message.answer(
            text=text, 
            reply_markup=builder.as_markup()
            )
    await callback.answer()
    
    # если юзер не реагирует на напоминание, запускаю цикл напоминаний снова
    check_status_and_remind(callback=callback)

@router_reminders.callback_query(F.data == "next_lesson")
async def watch_lesson(callback: types.CallbackQuery):
    db.set_status(status_id=2, id = callback.from_user.id)
    print(f"db.show_users()={db.show_users()}")
    pass

# напоминание через 10 мин, если не запросил урок
async def remind_if_lesson_did_not_watch(callback: types.CallbackQuery):
    # # time.sleep(600)
    # print("Before the sleep statement")
    # time.sleep(20)
    # print("After the sleep statement")
    # if db.get_status_from_user(id=callback.from_user.id) == 1:
    #     await callback.message.edit_text(text='Не забудь посмотреть видео')
    # else:
    #     db.set_status(status_id=2, id = callback.from_user.id)
    #     remind_to_watch_this()
    pass
    

# цикл напоминаний, если урок был выслан
async def remind_to_watch_this(callback: types.CallbackQuery):
 await time.sleep(1200)
 builder = InlineKeyboardBuilder()
 builder.add(types.InlineKeyboardButton(
    text="Да",
    callback_data="Ещё смотрю"),
    types.InlineKeyboardButton(
    text="Дальше",
    callback_data="step1_2"))
 await callback.message.edit_text(text='Ты уже посмотрел видео?',
                                  reply_markup=builder.as_markup())
 
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

