from aiogram import F
from aiogram import types
from aiogram.types import URLInputFile, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from .reminders import remind_to_watch_this
from config import video_lessons, texts_for_lessons
from loader import router_lessons, db, bot
import time
from aiogram.filters import Command
from asyncio import Lock
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from .fsm import Quiz

# # класс для настройки машины состояний
# class Step(StatesGroup):
#     ask = State()
#     answer = State()

# отправка первого видео урока
@router_lessons.callback_query(F.data == "lesson_1")
async def send_lesson_1(callback: types.CallbackQuery):
    
    video_id = 0 
    video = video_lessons[video_id]
    db.set_video_id(video_id=video_id, id = callback.from_user.id)
    callback.message.delete

    # Отправка файла по ссылке
    video_from_url = URLInputFile(video)
    callback.message.video
    await callback.message.answer_video(
        video= video_from_url,
        caption=" "
    )

    text = texts_for_lessons[video_id]
    await callback.message.answer(text=text)
    callback.answer()

    db.set_status(status_id=1, id = callback.from_user.id) # урок отправлен

    await remind_to_watch_this(callback)

# срабатывает если пользователь посмотрел предыдущий урок
@router_lessons.callback_query(F.data == "lesson_2")
async def before_lesson_2(callback: types.CallbackQuery):
    db.set_status(status_id=3, id = callback.from_user.id) # предыдущее видео уже просмотрено
    # print(f"index video = {video_lessons.index(video_lessons[db.get_video_id_from_user(id = callback.from_user.id)])}")
    callback.message.delete
    text = "<b>Супер! Ты на правильном пути!</b>\n\nВижу твою мотивацию и стремление!\n\n<b>Держи второе видео! 🎥</b>\n\n"
    callback.message.delete
    await callback.message.answer(text = text)
    # print(f"I'M HERE")
    # time.sleep(2)
    await send_lesson_2(callback=callback)
    
    # match db.get_video_id_from_user(id = callback.from_user.id)+1:
    #     case 1: 
    #         text = "<b>Супер! Ты на правильном пути!</b>\n\nВижу твою мотивацию и стремление!\n\n<b>Держи второе видео! 🎥</b>\n\n"
    #         callback.message.delete
    #         await callback.message.answer(text = text)
    #         print(f"I'M HERE")
    #         time.sleep(2)
    #         send_lesson_2(callback=callback)
    #     case 2: 
    #         text1 = "🌟 <b>Как только закончишь, дай знать! </b>\n\nОтправлю тебя следующее видео! 🎥"
    #         builder = InlineKeyboardBuilder()
    #         builder.add(
    #             types.InlineKeyboardButton(
    #             text=" Все готово! Давай новое видео!",
    #             callback_data="lesson_3"))
    #         callback.message.delete
    #         await callback.message.answer(text = text1, reply_markup=builder.as_markup())

    #         time.sleep(2)
    #     case 3:
    #         callback.message.answer(text="🌟 Как ты оцениваешь первые 3 урока?\n\nТы уже чувствуешь, как усиливается твой английский!\n\n<b>Скажи мне:</b> \n\n<i>Where are you from?</i>")
    #         print(f"callback.message.text= {callback.message.text}")
    #         # ввод от польщзователя
    #         answer = bot.get_chat
    #         print(f"get_chat = {answer}")
    #         builder = InlineKeyboardBuilder()
    #         builder.add(
    #             types.InlineKeyboardButton(
    #             text=" Да",
    #             callback_data=""),
    #             types.InlineKeyboardButton(
    #             text=" Давай передохнем",
    #             callback_data=""))
    #         await callback.message.delete
    #         await callback.message.answer(text= "🚀 Отлично! \n\n<b>Готов к 4-му, заключительному и самому увлекательному видео? </b>\n\nВ НЕМ ТЫ:\n\n1) освоишь искусство диалога 🗣\n\n2) преодолеешь языковой барьер 🌐\n\n3) значительно пополнишь свой словарный запас 📚",
    #                                       reply_markup=builder.as_markup())
    #     case 4: pass

    # await send_lesson(callback = callback)

