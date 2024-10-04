import time
import asyncio
from telegram import Bot

chat_id = '371643510'

bot = Bot('6868927671:AAG0DbZENsgd45ku_UragX8943NoVnPvH4s')

async def send_random_cat():
    url = f'https://cataas.com/cat?t=1'
    await bot.send_photo(chat_id, url)

if __name__ == "__main__":
    asyncio.run(send_random_cat())