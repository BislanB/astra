from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from bot.keyboards.inline import get_timer_keyboard
from bot.services.brick_service import BrickService

router = Router()
brick_service = BrickService()

@router.message(F.text == "/brick")
async def start_brick(message: Message, state: FSMContext):
    # Здесь будет логика выдачи кирпича
    brick_text = "Пример текста для анализа. Это тестовый «кирпич»."
    
    await state.update_data(brick_text=brick_text)
    await message.answer(
        f"🧱 Вам выдан текст для анализа:\n\n{brick_text}\n\n"
        "⏱ У вас 15 минут на выполнение задания!",
        reply_markup=get_timer_keyboard()
    )

@router.callback_query(F.data == "start_timer")
async def start_timer(callback: CallbackQuery, state: FSMContext):
    await callback.answer("Таймер запущен! У вас 15 минут.")
    # Здесь будет логика запуска таймера
    # В реальном приложении нужно сохранить время начала