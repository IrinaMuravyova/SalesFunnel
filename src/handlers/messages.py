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
    await message.answer("Привет! Если ты в этом боте, то значит ты готов заговорить на английском! Что этот бот умеет? Он поможет тебе заговорить на английском уже после первого урока и правильно подобрать программу, максимально эффективную для тебя! И ты мог довести свой английский до автоматизма.",
        reply_markup=builder.as_markup())

@router.callback_query(F.data == "step1_1")
async def send_random_value(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Хочу",
        callback_data="step2")
    )
    await callback.message.edit_text(
        text="На связи Александр Бебрис и мой проект “English Galaxy”. Я Предлагаю познакомиться и потом я расскажу тебе, как этот бот поможет тебе заговорить на  английском! Самое крутое, что методика настолько простая, что английский будет усваиваться сам! Но тебе надо приложить усилия и просто заниматься!",
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
        text=f"Привет, <b>{name}</b>! Если ты планируешь быстро и качественно заговорить на английском, сдать международные экзамены, переехать в англоговорящую страну, путешествовать или пройти собеседование на должность мечты - ты в нужном месте! Всего за 4 коротких урока ты сможешь заговорить на элементарном английском и понять, что английский - это не сложно, если ты занимаешься по правильной методике, подобрать свой формат обучения и получить программу, которая поможет тебе быстрее прийти к своей цели.",
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
        text="По нашей методике учатся миллионы учеников по всему миру и каждый день мы получаем сотни отзывов благодарности, в которых люди пишут о своих успехах. ",
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
        text="При регулярных занятиях за пол года наши ученики выходят на уверенный средний уровень разговорного английского, а за год готовятся к международным экзаменам и сдают на высокий балл!",
        reply_markup=builder.as_markup()
    )
    await callback.answer()

@router.callback_query(F.data == "step4")
async def send_message_to_step5(callback: types.CallbackQuery):
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
    await callback.message.edit_text(
        text="А теперь, давай немного познакомимся? Расскажи немного о себе."
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
        text="Возможно, ты видел меня на YouTube канале. У меня самый большой канал по изучению Английского языка на русскоговорящем YouTube. 2 млн подписчиков. За счет чего у меня такая большая аудитория?",
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
        text="На моем канале очень много бесплатных и очень результативных курсов по изучению Английского языка. ",
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
        text="Я обучаю уже почти 20 лет, провел около 10000 живых уроков по английскому языку и записал около 10000 видеоуроков. По моей методике учатся миллионы учеников, а десятки тысяч самых упорных добиваются потрясающих результатов: начинают говорить, сдают ЕГЭ, международные экзамены и поступают в иностранные вузы. О чем говорят сотни тысяч отзывов на канале и в моем приложении по изучению Английского языка English Galaxy",
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
        text="А теперь к методике. У меня есть один платный курс, который частично выложен на YouTube, но сейчас я хочу подарить тебе доступ к полной версии 1 урока этого курса.",
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
        text="Уже после 1 урока ты начнешь немного говорить и поймешь простые конструкции английском языке, но главное, ты поймешь, что английский можно учить в легкости и за уроки не надо платить большие деньги, чтобы действительно добиться результат!",
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
        text="Отлично! Рад, что-то решился изменить свою жизнь! Ведь английский открывает очень много новых дверей в твоей жизни!",
        reply_markup=builder.as_markup()
        )
    await callback.answer()

