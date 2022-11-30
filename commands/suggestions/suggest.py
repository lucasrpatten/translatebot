from discord.ext import commands
from datetime import datetime

class Suggestions(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command(aliases=['sug'])
    async def suggest(self, ctx, *, args):
        with open('commands//suggestions//suggestions.txt', 'a') as file:
            file.write(f'Author: {ctx.author}\tAuthorID: {ctx.author.id}\tTime: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}\tSuggestion: {args}\n')

        await ctx.channel.send(f"{ctx.author.mention} your suggestion has been submitted!")
def setup(bot):
    bot.add_cog(Suggestions(bot))