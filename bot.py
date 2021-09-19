#!/usr/bin/python
#!/usr/bin/home
# -*- coding: utf-8 -*-

R = '\033[31m'  # Red

from pyrogram.raw.functions.messages import ReportSpam
from pyrogram import Client, filters, idle
from pyrogram.errors import FloodWait
from pyrogram.types import ChatPermissions, Message, ReplyKeyboardMarkup
from time import sleep, perf_counter
from pyrogram.handlers import MessageHandler
import time, random, datetime, asyncio, sys, requests, os
from pathlib import Path

app = Client("my_account")

print(f""" 
{R}ZZZZZZZZZZZZZZZZZZZZᅠ
ᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠZZZᅠᅠᅠᅠᅠ
ᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠZZZᅠᅠᅠᅠᅠᅠᅠᅠ
ᅠᅠᅠᅠᅠᅠᅠᅠZZZᅠᅠᅠᅠᅠᅠᅠᅠᅠ
ᅠᅠᅠᅠᅠᅠZZZᅠᅠᅠᅠᅠᅠᅠᅠᅠ
ᅠᅠᅠᅠᅠᅠZZZZZZZZZZZZZZZZZ{R}
""")


# Информация

@app.on_message(filters.command("help", prefixes=".") & filters.me)
async def helpj(client: Client, message: Message):
  await message.edit(f"""
<b>UserZ Global v1.1.5</b>
<code>
𝚄𝚜𝚎𝚛𝙱𝚘𝚝
.help ➪ Вывод всех команд и их описание
.info ➪ Инфо
.scan <number> ➪ Сканировать номера по БД UserZ
.fnum <tgusername> ➪ Найти номер по юзернейму
.loading <текст> <проценты> ➪ Имитация загрузки
⌨︎Спам☯︎
.start ➪ спам с юзером zOut
.antifem ➪ спам для рейда фемгрупп
.spam <text> ➪ спам с вашим текстом
.stopsp ➪ Остановить спам

𝘜𝘴𝘦𝘳𝘡 𝘗𝘳𝘰𝘧𝘪𝘭𝘦
.profile ➪ Мой профиль
.prof_text <text> ➪ Текст профиля

</code>
""")

@app.on_message(filters.command("spam", prefixes=".") & filters.me)
async def spam (client, message):
  ktext = message.text.split(".spam ", maxsplit=1)[1]
  text = ktext
  global spam
  spam = 0
  await message.reply_text(text)
  while(spam < 1000000):
    try:
      await message.reply_text(text)
      spam += 1
    except FloodWait as e:
      sleep(e.x)

@app.on_message(filters.command("stopsp", prefixes=".") & filters.me)
async def stop(client, message):
  global spam
  await message.edit("Останавливаем спам...")
  spam += 1000000

@app.on_message(filters.command("info", prefixes="."))
def info(_, msg):
  msg.edit(f"""
🇿 ➪ UserZ v0.9.1 ➪ By <a href="https://t.me/zetdev">ZetDevSc</a>
""")

@app.on_message(filters.command("scan", prefixes=".") & filters.me )
async def slogin(client, message):
  usr = message.text.split(".scan ", maxsplit=1)[1]
  await message.reply_text(f"🔎 Поиск {usr} по базам данных UserZ")
  sleep(3)
  foundf = Path(f"db/{usr}")
  if foundf.is_file():
    with open(f"db/{usr}") as f:
      inf = f.read()
    await message.reply_text(inf)
  else:
    await message.reply_text(f"❌ Не найдено информации по юзернейму: {usr}")

@app.on_message(filters.command("fnum", prefixes=".") & filters.me )
async def slogin(client, message):
  usr = message.text.split(".fnum ", maxsplit=1)[1]
  await message.reply_text(f"🔎 Поиск номера у {usr} по базам данных UserZ")
  sleep(3)
  foundf = Path(f"number/{usr}")
  if foundf.is_file():
    with open(f"number/{usr}") as f:
      inf = f.read()
    await message.reply_text(inf)
  else:
    await message.reply_text(f"❌ Не найдено номера по юзернейму: {usr}")

@app.on_message(filters.command("profile", prefixes=".") & filters.me )
async def profile(client, message):
  await message.edit("📉 Получаем информацию о профиле UserZ")
  pathe = Path("profile/dat.txt")
  if pathe.is_file():
    with open("profile/dat.txt") as f:
       dta = f.read()
       await message.edit(f"⌨️ Информация о профиле:\n{dta}")
  else:
    await message.edit("⛔ Информация не заполнена. Заполнение командой .prof_text <text>")

@app.on_message(filters.command("prof_text", prefixes=".") & filters.me)
async def profile(client, message):
  txt = message.text.split(".prof_text ", maxsplit=1)[1]
  with open("profile/dat.txt", "w+") as f:
    f.write(txt)
    await message.edit("🖨️ Профиль заполнен!")

app.run()
