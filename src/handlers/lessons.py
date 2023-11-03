from aiogram import F
from aiogram import types
from aiogram.types import URLInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder
from .reminders import check_status_and_remind
from config import video_lessons, texts_for_lessons
from loader import router_lessons, db, bot

# отправка видео урока
@router_lessons.callback_query(F.data == "lessons")
async def send_lesson(callback: types.CallbackQuery):

    for video in video_lessons:
        db.set_video_id(video_id=video_lessons.index(video), id = callback.from_user.id)
        # callback.message.delete

        # Отправка файла по ссылке
        video_from_url = URLInputFile(video)
        callback.message.video
        await callback.message.answer_video(
            video= video_from_url,
            caption=" "
            )
        
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text="Следующий урок",
            callback_data="next_lesson")
        )
        
        text = texts_for_lessons[video_lessons.index(video)]
        await callback.message.answer(
            text=text, 
            reply_markup=builder.as_markup()
            )
        await callback.answer()

        await check_status_and_remind(callback)