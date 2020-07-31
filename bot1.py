import discord

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("Phantom Forces")
    await client.change_presence(status=discord.Status.online, activity = game)


@client.event
async def on_message(message):
    if message.content.startswith("카람봇!"):
       await message.channel.send("뭐")
    if message.content.startswith("카람봇?"):
       await message.channel.send("왜불렀냐")


client.run("NzExNzQxNjY5NDA1NDkxMjQy.XsHbFQ.l_SzUlbDUlmmXB4IqV4FO4jslaI")