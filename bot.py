import requests
import asyncio
from bs4 import BeautifulSoup
from telegram import Bot
import os

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

URL = "COLOQUE_AQUI_A_URL_DA_PROMOCAO"

bot = Bot(token=TOKEN)

ultima_promocao = ""

async def verificar_super_odd():
    global ultima_promocao

    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    texto = soup.get_text()

    if "Super Odd" in texto or "Odd Turbinada" in texto:
        if texto != ultima_promocao:
            ultima_promocao = texto

            await bot.send_message(
                chat_id=CHAT_ID,
                text=f"🔥 Nova Super Odd detectada!\n\n{URL}"
            )

async def main():
    while True:
        await verificar_super_odd()
        await asyncio.sleep(600)

asyncio.run(main())
