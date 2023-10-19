from aiogram import Router, F
from aiogram import types
from aiogram.types import Message, URLInputFile, FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

# отправка видео первого урока
@router.callback_query(F.data == "lessons")
async def send_lesson(callback: types.CallbackQuery):
    # Сюда будем помещать file_id отправленных файлов, чтобы потом ими воспользоваться
    file_ids = []
    # Здесь будем хранить text к видео к урокам
    text_messages = ["Первое видео - это база! Основа основ - грамматика! Она помогает вам не бездумно заучивать фразы, а учиться строить их самостоятельно! Но только на примере и практике можно выучить любые правила! Успехов в обучении! "]
    
    callback.message.delete

    # # Отправка файла по ссылке
    # video_from_url = URLInputFile( "https://youtu.be/GavBpRVYilE")
    
    # callback.message.video
    # result = await callback.message.answer_video(
    #     video= video_from_url,
    #     caption=" "#"Урок к изучению"
    # )

    # Отправка файла из файловой системы
    video_from_pc = FSInputFile("/Users/irinamuravyeva/Documents/TelegramBots_Python/SalesFunnel/src/db_api/VideoFiles/001 gr.mp4")
    result = await callback.message.answer_video(
        video_from_pc,
        caption=" "
    )
    
    # file_ids.append(result.video[-1].file_id)

    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Следующий урок",
        callback_data="lessons")
    )

    await callback.message.answer(
        text=text_messages[0],
        reply_markup=builder.as_markup()
        )
    await callback.answer()
