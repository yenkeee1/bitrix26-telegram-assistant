import os
from dotenv import load_dotenv

# Загружаем переменные из файла .env
load_dotenv()

class Config:
    # Токен Telegram бота
    TELEGRAM_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    
    # Строка подключения к базе данных
    DATABASE_URL = os.getenv('DATABASE_URL')
    
    @classmethod
    def check_tokens(cls):
        """Проверяем, что все токены загружены"""
        if not cls.TELEGRAM_TOKEN:
            raise ValueError('❌ Не указан TELEGRAM_BOT_TOKEN в .env')
        if not cls.DATABASE_URL:
            raise ValueError('❌ Не указан DATABASE_URL в .env')
        print("✅ Все токены загружены корректно")
        return True

# Проверяем сразу при импорте
Config.check_tokens()