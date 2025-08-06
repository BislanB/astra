from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text == "/start")
async def start_command(message: Message):
    await message.answer("🚀 Привет! Я бот для подготовки к конкурсу «Большая Перемена».\n\n"
                         "Используй команды:\n"
                         "/brick - Получить аналитический «кирпич»\n"
                         "/help - Помощь по боту")

@router.message(F.text == "/help")
async def help_command(message: Message):
    await message.answer("ℹ️ Доступные команды:\n"
                         "/start - Начало работы\n"
                         "/brick - Получить задание на анализ текста\n"
                         "/help - Эта справка")