from main import bot
from telethon import events, Button

@bot.on(events.NewMessage(pattern='/broadcast'))
async def broadcast_handler(event):
    async with bot.conversation(event.chat_id) as conv:
        await conv.send_message('Please select a time interval (in minutes):', buttons=[
            [Button.inline('1', data='1'), Button.inline('5', data='5')],
            [Button.inline('10', data='10'), Button.inline('30', data='30')]
        ])
        time_interval = await conv.wait_event(events.CallbackQuery)
        await time_interval.answer()
        time_interval = int(time_interval.data.decode('utf-8'))
        
        await conv.send_message('Please select how many times to broadcast:', buttons=[
            [Button.inline('1', data='1'), Button.inline('2', data='2')],
            [Button.inline('3', data='3'), Button.inline('4', data='4')],
            [Button.inline('5', data='5')]
        ])
        num_broadcasts = await conv.wait_event(events.CallbackQuery)
        await num_broadcasts.answer()
        num_broadcasts = int(num_broadcasts.data.decode('utf-8'))
        
        await conv.send_message('Please reply with the message to broadcast:')
        message = await conv.get_response()
        
        for i in range(num_broadcasts):
            await bot.send_message(event.chat_id, message)
            await asyncio.sleep(time_interval * 60)
        
        # Send logs to private channel
        CHANNEL_LINK = 'REPLACE_WITH_YOUR_CHANNEL_LINK'
        await bot.send_message(CHANNEL_LINK, f'Name: {event.sender.first_name}\nUsername: {event.sender.username}\nMessage broadcasted: {message.text}\nNumber of times broadcasted: {num_broadcasts}\nTime interval: {time_interval} minutes')
