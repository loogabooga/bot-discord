import nextcord
from datetime import datetime
from nextcord.ext import commands

client = commands.Bot(command_prefix=commands.when_mentioned)

concurrent_time = datetime.now().strftime("%H:%M:%S")
file_object = open("log.txt", 'a', encoding="UTF-8")

silence = ["taiwan", "beijing", "tiananmen square", "june 4", "ytringsfrihet", "free", "tencent is bad", "tencent bad", "xi jingping bad"]


@client.event
async def on_ready():
    print('you in as {0.user}'.format(client))
    file_object.write('you in as {0.user}'.format(client) + " at " + concurrent_time + "\n")

@client.event
async def on_message(message):

    if message.author.bot:
        return

    gogn = str(message.author) + ": " + str(message.content)
    print(gogn)
    file_object.write(gogn + "\n")
    for banned_word in silence:
        if banned_word in message.content.lower():
            await message.delete()

    if "kirby" in message.content.lower():
        await message.channel.send("https://tenor.com/view/kirby-punch-stuffed-toy-beat-up-gif-17938642")
    if "punch" in message.content.lower():
        await message.channel.send("https://tenor.com/view/kirby-punch-stuffed-toy-beat-up-gif-17938642")

    if message.author.id == 900301678920736778:
        await message.delete()

    if "hongkong" in message.content.lower():
        await ctx.send.ban(user=message.author.id, delete_message_days=0)
        await message.delete()


client.run("funny toeken :)")
