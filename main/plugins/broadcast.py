import asyncio
from io import BytesIO
from meme_generator import MemeGenerator
from main import bot
from main import AUTH_USER as AUTH_USERS

from telethon import events, Button

CHAT_TO_BROADCAST = [-1001710923802,
                     -1001802580312,
                     -1001479936325]

@bot.on(events.NewMessage(pattern='/broadcast'))
async def broadcast_handler(event):
    if event.sender_id not in AUTH_USERS:
        meme_url = meme.generate_meme('Wrong direction', 'You are not authorized to use this command', 'restricted')
        meme_data = requests.get(meme_url).content
        file = BytesIO(meme_data)
        await bot.send_file(event.chat_id, file, caption='Wrong direction ❌')
        return
    
    async with bot.conversation(event.chat_id) as conv:
        await conv.send_message('Please select a time interval (in minutes):', buttons=[
            [Button.inline('1', data='1'), Button.inline('5', data='5')],
            [Button.inline('10', data='10'), Button.inline('30', data='30')],
            [Button.inline('1hrs ', data='60'), Button.inline('1.5hrs', data='6')],
            [Button.inline('2hrs', data='120')],
        ])
        time_interval = await conv.wait_event(events.CallbackQuery)
        await time_interval.answer()
        time_interval = int(time_interval.data.decode('utf-8'))
        
        await conv.send_message('Please select how many times to broadcast:', buttons=[
            [Button.inline('1', data='1'), Button.inline('2', data='2')],
            [Button.inline('3', data='3'), Button.inline('4', data='4')],
            [Button.inline('5', data='5'), Button.inline('6', data='6')],
            [Button.inline('7', data='5'), Button.inline('8', data='6')],
            [Button.inline('9', data='5'), Button.inline('10', data='6')],
            [Button.inline('11', data='5'), Button.inline('12', data='6')],
        ])
        num_broadcasts = await conv.wait_event(events.CallbackQuery)
        await num_broadcasts.answer()
        num_broadcasts = int(num_broadcasts.data.decode('utf-8'))
        
        await conv.send_message('Please reply with the message to broadcast:')
        message = await conv.get_response()
        
        # Manually define the list of group IDs
        groups = CHAT_TO_BROADCAST
        
        # Send broadcast message to all groups
        for i in range(num_broadcasts):
            for group in groups:
                await bot.send_message(group, message)
            await asyncio.sleep(time_interval * 60)
        
        # Send logs to private channel
        CHANNEL_LINK = 'REPLACE_WITH_YOUR_CHANNEL_LINK'
        CHANNEL_ID = -1001969910526
        await bot.send_message(CHANNEL_ID, f'Name: {event.sender.first_name}\nUsername: {event.sender.username}\nMessage broadcasted: {message.text}\nNumber of times broadcasted: {num_broadcasts}\nTime interval: {time_interval} minutes')
