# from main import dp
from aiogram import Router, F
from aiogram import types
from aiogram.types import Message 
from aiogram.types.user import User
from aiogram.filters import Command, CommandObject
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

@router.message(Command("start"))
async def start_handler(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="На связи Бебрис",
        callback_data="step1_1"),
        types.InlineKeyboardButton(
        text="Дальше",
        callback_data="step1_2")
    )
    await message.answer("Привет! Если ты в этом боте, то значит ты готов заговорить на английском! Что этот бот умеет? Он поможет тебе заговорить на английском уже после первого урока и правильно подобрать программу, максимально эффективную для тебя! И ты мог довести свой английский до автоматизма.",
        reply_markup=builder.as_markup())

@router.callback_query(F.data == "step1_1")
async def send_random_value(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Хочу",
        callback_data="step2")
    )
    await callback.message.answer(
        text="На связи Александр Бебрис и мой проект “English Galaxy”. Я Предлагаю познакомиться и потом я расскажу тебе, как этот бот поможет тебе заговорить на  английском! Самое крутое, что методика настолько простая, что английский будет усваиваться сам! Но тебе надо приложить усилия и просто заниматься!",
        reply_markup=builder.as_markup(),
        show_alert=True
    )
    await callback.answer()

@router.callback_query(F.data == "step1_2") #, Command("name")
async def send_message_to_step2(callback: types.CallbackQuery): #, command: CommandObject)
    # if command.args:
    #     await callback.message.answer(
    #     text="Привет, <b>{command.args}</b>! Если ты планируешь быстро и качественно заговорить на английском, сдать международные экзамены, переехать в англоговорящую страну, путешествовать или пройти собеседование на должность мечты - ты в нужном месте! Всего за 4 коротких урока ты сможешь заговорить на элементарном английском и понять, что английский - это не сложно, если ты занимаешься по правильной методике, подобрать свой формат обучения и получить программу, которая поможет тебе быстрее прийти к своей цели.",
    #     show_alert=True
    # )
    # else:
    #     await callback.answer("Пожалуйста, укажи своё имя после команды /name!",
    #                           show_alert=True)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Хочу",
        callback_data="step2")
    )
    await callback.message.answer(
        text="Привет, <b>{from_user.first_name}</b>! Если ты планируешь быстро и качественно заговорить на английском, сдать международные экзамены, переехать в англоговорящую страну, путешествовать или пройти собеседование на должность мечты - ты в нужном месте! Всего за 4 коротких урока ты сможешь заговорить на элементарном английском и понять, что английский - это не сложно, если ты занимаешься по правильной методике, подобрать свой формат обучения и получить программу, которая поможет тебе быстрее прийти к своей цели.",
        reply_markup=builder.as_markup(),
        show_alert=True,
        callback_data="step2"
    )
    await callback.answer()

@router.callback_query(F.data == "step2")
async def send_random_value(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Интересно",
        callback_data="step3")
    )
    await callback.message.answer(
        text="По нашей методике учатся миллионы учеников по всему миру и каждый день мы получаем сотни отзывов благодарности, в которых люди пишут о своих успехах. ",
        reply_markup=builder.as_markup(),
        show_alert=True
    )
    await callback.answer()

@router.callback_query(F.data == "step3")
async def send_random_value(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Здорово!",
        callback_data="step4")
    )
    await callback.message.answer(
        text="При регулярных занятиях за пол года наши ученики выходят на уверенный средний уровень разговорного английского, а за год готовятся к международным экзаменам и сдают на высокий балл!",
        reply_markup=builder.as_markup(),
        show_alert=True
    )
    await callback.answer()

@router.callback_query(F.data == "step4")
async def send_random_value(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="<17",
        callback_data="step5"),
        types.InlineKeyboardButton(
        text="17-22",
        callback_data="step5"),
        types.InlineKeyboardButton(
        text="23-29",
        callback_data="step5"),
        types.InlineKeyboardButton(
        text="30-39",
        callback_data="step5"),
        types.InlineKeyboardButton(
        text="40-49",
        callback_data="step5"),
        types.InlineKeyboardButton(
        text="50-59",
        callback_data="step5"),
        types.InlineKeyboardButton(
        text="60<",
        callback_data="step5")
    )
    await callback.message.answer(
        text="А теперь, давай немного познакомимся? Расскажи немного о себе.",
        show_alert=True
    )
    await callback.message.answer(
        text="Сколько тебе лет?",
        reply_markup=builder.as_markup(),
        show_alert=True
    )
    await callback.answer()
    