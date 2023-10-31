import asyncio # для асинхронного запуска бота
import logging # для настройки логгирования, которое поможет в отладке

from config import config
from handlers import router_list
from loguru import logger
from loader import bot, dp
        
async def main():
    dp.include_routers(*router_list) # подключает к нашему диспетчеру все обработчики
    await bot.delete_webhook(drop_pending_updates=True) # бот обрабатывал только те сообщения, которые пришли ему непосредственно во время его работы, а не за всё время
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types()) # запускаем бота

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

