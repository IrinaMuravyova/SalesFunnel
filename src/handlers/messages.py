# import asyncio
from aiogram import Router, F
from aiogram import types
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from loader import db, router_messages
# from time import sleep 
import time


def all_values_of_field(table: str, number_of_field: int) -> [str]:
    all_values_of_field = []
    for value_of_field in db.select_data_of_table(table = table):
        all_values_of_field.append(value_of_field[number_of_field])
        # print(f"all_values_of_field = {all_values_of_field}")
    return all_values_of_field

@router_messages.message(Command("start"))
async def start_handler(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="На связи Бебрис",
        callback_data="step1")
    )

    # если пользователь новый, то добавляю в таблицу Users
    if message.from_user.id not in all_values_of_field(table="Users", number_of_field=0):
        db.add_user(id = message.from_user.id)

    await message.answer(f"<b>Привет, {message.from_user.first_name}!</b> 🌟" 
                            "\n\nЕсли ты мечтаешь:" 
                            "\n\n1) Свободно говорить на английском"
                            "\n\n2) Успешно сдать международные экзамены 📜"
                            "\n\n3) Начать новую жизнь в англоговорящей стране 🌍"
                            "\n\n4) Путешествовать без языковых барьеров ✈️ "
                            "\n\n5) Произвести впечатление на собеседовании 💼"
                            "\n\n- ТЫ В НУЖНОМ МЕСТЕ"
                            "\n\n📚<b> Всего за 4 коротких урока </b>📚"
                            "\n\nТы сможешь начать общаться на базовом английском и <b>убедиться, что английский - это проще, чем кажется</b>, когда у тебя <b>правильный подход и методика</b> 🚀"
                            "\n\nНАШ БОТ:"
                            "\n\n1. <b>Подберет</b> идеальный для тебя <b>формат обучения</b>"  
                            "\n2. <b>Составит программу</b>, которая приведет тебя к желаемому результату в кратчайшие сроки! 💪",
        reply_markup=builder.as_markup())

@router_messages.callback_query(F.data == "step1")
async def send_random_value(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Хочу",
        callback_data="step2")
    )
    await callback.message.edit_text(
        text="<b>Привет!</b> 🌟"  
                "\n\nНа связи Александр Бебрис и мой проект “English Galaxy”.  <b>Давай знакомиться!</b> 🤝 "
                "\n\nДалее я расскажу, как этот бот поможет тебе свободно заговорить на английском! 🚀 "
                "\n\n<b>Самое удивительное:</b> наша методика настолько интуитивна и проста, что английский будто сам усвоится у тебя! ✨ "
                "\n\nНо помни: <b>твои большие усилия и регулярные занятия - ключ к успеху!</b> 💪",
        reply_markup=builder.as_markup()
    )
    await callback.answer()

@router_messages.callback_query(F.data == "step2")
async def send_message_to_step3(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Интересно",
        callback_data="step3")
    )
    await callback.message.edit_text(
        text="<b>По нашей уникальной методике </b>📚 учатся миллионы учеников по всему миру 🌍! "
                "\n\nИ каждый день мы получаем сотни отзывов благодарности 💌"
                "\n\nЛюди делятся своими впечатляющими успехами и радостью от освоения английского языка! 🎉",
        reply_markup=builder.as_markup()
    )
    await callback.answer()

@router_messages.callback_query(F.data == "step3")
async def send_message_to_step4(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Здорово!",
        callback_data="step4")
    )
    await callback.message.edit_text(
        text="📅 При регулярных занятиях всего за полгода "
                "\n\n<b>наши студенты</b> достигают уверенного среднего уровня разговорного английского 🗣"
                "\n\nА за год они не только готовятся к международным экзаменам 📜"
                "\n\nно и <b>успешно сдают их, получая высокие баллы!</b> 🌟🎓",
        reply_markup=builder.as_markup()
    )
    await callback.answer()

