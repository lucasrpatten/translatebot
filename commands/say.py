from discord.ext import commands

class Webhook(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def say(self, ctx, *, args):
        g = await ctx.channel.create_webhook(name="mywebhook")
        print(g.url)
        print(args)
        await g.send(content=args, wait=True, username=ctx.author.name,avatar_url=ctx.author.avatar_url,tts=False,file=None,files=None,embed=None,embeds=None)
        await g.id.delete()

def setup(bot):
    bot.add_cog(Webhook(bot))