# отправка второго видео урока
# @router_lessons.callback_query(F.data == "lessons")
# @router_lessons.callback_query(Command("send"))
async def send_lesson_2(callback: types.CallbackQuery):

    video_id = 1#db.get_video_id_from_user(id = callback.from_user.id)
    video = video_lessons[video_id]
    db.set_video_id(video_id=video_id, id = callback.from_user.id)

    callback.message.delete

    # Отправка файла по ссылке
    video_from_url = URLInputFile(video)
    callback.message.video
    await callback.message.answer_video(
        video= video_from_url,
        caption=" "
    )

    text = texts_for_lessons[video_id]
    await callback.message.answer(text=text)
    callback.answer()

    db.set_status(status_id=1, id = callback.from_user.id) # урок отправлен

    time.sleep(10) # 20 мин
    
    text1 = "🌟 <b>Как только закончишь, дай знать! </b>\n\nОтправлю тебе следующее видео! 🎥"
    builder = InlineKeyboardBuilder()
    builder.add(
        types.InlineKeyboardButton(
        text=" Все готово! Давай новое видео!",
        callback_data="lesson_3"))
    callback.message.delete
    await callback.message.answer(text = text1, reply_markup=builder.as_markup())

    # time.sleep(2)

    # await send_next_lesson(callback=callback)


@router_lessons.callback_query(F.data == "lesson_3")
async def send_lesson_3(callback: types.CallbackQuery, state = None):

    text = "🌟 ОТЛИЧНО!\n\n<b>Ты молодец и уже на правильном пути. </b>\n\nЯ уверен, что твои усилия принесут плоды! \n\n<b>Через 2 месяца ты будешь свободно общаться на английском! 🗣</b>"
    await callback.message.answer(text = text)
    # await send_lesson(callback = callback)
    video_id = 2#db.get_video_id_from_user(id = callback.from_user.id)
    video = video_lessons[video_id]
    db.set_video_id(video_id=video_id, id = callback.from_user.id)

    callback.message.delete

    # Отправка файла по ссылке
    video_from_url = URLInputFile(video)
    callback.message.video
    await callback.message.answer_video(
        video= video_from_url,
        caption=" "
    )

    text = texts_for_lessons[video_id]
    await callback.message.answer(text=text)
    callback.answer()

    db.set_status(status_id=1, id = callback.from_user.id) # урок отправлен

    time.sleep(10) # 20 мин

    await callback.message.answer(text="🌟 Как ты оцениваешь первые 3 урока?\n\nТы уже чувствуешь, как усиливается твой английский!\n\n<b>Скажи мне:</b> \n\n<i>Where are you from?</i>")
    # print(f"callback.message.text= {callback.message.text}")
    # ввод от пользователя
    await state.set_state(Quiz.ask)
    await get_answer(message=callback.message)

    # await get_answer(message=callback.message)

    builder = InlineKeyboardBuilder()
    builder.add(
        types.InlineKeyboardButton(
        text=" Да",
        callback_data="lesson_4"),
        types.InlineKeyboardButton(
        text=" Давай передохнем",
        callback_data="wait"))
    callback.message.delete
    await callback.message.answer(text= "🚀 Отлично! \n\n<b>Готов к 4-му, заключительному и самому увлекательному видео? </b>\n\nВ НЕМ ТЫ:\n\n1) освоишь искусство диалога 🗣\n\n2) преодолеешь языковой барьер 🌐\n\n3) значительно пополнишь свой словарный запас 📚",
                                    reply_markup=builder.as_markup())
    
# @router_lessons.callback_query(content_types=types.ContentType.TEXT, state=Step.ask)
async def get_answer(message: types.Message, state = None):
    await state.set_state(Quiz.answer)
    await state.update_data(text=message.text)
    print(f"callback.message.text = {message.text}")

@router_lessons.callback_query(F.data == "lesson_4")#, state=Step.answer)
async def send_lesson_3(callback: types.CallbackQuery):

    text = "<b>Класс! 👍</b>\n\nМеня радует твое стремление! 😊"
    await callback.message.answer(text = text)
    # await send_lesson(callback = callback)
    video_id = 3#db.get_video_id_from_user(id = callback.from_user.id)
    video = video_lessons[video_id]
    db.set_video_id(video_id=video_id, id = callback.from_user.id)

    callback.message.delete

    # Отправка файла по ссылке
    video_from_url = URLInputFile(video)
    callback.message.video
    await callback.message.answer_video(
        video= video_from_url,
        caption=" "
    )

    text = texts_for_lessons[video_id]
    await callback.message.answer(text=text)
    callback.answer()

    db.set_status(status_id=1, id = callback.from_user.id) # урок отправлен

    time.sleep(10) # 25 мин

    builder = InlineKeyboardBuilder()
    builder.add(
        types.InlineKeyboardButton(
        text="Я реально уже могу немного говорить",
        callback_data=""),
        types.InlineKeyboardButton(
        text="Мне надо пройти его еще раз и все получится!",
        callback_data=""),
        types.InlineKeyboardButton(
        text="Мне было очень мало! Я хочу еще!",
        callback_data=""))
    callback.message.delete
    await callback.message.answer(text= "🌟 Как тебе уроки? \n\nОщущаешь прогресс?",
                                    reply_markup=builder.as_markup())