import logging
import asyncio

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import user_handlers, other_handlers
from keyboards.main_menu import set_main_menu


#Init logger
logger = logging.getLogger(__name__)

#Function start bot
async def main():
    #Config logger
    logging.basicConfig(
        level = logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s '
               u'[%(asctime)s] - %(name)s - %(message)s'
    )

    logger.info('Starting bot')


    #Init config
    config: Config = load_config()

    #Init bot and dispatcher
    bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher()

    #Settings main menu
    await set_main_menu(bot)

    #Registering routers in the manager
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    #Skip the accumulated updates and run polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__=='__main__':
    try:
        #Run the main function
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        #Output an error message to the console
        logger.error('Bot Stopped')