import asyncio # для асинхронного запуска бота
import logging # для настройки логгирования, которое поможет в отладке

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage #хранилища данных для состояний пользователей

import config as config
import sqlite3
from handlers._init_ import router
from handlers import messages, lessons
from pathlib import Path
from db_api._init_ import Database
from loguru import logger

def test_sql_error(func) -> None:
    try :
        func()
    except sqlite3.OperationalError as error_info:
        logger.debug(error_info)
    except Exception as error_info:
        logger.debug(error_info) 
        
async def main():
    # создаём объект бота с нашим токеном
    bot = Bot(token=config.TOKEN, parse_mode=ParseMode.HTML) # HTML, чтобы избежать проблем с экранированием символов.
    dp = Dispatcher(storage=MemoryStorage()) # создаём объект диспетчера. все данные бота, которые мы не сохраняем в БД (к примеру состояния), будут стёрты при перезапуске
    dp.include_routers(messages.router, lessons.router) # подключает к нашему диспетчеру все обработчики
    db_path = Path('db_api', 'database','clients.db')
    db = Database(db_path=db_path)
    await bot.delete_webhook(drop_pending_updates=True) # бот обрабатывал только те сообщения, которые пришли ему непосредственно во время его работы, а не за всё время
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types()) # запускаем бота

    funcs_for_test = (db.create_table_users, 
                    db.create_table_age_categorys, 
                    db.create_table_goals, 
                    db.create_table_statuses)

    for func in funcs_for_test:
        test_sql_error(func)

    db.add_goal(id=1, goal = "Для работы в it")
    db.add_goal(id=2, goal = "Для работы в офисе")
    db.add_goal(id=3, goal = "Для работы в иностранной компании")
    db.add_goal(id=4, goal = "Для повышения по должности")
    db.add_goal(id=5, goal = "Для учебы")
    db.add_goal(id=6, goal = "Для путешествий")
    db.add_goal(id=7, goal = "Для иммиграции в другую страну")
    db.add_goal(id=8, goal = "Для саморазвития")
    db.add_goal(id=9, goal = "Для чтения книг и просмотра фильмов")
    db.add_goal(id=10, goal = "Другое")

    db.add_age_category(id=1, age_category="<17")
    db.add_age_category(id=2, age_category="17-22")
    db.add_age_category(id=3, age_category="23-29")
    db.add_age_category(id=4, age_category="30-39")
    db.add_age_category(id=5, age_category="40-49")
    db.add_age_category(id=6, age_category="50-59")
    db.add_age_category(id=7, age_category="60<")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

# заполняем БД - цели обучения, возвратные категории

# db.add_goal(id=1, goal = "Для работы в it")
# db.add_goal(id=2, goal = "Для работы в офисе")
# db.add_goal(id=3, goal = "Для работы в иностранной компании")
# db.add_goal(id=4, goal = "Для повышения по должности")
# db.add_goal(id=5, goal = "Для учебы")
# db.add_goal(id=6, goal = "Для путешествий")
# db.add_goal(id=7, goal = "Для иммиграции в другую страну")
# db.add_goal(id=8, goal = "Для саморазвития")
# db.add_goal(id=9, goal = "Для чтения книг и просмотра фильмов")
# db.add_goal(id=10, goal = "Другое")

# db.add_age_category(id=1, age_category="<17")
# db.add_age_category(id=2, age_category="17-22")
# db.add_age_category(id=3, age_category="23-29")
# db.add_age_category(id=4, age_category="30-39")
# db.add_age_category(id=5, age_category="40-49")
# db.add_age_category(id=6, age_category="50-59")
# db.add_age_category(id=7, age_category="60<")
