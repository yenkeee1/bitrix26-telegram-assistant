import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from config import Config

# Настройка логов
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Инициализация бота
bot = Bot(token=Config.TELEGRAM_TOKEN)
dp = Dispatcher()

# Команда /start
@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer(
        "🤖 Привет! Я Bitrix24 Assistant Bot\n\n"
        "Я помогу тебе с вопросами по API Bitrix24.\n"
        "Просто напиши свой вопрос, например:\n"
        "• Как добавить контакт через API?\n"
        "• Как работает метод crm.deal.list?\n"
        "• Как настроить вебхук?\n\n"
        "Пока я умею только отвечать на /start и /help, "
        "но скоро научусь искать ответы в документации!"
    )

# Команда /help
@dp.message(Command("help"))
async def help_command(message: types.Message):
    await message.answer(
        "📖 Помощь по использованию:\n\n"
        "/start - начало работы\n"
        "/help - эта справка\n\n"
        "Просто задай вопрос по Bitrix24 API, и я постараюсь помочь!\n"
        "Документация: https://apidocs.bitrix24.ru/"
    )

# Обработчик всех сообщений
@dp.message()
async def handle_message(message: types.Message):
    await message.answer(
        f"🔍 Ищу информацию по вашему запросу: '{message.text}'\n\n"
        "Пока что я в разработке, но скоро смогу отвечать на вопросы!\n"
        "А пока можете посмотреть документацию:\n"
        "https://apidocs.bitrix24.ru/"
    )

# Запуск бота
async def main():
    logger.info("=" * 50)
    logger.info("🚀 Запуск Bitrix24 Assistant Bot...")
    logger.info("=" * 50)
    
    # Удаляем вебхук (если был)
    await bot.delete_webhook(drop_pending_updates=True)
    
    # Запускаем опрос Telegram
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("⏹ Бот остановлен")
    except Exception as e:
        logger.error(f"❌ Ошибка: {e}")
        input("Нажми Enter для выхода...")