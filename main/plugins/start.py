from main import bot, AUTH_USER
from telethon import events, Button, types

MSG = """
Hey there👋, Welcome!

📕If you want to purchase the subscription of ADs bot, Read this :

⚠️Details:
✓  Per 15/20/30 mins
✓  It broadcasts 50 times per day 
✓ More than 200 connected marketplaces 

⚠️PRICING:
🚥For 1 week: 20$
🚥For 2 weeks: 40$
🚥For 1 month: 70$

"""
IMG = "https://telegra.ph/file/acc9e663136c4e2d688dd.jpg" #thumbnail

@bot.on(events.NewMessage(incoming=True, pattern='/start'))
async def start_handler(event):
    name = event.sender.first_name
    user_id = event.sender_id
    user_name = event.sender.username 
    if user_id != AUTH_USER:
        buttons = [
            [Button.inline('Contact now⬇️', data='sdhgsd')],
            [Button.url("IMMORTAL", url="t.me/maybeimmortal")],
        ]
        await bot.send_file(event.chat_id, file=IMG, caption=MSG, buttons=buttons)
        #kk = types.ReplyKeyboardMarkup(buttons, one_time_keyboard=True)
        #await bot.send_message(event.chat_id, "What are you waiting for, Do your promotion!!", reply_markup=kk)
    else:
        #kk = types.ReplyKeyboardMarkup(buttons, one_time_keyboard=True)
        await bot.send_message(event.chat_id, 'hello master')
