from main import AUTH_USER

@bot.on(events.NewMessage(incoming=True, pattern='/start'))
async def strt(event):
  name = event.sender.first_name
  user_id = event.sender_id
  user_name = event.sender.username #
  if event.sender_id != AUTH_USER:
    buttons = [
      [Button.inline("Redirect ⬇️", data='wigensjs')],
      [Button.url(name, url=f"t.me/{user_name}")]
    ]
    await bot.send_file(user_id, file='https://telegra.ph/file/1f72ad102d6194d02bb13.jpg', caption='**Hey there**\n\n__Use below button to get links and about section__\n\n**Have a nice day**')
    await bot.send_message(AUTH_USER, f'**New User Started the bot**\n\nUser id: {user_id}\nUser name: {user_name}', buttons=buttons)
  elif event.sender_id == AUTH_USER:
    await bot.send_file(user_id, file='https://telegra.ph/file/1f72ad102d6194d02bb13.jpg', caption='**Hello master!**\n\n__Use Below buttons to go through my menu__\n\n**Have a nice day**')
