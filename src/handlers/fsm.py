from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from loader import router_quiz, db, bot
from aiogram import types

class Quiz(StatesGroup):
    ask = State()
    answer = State()
    text = State()

# @router_quiz.callback_query(state = Quiz.ask)
# async def command_start(callback: types.CallbackQuery, state: FSMContext) -> None:
#     await state.set_state(Quiz.answer)
#     await state.update_data(text=callback.message.text)
#     print(f"callback.message.text = {callback.message.text}")