from aiogram import Bot, Dispatcher, Router
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage #хранилища данных для состояний пользователей

from config import config
import sqlite3
from pathlib import Path
from db_api import Database
from loguru import logger

def test_sql_error(func) -> None:
    try :
        func()
    except sqlite3.OperationalError as error_info:
        logger.debug(error_info)
    except Exception as error_info:
        logger.debug(error_info) 
           
bot = Bot(token=config.bot_token.get_secret_value(), parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage()) # создаём объект диспетчера. все данные бота, которые мы не сохраняем в БД (к примеру состояния), будут стёрты при перезапуске
router_messages = Router()
router_lessons = Router()
db_path = Path('db_api', 'database','clients.db')
db = Database(db_path=db_path)

funcs_for_test = (db.create_table_users, 
                db.create_table_age_categorys, 
                db.create_table_goals, 
                db.create_table_statuses)

for func in funcs_for_test:
    test_sql_error(func)

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

# db.add_status(id=1, status= "sent_video")
# db.add_status(id=2, status= "start_watch")
# db.add_status(id=3, status= "finished_watch")
# db.add_status(id=4, status= "remind_first")
# db.add_status(id=5, status= "remind_second")
# db.add_status(id=6, status= "remind_third")
# db.add_status(id=7, status= "add_time")
