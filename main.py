from aiogram import Bot, Dispatcher, types
from environs import Env
from aiogram.filters import Command, CommandStart
import asyncio
import logging
import config
from aiogram.utils import markdown
from aiogram.enums import ParseMode, ChatAction

env = Env()
env.read_env()
bot_token = env.str("BOT_TOKEN")
admin = env.str("ADMIN")
ip = env.str("ip")

bot = Bot(token=bot_token)
dp = Dispatcher()

@dp.message(CommandStart())
async def handle_start(message: types.Message):
    url = "https://playerok.com/file-storage/images/1ee7e4b2-587f-6c60-f354-e1ea6b5bfa78.jpg?timestamp=1699457171"
    await message.answer(
        text=f"{markdown.hide_link(url)}Assalomu alaykum {markdown.hbold(message.from_user.full_name)}!",
        parse_mode=ParseMode.HTML,
    )

@dp.message(Command("help"))
async def handle_help(message: types.Message):
    text = "Menga xabar yuboring!"
    await message.answer(text=text)


@dp.message()
async def echo_message(message: types.Message):
    # await bot.send_message(
    #     chat_id=message.chat.id,
    #     text="Start processing...",
    # )
    # await bot.send_message(
    #     chat_id=message.chat.id,
    #     text="Detected message...",
    #     reply_to_message_id=message.message_id,
    # )

    await message.answer(
        text="bir necha soniya kuting...",
    )
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text="Yangi narsa 🙂")


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())