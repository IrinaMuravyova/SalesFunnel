TOKEN = '6562224055:AAEZRGuEsAwNxets5xeUTQV8UbAfxWmYhGM'
# from pydantic_settings import BaseSettings, SettingsConfigDict
# from pydantic import SecretStr


# class Settings(BaseSettings):
#     # Желательно вместо str использовать SecretStr 
#     # для конфиденциальных данных, например, токена бота
#     bot_token: SecretStr

#     # Начиная со второй версии pydantic, настройки класса настроек задаются
#     # через model_config
#     # В данном случае будет использоваться файла .env, который будет прочитан
#     # с кодировкой UTF-8
#     model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


# # При импорте файла сразу создастся 
# # и провалидируется объект конфига, 
# # который можно далее импортировать из разных мест
# config = Settings(BaseSettings)

video_lessons = ["https://youtu.be/GavBpRVYilE",
                 "https://youtu.be/Yf9Pv7Mx21M",
                 "https://youtu.be/NE2SjbJo-iA",
                 "https://youtu.be/2xi8sxcQ0lY"]

texts_for_lessons = ["Первое видео - это база! Основа основ - грамматика! Она помогает вам не бездумно заучивать фразы, а учиться строить их самостоятельно! Но только на примере и практике можно выучить любые правила! Успехов в обучении! ",
                     "Второе видео - это полезные фразы, зная которые тебе будет гораздо легче начать говорить уже сразу, не ожидая более сложных конструкций в грамматике! ",
                     "В этом видео я подготовил тебе разговорные ситуации. Это развивает разговорный английский, аудирование, снимает страх языкового барьера и увеличивает словарный запас! Ты уже после этого урока сможешь говорить на базовые темы!",
                     "В этом видео я подготовил для тебя диалоги, которые построены так, как говорят носители языка! Ты сможешь не просто правильно строить предложения, но и звучать, как носитель! "]

