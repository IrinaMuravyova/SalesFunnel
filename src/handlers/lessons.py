from aiogram import Router, F
from aiogram import types
from aiogram.types import Message, URLInputFile, FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder
import datetime
from config import video_lessons, texts_for_lessons

router = Router()

# отправка видео урока
@router.callback_query(F.data == "lessons")
async def send_lesson(callback: types.CallbackQuery):
    for video in video_lessons:
        text = texts_for_lessons[video_lessons.index(video)]
        
        # Сюда будем помещать file_id отправленных файлов, чтобы потом ими воспользоваться
        # file_ids = []
        
        callback.message.delete

        # Отправка файла по ссылке
        # video_from_url = URLInputFile( "https://youtu.be/GavBpRVYilE")
        video_from_url = URLInputFile(video)
        
        callback.message.video
        result = await callback.message.answer_video(
            video= video_from_url,
            caption=" "
        )

        # Отправка файла из файловой системы
        # video_from_pc = FSInputFile("/Users/irinamuravyeva/Documents/TelegramBots_Python/SalesFunnel/src/db_api/VideoFiles/001 gr.mp4")
        # result = await callback.message.answer_video(
        #     video_from_pc,
        #     caption=" "
        # )
        
        # file_ids.append(result.video[-1].file_id)

        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text="Следующий урок",
            callback_data="lessons")
        )

        await callback.message.answer(
            text=text, 
            reply_markup=builder.as_markup()
            )
        await callback.answer()
