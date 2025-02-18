import asyncio
import logging
import sys
import os

import wikipedia
wikipedia.set_lang('uz')
from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from token2 import BOT_TOKEN as token 
from button import *
bot = Bot(token="7873243450:AAG23zLElmKNaZUv0Fcd_SSJN15UOaHzfzc")
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message:Message):
    await message.answer("Salom botga hush kelibsiz. Bu bot siz hohlagan malumotni olib korsatadi!", reply_markup=mamlakat)

@dp.message(F.text.contains('Mamlakatni tanlang'))
async def orqaga(message: Message):
    await message.answer(text='Mamlakatni tanlang', reply_markup=mamlakat)




@dp.message(F.text =='Uzbakistan')
async def shirinlik1(message: Message):
    ax=wikipedia.summary(message.text)
    await message.answer(ax,reply_markup=mamlakat)

@dp.message(F.text =='Rassiya')
async def shirinlik1(message: Message):
    ax=wikipedia.summary(message.text)
    await message.answer(ax,reply_markup=mamlakat)

@dp.message(F.text =='Janubiy Amerika')
async def shirinlik1(message: Message):
    ax=wikipedia.summary(message.text)
    await message.answer(ax,reply_markup=mamlakat)


@dp.message(F.text =='Turkiya')
async def shirinlik1(message: Message):
    ax=wikipedia.summary(message.text)
    await message.answer(ax,reply_markup=mamlakat)

@dp.message(F.text =='Britanya')
async def shirinlik1(message: Message):
    ax=wikipedia.summary(message.text)
    await message.answer(ax,reply_markup=mamlakat)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
