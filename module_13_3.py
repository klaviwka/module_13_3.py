from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    response_text = 'Привет! Я бот, помогающий твоему здоровью.'
    await message.answer(response_text)
    print(response_text)

@dp.message_handler()
async def all_messages(message: types.Message):
    response_text = 'Введите команду /start, чтобы начать общение.'
    await message.answer(response_text)  # Отправляем сообщение в чат
    print(response_text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
