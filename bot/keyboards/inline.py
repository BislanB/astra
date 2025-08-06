from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_timer_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="⏱ Начать таймер (15 мин)", callback_data="start_timer")
    return builder.as_markup()