from discord.ext import commands
from random import randint

class AIGeneratedImages(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def anime(self, ctx, creativity = 8):
        creativity = float(f'{(creativity + 2) / 10:.2f}')
        if creativity < 0.3:
            creativity = 0.3
        if creativity > 2.0:
            creativity = 2.0
        randomnum = randint(0, 99999)
        if randomnum <= 9999:
            if randomnum <= 999:
                if randomnum <= 99:
                    if randomnum <= 9:
                        randomnum = "0000" + str(randomnum)
                    randomnum = "000" + str(randomnum)
                randomnum = "00" + str(randomnum)
            randomnum = "0" + str(randomnum)
        await ctx.channel.send(f'https://thisanimedoesnotexist.ai/results/psi-{creativity}/seed{randomnum}.png')

    @commands.command()
    async def fursona(self, ctx):
        randomnum = randint(0, 99999)
        if randomnum <= 9999:
            if randomnum <= 999:
                if randomnum <= 99:
                    if randomnum <= 9:
                        randomnum = "0000" + str(randomnum)
                    randomnum = "000" + str(randomnum)
                randomnum = "00" + str(randomnum)
            randomnum = "0" + str(randomnum)
        await ctx.channel.send(f'https://thisfursonadoesnotexist.com/v2/jpgs-2x/seed{randomnum}.jpg')

    @commands.command()
    async def pony(self, ctx):
        randomnum = randint(0, 99999)
        if randomnum <= 9999:
            if randomnum <= 999:
                if randomnum <= 99:
                    if randomnum <= 9:
                        randomnum = "0000" + str(randomnum)
                    randomnum = "000" + str(randomnum)
                randomnum = "00" + str(randomnum)
            randomnum = "0" + str(randomnum)

        await ctx.channel.send(f'https://thisponydoesnotexist.net/v1/w2x-redo/jpgs/seed{randomnum}.jpg')

def setup(bot):
    bot.add_cog(AIGeneratedImages(bot))