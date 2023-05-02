import requests
from main import bot
from telethon import events

@bot.on(events.ChatAction)
welcome_handler(event):
    if event.user_added and event.user_id == bot.uid:
        # Fetch a random quote from the ZenQuotes API
        response = requests.get('https://zenquotes.io/api/random')
        data = response.json()
        quote = data[0]['q']
        author = data[0]['a']
        #imageres = requests.get('https://api.unsplash.com/photos/random', headers={
            #'Authorization': 'Client-ID HH4vCat4VWlwVhtg9KDNP9imZf_PBuzz8k8yAZ9C8qc'
        #})
        #imgdata = response.json()
        #photo_url = imgdata['urls']['regular']

        # Send welcome message to group
        message = f"Thanks for adding me to this group! Here's a thought for you:\n\n**{quote}**\n— {author}"
         await event.respond(message)