@router_messages.callback_query(F.data == "step4")
async def send_message_to_step5(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="<17",
        callback_data="<17_button_pressed"))
    builder.row(types.InlineKeyboardButton(
        text="17-22",
        callback_data="17-22_button_pressed"),
        types.InlineKeyboardButton(
        text="23-29",
        callback_data="23-29_button_pressed"),
        types.InlineKeyboardButton(
        text="30-39",
        callback_data="30-39_button_pressed"))
    builder.row(types.InlineKeyboardButton(
        text="40-49",
        callback_data="40-49_button_pressed"),
        types.InlineKeyboardButton(
        text="50-59",
        callback_data="50-59_button_pressed"))
    builder.row(types.InlineKeyboardButton(
        text="60<",
        callback_data="60<_button_pressed"))
    
    await callback.message.edit_text(
        text="🤝 <b>А теперь давай немного познакомимся! </b>🌟 "
                "\n\nРасскажи мне немного о себе"
                "\n\nЯ очень хочу узнать больше о тебе и какие у тебя цели в изучении английского! 📝"
        )
    await callback.message.answer(
        text="Сколько тебе лет?",
        reply_markup=builder.as_markup(),
        show_alert=True
    )
    await callback.answer()

@router_messages.callback_query(F.data.in_(["step5", 
                                            "<17_button_pressed", 
                                            "17-22_button_pressed",
                                            "23-29_button_pressed", 
                                            "30-39_button_pressed", 
                                            "40-49_button_pressed", 
                                            "50-59_button_pressed", 
                                            "60<_button_pressed"]))
async def send_message_to_step6(callback: types.CallbackQuery):
     # сохраняю возрастной диапазон пользователя после нажатия на кнопку
    for age_category in all_values_of_field(table="AgeCategories", number_of_field=1):
        if callback.data.startswith(age_category):
            db.set_age_category(age_category = age_category, id = callback.from_user.id)
    # print(f"db.show_users()={db.show_users()}")
    
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Для работы в IT 🖥",
        callback_data="Для работы в IT")),
    builder.row(types.InlineKeyboardButton(
        text="Для работы в офисе 🏢",
        callback_data="Для работы в офисе")),
    builder.row(types.InlineKeyboardButton(
        text="Для работы в иностранной компании 🌍",
        callback_data="Для работы в иностранной")),
    builder.row(types.InlineKeyboardButton(
        text="Для повышения по должности 📈🚀",
        callback_data="Для повышения по должности")),
    builder.row(types.InlineKeyboardButton(
        text="Для учебы 📚🎓",
        callback_data="Для учебы")),
    builder.row(types.InlineKeyboardButton(
        text="Для путешествий ✈️🌍",
        callback_data="Для путешествий")),
    builder.row(types.InlineKeyboardButton(
        text="Для иммиграции в другую страну 🌏",
        callback_data="Для иммиграции")),
    builder.row(types.InlineKeyboardButton(
        text="Для саморазвития 📖📚🧠",
        callback_data="Для саморазвития")),
    builder.row(types.InlineKeyboardButton(
        text="Для чтения книг и просмотра фильмов 📖📺🍿",
        callback_data="Для чтения книг")),
    builder.row(types.InlineKeyboardButton(
        text="Другое",
        callback_data="Другое"))

    await callback.message.edit_text(
        text="Скажи, для чего ты учишь английский?",
        reply_markup=builder.as_markup()
        )
    await callback.answer()

@router_messages.callback_query(F.data.in_(["step6", 
                                            "Для работы в IT", 
                                            "Для работы в офисе",
                                            "Для работы в иностранной", 
                                            "Для повышения по должности", 
                                            "Для учебы", 
                                            "Для путешествий", 
                                            "Для иммиграции",
                                            "Для саморазвития",
                                            "Для чтения книг",
                                            "Другое"]))
async def send_message_to_step7(callback: types.CallbackQuery):
    # сохраняю выбранное значение цели обучения
    for goal in all_values_of_field(table="Goals", number_of_field=1):
        if callback.data.startswith(goal):
            db.set_goal_id(goal = goal, id = callback.from_user.id)
    # print(f"db.show_users()={db.show_users()}")

    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Давай",
        callback_data="step7")
    )
    await callback.message.edit_text(
        text="<b>Рад познакомиться</b> 😊 Давай теперь я немного расскажу о себе.",
        reply_markup=builder.as_markup()
        )
    await callback.answer()

@router_messages.callback_query(F.data == "step7")
async def send_message_to_step8(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Вау! 2 миллиона подписчиков! ",
        callback_data="step8")
    )
    await callback.message.edit_text(
        text="🎥 Возможно, ты уже видел меня на YouTube? "
                "\n\nУ меня самый популярный канал по изучению английского языка на русскоязычном YouTube с аудиторией в 2 млн. подписчиков! 🌟 "
                "\n\nНо в чем секрет такой популярности? 🤔",
        reply_markup=builder.as_markup()
        )
    await callback.answer()

