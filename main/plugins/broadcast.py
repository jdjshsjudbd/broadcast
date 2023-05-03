import requests
import asyncio
from io import BytesIO
from main import bot
from main import AUTH_USER as AUTH_USERS

from telethon import events, Button

CHAT_TO_BROADCAST = [-1001710923802,
                     -1001802580312,
                     -1001479936325]

MEME_API_URL = 'https://api.imgflip.com/caption_image'

@bot.on(events.NewMessage(pattern='/broadcast'))
async def broadcast_handler(event):
    if event.sender_id not in AUTH_USERS: #h
        params = {
            'template_id': 61579,
            'username': 'theshashankk',
            'password': '@Shashank009',
            'text0': 'You are not authorized',
            'text1': 'to use this command'
        }
        response = requests.post(MEME_API_URL, params=params)
        data = response.json()
        if data['success']:
            meme_url = data['data']['url']
            await bot.send_message(event.chat_id, 'Wrong direction ❌', file=meme_url)
        return
    
    async with bot.conversation(event.chat_id) as conv:
        await conv.send_message('Please select a time interval (in minutes):', buttons=[
            [Button.inline('10', data='10'), Button.inline('30', data='30')],
            [Button.inline('1hrs ', data='60'), Button.inline('2hrs', data='120')],
            [Button.inline('3hrs', data='180'), Button.inline('4hrs', data='240')],
            [Button.inline('5hrs', data='300'), Button.inline('6hrs', data='360')],
            [Button.inline('7hrs', data='420'), Button.inline('8hrs', data='480')],
            [Button.inline('9hrs', data='540'), Button.inline('10hrs', data='600')],
            [Button.inline('11hrs', data='660'), Button.inline('12hrs', data='720')],

        ])
        time_interval = await conv.wait_event(events.CallbackQuery)
        await time_interval.answer()
        time_interval = int(time_interval.data.decode('utf-8'))
        
        await conv.send_message('Please select how many times to broadcast:', buttons=[
            [Button.inline(str(i), data=str(i)) for i in range(1, 11)],
            [Button.inline(str(i), data=str(i)) for i in range(11, 21)],
            [Button.inline(str(i), data=str(i)) for i in range(21, 31)],
            [Button.inline(str(i), data=str(i)) for i in range(31, 41)],
            [Button.inline(str(i), data=str(i)) for i in range(41, 51)]
        ])
        num_broadcasts = await conv.wait_event(events.CallbackQuery)
        await num_broadcasts.answer()
        num_broadcasts = int(num_broadcasts.data.decode('utf-8'))
        
        await conv.send_message('Please send me the text you want to broadcast:')
        message = await conv.get_response()
        
        # Manually define the list of group IDs
        groups = CHAT_TO_BROADCAST
        
        # Send broadcast message to all groups
        for i in range(num_broadcasts):
            for group in groups:
                await bot.send_message(group, message)
            await asyncio.sleep(time_interval * 60)
        
        # Send logs to private channel
        CHANNEL_ID = -1001969910526
        await bot.send_message(CHANNEL_ID, f'Name: {event.sender.first_name}\nUsername: {event.sender.username}\nMessage broadcasted: {message.text}\nNumber of times broadcasted: {num_broadcasts}\nTime interval: {time_interval} minutes')
