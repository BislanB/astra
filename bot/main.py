import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from core.config import settings
from bot.handlers import base, bricks

async def start_bot():
    # Настройка логирования
    logging.basicConfig(level=logging.INFO)
    
    # Инициализация бота
    bot = Bot(token=settings.BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    
    # Регистрация обработчиков
    dp.include_router(base.router)
    dp.include_router(bricks.router)
    
    # Запуск бота в режиме polling
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(start_bot())