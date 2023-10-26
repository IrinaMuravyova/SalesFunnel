from aiogram import Router, F
from aiogram import types
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

@router.message(Command("start"))
async def start_handler(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="На связи Бебрис",
        callback_data="step1")
    )

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

@router.callback_query(F.data == "step1")
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

@router.callback_query(F.data == "step2")
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

@router.callback_query(F.data == "step3")
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

@router.callback_query(F.data == "step4")
async def send_message_to_step5(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="<17",
        callback_data="step5"))
    builder.row(types.InlineKeyboardButton(
        text="17-22",
        callback_data="step5"),
        types.InlineKeyboardButton(
        text="23-29",
        callback_data="step5"),
        types.InlineKeyboardButton(
        text="30-39",
        callback_data="step5"))
    builder.row(types.InlineKeyboardButton(
        text="40-49",
        callback_data="step5"),
        types.InlineKeyboardButton(
        text="50-59",
        callback_data="step5"))
    builder.row(types.InlineKeyboardButton(
        text="60<",
        callback_data="step5"))
    
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
    

@router.callback_query(F.data == "step5")
async def send_message_to_step6(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Для работы в IT 🖥",
        callback_data="step6")),
    builder.row(types.InlineKeyboardButton(
        text="Для работы в офисе 🏢",
        callback_data="step6")),
    builder.row(types.InlineKeyboardButton(
        text="Для работы в иностранной компании 🌍",
        callback_data="step6")),
    builder.row(types.InlineKeyboardButton(
        text="Для повышения по должности 📈🚀",
        callback_data="step6")),
    builder.row(types.InlineKeyboardButton(
        text="Для учебы 📚🎓",
        callback_data="step6")),
    builder.row(types.InlineKeyboardButton(
        text="Для путешествий ✈️🌍",
        callback_data="step6")),
    builder.row(types.InlineKeyboardButton(
        text="Для иммиграции в другую страну 🌏",
        callback_data="step6")),
    builder.row(types.InlineKeyboardButton(
        text="Для саморазвития 📖📚🧠",
        callback_data="step6")),
    builder.row(types.InlineKeyboardButton(
        text="Для чтения книг и просмотра фильмов 📖📺🍿",
        callback_data="step6")),
    builder.row(types.InlineKeyboardButton(
        text="Другое",
        callback_data="step6")
    )
    await callback.message.edit_text(
        text="Скажи, для чего ты учишь английский?",
        reply_markup=builder.as_markup()
        )
    await callback.answer()

@router.callback_query(F.data == "step6")
async def send_message_to_step7(callback: types.CallbackQuery):
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

@router.callback_query(F.data == "step7")
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

@router.callback_query(F.data == "step8")
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

@router.callback_query(F.data == "step9")
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

@router.callback_query(F.data == "step10")
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

@router.callback_query(F.data == "step11")
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

@router.callback_query(F.data == "step12")
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

@router.callback_query(F.data == "step13")
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

@router.callback_query(F.data == "step14")
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

@router.callback_query(F.data == "step15")
async def send_message_to_step16(callback: types.CallbackQuery):
    # db.set_status(user_id=callback.message.from_user.id, status_id=1)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Начать урок",
        callback_data="lessons")
    )
    await callback.message.edit_text(
        text="🌟<b> Отличное решение!</b> "
                "\n\nАнглийский действительно откроет перед тобой множество новых возможностей и горизонтов в жизни! 🚪✨",
        reply_markup=builder.as_markup()
        )
    await callback.answer()

