from aiogram import Bot,Dispatcher
import logging
from config import PROXY_URL,TOKEN
from aiogram.client.session.aiohttp import AiohttpSession
from app.handlers import router

import asyncio

async def main():
    print("Запускаем бота...")
    print(f"Используем прокси: {PROXY_URL}")
    
    # Создание сессию с прокси
    session = AiohttpSession(proxy=PROXY_URL)
    
    # Создание бота
    bot = Bot(token=TOKEN, session=session)
    dp = Dispatcher()

    dp.include_router(router=router)
    
    try:
        # Проверка соединение
        me = await bot.get_me()
        print(f"Бот успешно запущен: @{me.username}")
        print(" Бот готов к работе!")
        
        # Запуск бота
        await dp.start_polling(bot)
    except Exception as e:
        print(f"Ошибка: {e}")
    
#точка входа
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n🛑 Программа завершена")
