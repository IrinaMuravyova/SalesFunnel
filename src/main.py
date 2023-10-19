import asyncio # для асинхронного запуска бота
import logging # для настройки логгирования, которое поможет в отладке

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage #хранилища данных для состояний пользователей

import config as config
from handlers._init_ import router
from handlers import messages, lessons
from pathlib import Path
# from db_api import Database


async def main():
    # создаём объект бота с нашим токеном
    bot = Bot(token=config.TOKEN, parse_mode=ParseMode.HTML) # HTML, чтобы избежать проблем с экранированием символов.
    dp = Dispatcher(storage=MemoryStorage()) # создаём объект диспетчера. все данные бота, которые мы не сохраняем в БД (к примеру состояния), будут стёрты при перезапуске
    dp.include_routers(messages.router, lessons.router) # подключает к нашему диспетчеру все обработчики
    # db_path = Path('db_api', 'database','techshop_database.db')
    # db = Database(db_path=db_path)
    await bot.delete_webhook(drop_pending_updates=True) # бот обрабатывал только те сообщения, которые пришли ему непосредственно во время его работы, а не за всё время
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types()) # запускаем бота
    

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())