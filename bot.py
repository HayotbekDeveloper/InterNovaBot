import asyncio
from aiogram import Bot, Dispatcher, types, html
from config.bot_config import bot, dp
from handlers import create_profile, common, keyboard1
from middlewares.test_middleware import ChatActionMiddleware
from db.models import async_main

# main
async def main():
    await async_main()
    dp.message.middleware(ChatActionMiddleware())
    dp.include_routers(keyboard1.router,common.router, create_profile.router)
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
    
if __name__ == '__main__':
    asyncio.run(main())