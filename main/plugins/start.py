from main import bot, AUTH_USER
from telethon import events, Button, functions, types

@bot.on(events.NewMessage(incoming=True, pattern='/start'))
async def strt(event):
    name = event.sender.first_name
    user_id = event.sender_id
    user_name = event.sender.username 
    if event.sender_id != AUTH_USER:
        buttons = [
            [Button.inline("Redirect ⬇️", data='wigensjs')],
            [Button.url(name, url=f"t.me/{user_name}")]
        ]
        await bot.send_file(user_id, file='https://telegra.ph/file/1f72ad102d6194d02bb13.jpg', caption='**Hey there**\n\n__Contact @xD_Comrade to purchase subscription of AD Bot__\n\n**Have a nice day**')
        await bot(functions.messages.SendInlineBotResultRequest(
            user_id,
            query_id='bot-started',
            result_id='some-result-id',
            message=f'**New User Started the bot**\n\nUser id: {user_id}\nUser name: {user_name}',
            reply_markup=types.InlineKeyboardMarkup(buttons)
        ))
    elif event.sender_id == AUTH_USER:
        await bot.send_file(user_id, file='https://telegra.ph/file/1f72ad102d6194d02bb13.jpg', caption='**Hello master!**\n\n__Use Below buttons to go through my menu__\n\n**Have a nice day**')
