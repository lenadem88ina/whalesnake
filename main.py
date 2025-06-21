import os
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
from game import WhaleGame

load_dotenv()
API_TOKEN = os.getenv("TELEGRAM_TOKEN")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

games = {}

def get_controls():
    kb = InlineKeyboardMarkup(row_width=2)
    for emoji in ["⬆️", "⬇️", "⬅️", "➡️"]:
        kb.add(InlineKeyboardButton(emoji, callback_data=emoji))
    return kb

@dp.message_handler(commands=['start'])
async def cmd_start(msg: types.Message):
    game = WhaleGame()
    games[msg.from_user.id] = game
    await msg.answer(game.render(), reply_markup=get_controls())

@dp.callback_query_handler(lambda c: c.data in ["⬆️","⬇️","⬅️","➡️"])
async def on_move(cq: types.CallbackQuery):
    user_id = cq.from_user.id
    game = games.get(user_id)
    if not game:
        game = WhaleGame()
        games[user_id] = game
    game.move(cq.data)
    await cq.message.edit_text(game.render(), reply_markup=get_controls())
    await cq.answer()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