@router_messages.callback_query(F.data == "step8")
async def send_message_to_step9(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Круто!",
        callback_data="step9")
    )
    await callback.message.edit_text(
        text="📚 На моем <b>YT-канале</b> "
                '\n\n"АНГЛИЙСКИЙ ЯЗЫК ПО ПЛЕЙЛИСТАМ"'
                "\n\n<b>Ты найдешь</b> "
                "\n\nмножество <b>бесплатных курсов</b> по изучению английского языка, "
                "\n\nкоторые не только интересные, но и <b>результативные!</b> 🚀",
        reply_markup=builder.as_markup()
        )
    await callback.answer()

@router_messages.callback_query(F.data == "step9")
async def send_message_to_step10(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Ого!",
        callback_data="step10")
    )
    await callback.message.edit_text(
        text="Я обучаю уже 20 лет 🌟 "
                "\n\n👉 <b>провел</b> более 10 000 живых уроков "
                "\n\n👉 <b>записал</b> столько же видеоуроков по английскому языку! 🎥 "
                "\n\nМоя методика проверена временем! "
                "\n\n<b>Миллионы учеников изучают английский именно по ней, и</b> десятки тысяч из них достигают <b>потрясающих результатов</b> 🚀: "
                "\n\n- от свободного общения на английском до успешной сдачи ЕГЭ!"
                "\n\n- международных экзаменов и поступления в зарубежные вузы🎓 "
                '\n\nСотни тысяч отзывов на моем канале и в моем приложении "English Galaxy" - говорят об этом!',
        reply_markup=builder.as_markup()
        )
    await callback.answer()

@router_messages.callback_query(F.data == "step10")
async def send_message_to_step11(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Интересно",
        callback_data="step11")
    )
    await callback.message.edit_text(
        text="🔍 Итак, давай перейдем к самой <b>методике. </b>"
                "\n\n<b>Сегодня</b> именно <b>для тебя</b> я подготовил <b>особый подарок!</b> 🎁  "
                "\n\nНа моем <b>YT-канале</b> ты можешь найти <i>часть моего платного курса</i> - <b>1й урок.</b>",
        reply_markup=builder.as_markup()
        )
    await callback.answer()

@router_messages.callback_query(F.data == "step11")
async def send_message_to_step12(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Хочу знать",
        callback_data="step12")
    )
    await callback.message.edit_text(
        text="Почему так важно пройти этот урок полностью <b>прямо сейчас</b>? 🤔",
        reply_markup=builder.as_markup()
        )
    await callback.answer()

@router_messages.callback_query(F.data == "step12")
async def send_message_to_step13(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Вау! Классно",
        callback_data="step13")
    )
    await callback.message.edit_text(
        text="🌟 После <b>первого урока</b> ты:"
                "\n\n1) начнешь говорить на английском" 
                "\n\n2) поймешь базовые конструкции языка"
                "\n\nТы увидишь, что <b>изучение может быть легким,</b> и будешь знать - что у нет переплаты за качество! 💬",
        reply_markup=builder.as_markup()
        )
    await callback.answer()

@router_messages.callback_query(F.data == "step13")
async def send_message_to_step14(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Урок 1 ",
        callback_data="step14")
    )
    await callback.message.edit_text(
        text="Предлагаю перейти к уроку №1! 😊",
        reply_markup=builder.as_markup()
        )
    await callback.answer()

@router_messages.callback_query(F.data == "step14")
async def send_message_to_step15(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Уже подписан",
        callback_data="step15"),
        types.InlineKeyboardButton(
        text="Подписался",
        callback_data="step15")
    )
    await callback.message.edit_text(
        text="Но чтобы <b>обучение</b> было точно <b>результативным </b>- "
                "\n\n<b>обязательно подпишись</b> на мой YT-канал 🔔"
                "\n\nи возвращайся за уроком! 📚👋",
        reply_markup=builder.as_markup()
        )
    await callback.answer()

@router_messages.callback_query(F.data == "step15")
async def send_message_to_step16(callback: types.CallbackQuery):

    db.set_status(status_id=1, id = callback.from_user.id)
    print(f"db.show_users()={db.show_users()}")

    db.set_video_id(video_id=-1, id = callback.from_user.id) # убрать после отладки

    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Начать урок",
        callback_data="lesson_1")
    )
    await callback.message.edit_text(
        text="🌟<b> Отличное решение!</b> "
                "\n\nАнглийский действительно откроет перед тобой множество новых возможностей и горизонтов в жизни! 🚪✨",
        reply_markup=builder.as_markup()
        )
    await callback.answer()


