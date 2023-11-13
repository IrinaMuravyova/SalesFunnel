# TOKEN = '6562224055:AAEZRGuEsAwNxets5xeUTQV8UbAfxWmYhGM'
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Settings(BaseSettings):
    # Желательно вместо str использовать SecretStr 
    # для конфиденциальных данных, например, токена бота
    bot_token: SecretStr

    # Начиная со второй версии pydantic, настройки класса настроек задаются
    # через model_config
    # В данном случае будет использоваться файла .env, который будет прочитан
    # с кодировкой UTF-8
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


# При импорте файла сразу создастся 
# и провалидируется объект конфига, 
# который можно далее импортировать из разных мест
config = Settings()

video_lessons = ["https://youtu.be/GavBpRVYilE",
                 "https://youtu.be/Yf9Pv7Mx21M",
                 "https://youtu.be/NE2SjbJo-iA",
                 "https://youtu.be/2xi8sxcQ0lY"]

texts_for_lessons = ["🌟 Первое видео - это фундамент!" 
                     "\n\n<b>Грамматика - сердце английского языка!</b>"
                     "\n\nОна позволяет не просто заучивать фразы, но и создавать их самому!"
                     "\n\n<i>Но без практики и примеров невозможно освоить правила.</i>"
                     "\n\nЖелаю успехов в изучении! 📚✨",
                     "🌟 Второе видео дарит тебе полезные фразы, с которыми "
                     "\n\nты сможешь <b>начать говорить на английском прямо сейчас, </b>"
                     "\n\nне дожидаясь сложных грамматических правил! 🗣",
                     "🎥 В этом видео тебя ждут реальные разговорные ситуации!"
                     "\n\n<b>ОНИ ПОМОГУТ: </b>"
                     "\n\n<b>1)</b> развить твой разговорный английский 🗣 "
                     "\n\n<b>2)</b> улучшить аудирование  🎧"
                     "\n\n<b>3)</b> преодолеть языковой барьер 🚫 "
                     "\n\n<b>4)</b> пополнить словарный запас 📚"
                     "\n\n<b>И САМОЕ ГЛАВНОЕ:</b>" "\n\nПосле этого урока <b>ты сможешь общаться</b> по базовым темам!",
                     "🎥 В этом видео <b>тебя ждут диалоги,</b> которые"
                     "\n\nпостроены так, <b>как говорят носители языка</b>! "
                     "\n\nТЫ СМОЖЕШЬ:"
                     "\n\n<b>1)</b> правильно формулировать свои мысли 💬"
                     "\n\n<b>2)</b> будешь звучать как настоящий носитель английского! 🗣"]

