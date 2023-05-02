from main import bot, AUTH_USER
from telethon import events, Button, functions, types

@bot.on(events.NewMessage(incoming=True, pattern='/start'))
async def strt(event):
    name = event.sender.first_name
    user_id = event.sender_id
    user_name = event.sender.username 
    if event.sender_id != AUTH_USER:
        buttons = [
            [Button.inline("1 weeks", data="oneweek"), Button.url("Purchase now", "t.me/xdcomrade")],
            [Button.inline("2 weeks", data="twoweek"), Button.url("Purchase now", "t.me/xdcomrade")],
            [Button.inline("3 weeks", data="threeweeks"), Button.url("Purchase now", "t.me/xdcomrade")],
            [Button.inline("1 months", data="onemonths"), Button.url("Purchase now", "t.me/xdcomrade")]
        ]
        await bot.send_message(event.sender_id, "__Hey there__\n\nI'm ad bot, i can do promotion of your content, products aything you want to promote.\n\n**Use the below buttons to get subscription information ", buttons=buttons)
    else:
        await bot.send_message(event.sender_id, 'hello master')
