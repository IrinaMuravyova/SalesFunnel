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
        callback_data="step1_1"),
        types.InlineKeyboardButton(
        text="Дальше",
        callback_data="step1_2")
    )
    await message.answer("Привет! 🎉 Если ты здесь, значит, ты готов начать говорить на английском! 🇬🇧 Что умеет этот бот? 🤖 Он не только поможет заговорить на английском уже после первого урока, но и подберёт индивидуальную программу, подходящую именно для тебя! ✨ Так ты сможешь довести свой английский до автоматизма! 🚀",
        reply_markup=builder.as_markup())

@router.callback_query(F.data == "step1_1")
async def send_random_value(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Хочу",
        callback_data="step2")
    )
    await callback.message.edit_text(
        text="Привет! 🌌 На связи Александр Бебрис и мой проект “English Galaxy” 🌠. Давай знакомиться! 🤝 Далее я расскажу, как этот бот поможет тебе свободно заговорить на английском! 🚀 Самое удивительное: наша методика настолько интуитивна и проста, что английский будто сам усвоится у тебя! ✨ Но помни: твои большие усилия и регулярные занятия - ключ к успеху! 💪",
        reply_markup=builder.as_markup()
    )
    # await callback.message.edit_reply_markup()
    # await callback.message.answer(
    #     text="На связи Александр Бебрис и мой проект “English Galaxy”. Я Предлагаю познакомиться и потом я расскажу тебе, как этот бот поможет тебе заговорить на  английском! Самое крутое, что методика настолько простая, что английский будет усваиваться сам! Но тебе надо приложить усилия и просто заниматься!",
    #     reply_markup=builder.as_markup(),
    #     show_alert=True
    # )
    await callback.answer()

@router.callback_query(F.data == "step1_2") 
async def send_message_to_step2(callback: types.CallbackQuery): 
    
    name = callback.message.from_user.first_name
    
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Хочу",
        callback_data="step2")
    )
    await callback.message.edit_reply_markup()
    await callback.message.answer(
        text=f"Привет, <b>{name}</b>!  🌟 Если ты мечтаешь свободно говорить на английском, успешно сдать международные экзамены 📜, начать новую жизнь в англоговорящей стране 🌍, путешествовать без языковых барьеров ✈️ или произвести впечатление на собеседовании 💼 - ты в нужном месте! Всего за 4 коротких урока 📚 ты сможешь начать общаться на базовом английском и убедиться, что английский - это проще, чем кажется, когда у тебя правильный подход и методика 🚀. Мы поберем идеальный для тебя формат обучения и составим программу, которая приведет тебя к желаемому результату в кратчайшие сроки! 💪",
        reply_markup=builder.as_markup(),
        show_alert=True,
        callback_data="step2"
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
        text="По нашей уникальной методике 📚 учатся миллионы учеников по всему миру 🌍! И каждый день мы получаем сотни отзывов благодарности 💌. Люди делятся своими впечатляющими успехами и радостью от освоения английского языка! 🎉. ",
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
        text="При регулярных занятиях 📅 всего за полгода наши студенты достигают уверенного среднего уровня разговорного английского 🗣️. А за год они не только готовятся к международным экзаменам 📜, но и успешно сдают их, получая высокие баллы! 🌟🎓",
        reply_markup=builder.as_markup()
    )
    await callback.answer()

@router.callback_query(F.data == "step4")
async def send_message_to_step5(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    # builder.add(types.InlineKeyboardButton(
    #     text="<17",
    #     callback_data="step5"),
    #     types.InlineKeyboardButton(
    #     text="17-22",
    #     callback_data="step5"),
    #     types.InlineKeyboardButton(
    #     text="23-29",
    #     callback_data="step5"),
    #     types.InlineKeyboardButton(
    #     text="30-39",
    #     callback_data="step5"),
    #     types.InlineKeyboardButton(
    #     text="40-49",
    #     callback_data="step5"),
    #     types.InlineKeyboardButton(
    #     text="50-59",
    #     callback_data="step5"),
    #     types.InlineKeyboardButton(
    #     text="60<",
    #     callback_data="step5")
    # )
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
        text="🤝 А теперь давай немного познакомимся! 🌟 Расскажи мне немного о себе, я очень хочу узнать больше о тебе и какие у тебя цели в изучении английского! 📝"
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
        text="Для работы в it",
        callback_data="step6")),
    builder.row(types.InlineKeyboardButton(
        text="Для работы в офисе",
        callback_data="step6")),
    builder.row(types.InlineKeyboardButton(
        text="Для работы в иностранной компании",
        callback_data="step6")),
    builder.row(types.InlineKeyboardButton(
        text="Для повышения по должности",
        callback_data="step6")),
    builder.row(types.InlineKeyboardButton(
        text="Для учебы",
        callback_data="step6")),
    builder.row(types.InlineKeyboardButton(
        text="Для путешествий",
        callback_data="step6")),
    builder.row(types.InlineKeyboardButton(
        text="Для иммиграции в другую страну",
        callback_data="step6")),
    builder.row(types.InlineKeyboardButton(
        text="Для саморазвития",
        callback_data="step6")),
    builder.row(types.InlineKeyboardButton(
        text="Для чтения книг и просмотра фильмов",
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
        text="Рад познакомиться. Давай теперь я немного расскажу о себе.",
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
        text="🎥 Возможно, ты уже видел меня на YouTube? У меня самый популярный канал по изучению английского языка на русскоязычном YouTube с аудиторией в 2 млн. подписчиков! 🌟 Но в чем секрет такой популярности? 🤔",
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
        text="📚 На моем YT-канале ты найдешь множество бесплатных курсов по изучению английского языка, которые не только интересные, но и результативные! 🚀 ",
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
        text='🌟 Я обучаю уже 20 лет, провел более 10 000 живых уроков и записал столько же видеоуроков по английскому языку! 🎥 Моя методика проверена временем: миллионы учеников изучают английский именно по ней, и десятки тысяч из них достигают потрясающих результатов 🚀 - от свободного общения на английском до успешной сдачи ЕГЭ, международных экзаменов и поступления в зарубежные вузы. 🎓 Сотни тысяч отзывов на моем канале и в моем приложении "English Galaxy" - говорят об этом! 🌌',
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
        text="🔍 Итак, давайте перейдем к самой методике. Сегодня именно для тебя я подготовил особый подарок! 🎁  На моем YT-канале ты можешь найти часть моего платного курса - 1й урок.",
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
        text="Почему так важно пройти этот урок полностью?",
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
        text="🌟 После первого урока ты начнешь говорить на английском и поймешь базовые конструкции. Ты увидишь, что изучение может быть легким, и у нас нет переплаты за качество! 💬💸",
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
        text="Предлагаю уже перейти к 1 уроку! ",
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
        text="Но чтобы обучение было точно результативным - обязательно подпишись на мой канал и возвращайся за уроком!",
        reply_markup=builder.as_markup()
        )
    await callback.answer()

@router.callback_query(F.data == "step15")
async def send_message_to_step16(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Начать урок",
        callback_data="lessons")
    )
    await callback.message.edit_text(
        text="🌟 Отличное решение! Английский действительно откроет перед тобой множество новых возможностей и горизонтов в жизни! 🚪✨",
        reply_markup=builder.as_markup()
        )
    await callback.answer()

