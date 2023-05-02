from main import bot

from telethon import events, Button
from telethon.tl.functions.channels import GetDialogsRequest
from telethon.tl.types import Chat, Channel

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
        
        await conv.send_message('Please send me the message you want to broadcast:')
        message = await conv.get_response()
        
        # Get all groups where the bot is a member
        dialogs = await bot(GetDialogsRequest(
            offset_date=None,
            offset_id=0,
            offset_peer=InputPeerEmpty(),
            limit=100,
            hash=0
        ))
        groups = []
        for entity in dialogs.chats:
            if isinstance(entity, Chat) or (isinstance(entity, Channel) and entity.megagroup):
                groups.append(entity.id)
        
        # Send broadcast message to all groups
        for i in range(num_broadcasts):
            for group in groups:
                await bot.send_message(group, message)
            await asyncio.sleep(time_interval * 60)
        
        # Send logs to private channel
        CHANNEL_LINK = 'REPLACE_WITH_YOUR_CHANNEL_LINK'
        CHANNEL_ID = -1001969910526
        await bot.send_message(CHANNEL_ID, f'Name: {event.sender.first_name}\nUsername: {event.sender.username}\nMessage broadcasted: {message.text}\nNumber of times broadcasted: {num_broadcasts}\nTime interval: {time_interval} minutes')
