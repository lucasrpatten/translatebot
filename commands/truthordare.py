from discord.ext import commands
from random import randint
import time

dares = ["Send a picture of yourself.", "Suck your big toe.", "Send audio or a video of you singing a song.", "Send a screenshot of your search history (no deleting anything).", "Change your profile pic to an anime girl for 24 hours.", 'DM a RANDOM server member "I love you"', "Send a thigh pic.", "Message the person at the bottom of your DM list", 'Message someone and say, "I know what you did" and then don\'t respond.', "Change your status to the message below this for a day.", "Do 20 pushups.", "Do 20 squats.", "Call someone in this server.", "Plank for a minute.", "Draw a self portrait of yourself and send it to the server (do it in a minute or less for an additional challenge).", "Take off a piece of clothing with your teeth.", "Smell your own feet for 30 seconds. Smell deeply.", "Do 50 jumping jacks.", "Send someone in the server a bad pickup line (preferrably someone of the gender you are attracted to, if possible)", "Use only your elbows to set your discord status, and keep it that way", "Stop blinking for 30 seconds."]

truths = ["If you could trade lives with any person you know for a day, who would it be?" ,"What’s something you only do when you’re alone?" ,"If you had to move to a different country tomorrow, where would you go?" ,"If you could travel to the past and meet one person, who would it be?" ,"If you had to get a tattoo today, what would it be?" ,"What’s the last thing you Googled?" ,"What is your biggest insecurity?" ,"If you had to change your name, what would your new first name be?" ,"What animal do you think you most look like?", "What’s your biggest regret?" ,"If a genie granted you three wishes, what would you ask for?" ,"If you could be invisible, what’s the first thing you would do?", "What’s one thing you wish you could change about yourself?", "What is your favorite part of your body?", "What's the most embarrasing song you unironically listen to?" ,"Who is your celebrity crush", "Whats the first thing you'd do as the opposite gender?", "What’s the longest you’ve gone without showering?", "Who is your least favorite person in the server?", "What’s one thing you’d do if you knew there no consequences?", "What's the worst thing you've done at school?", "What is your biggest fear?", "Who do you think you're the most of a dissapointment to.", "What's something you're glad your mom doesn't know about you?", "What's your most embarassing moment?", "What person in this server would you most like to kiss?", "What's the worst thing thats ever happened to you?", "If you could be anywhere in the world, where would you be?", "When was the last time you cried, and why?", "Do you miss anyone? If so who?", "What color is your underwear you are currently wearing?", "What is your worst habit?", "If you were homosexual, who in this server (of the same gender) would you most want to kiss? If you are already homosexual, who of the opposite gender. If you are bi or pan, pick someone of the opposite gender of your current or last crush. If you are aromantic I don't care who tf you pick.", "If you had to choose between going naked or having your thoughts appear in thought bubbles above your head for everyone to read, which would you choose?", "If you could be invisible, who would you spy on?", "If you could go back in time in erase one thing you said or did, what would it be?", "What is your bra/pp size?", "What would your perfect partner be/look like?", "What's one thing you do that you don't want anyone to know about?", "What's the most useless piece of knowledge you know?", "If you could change one thing about your body, what would it be?", "What would you do with a million dollars?", "What is the stupidest thing you have ever done?", "What do you think about cheerleaders?", "If you could date anybody in the world, who would it be?", "If you could have anyone in this server be your slave, who would it be and what would you make them do?"]

class TruthOrDare(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases=['truthordare'])
    async def tod(self, ctx, person='nonelol'):
        if person == 'nonelol':
            person = int(ctx.message.author.id)
        else:
            person = int(person.replace('<', '').replace('@', '').replace('!', '').replace('>', ''))
        time.sleep(0.04)
        await ctx.message.add_reaction('🇹')
        time.sleep(0.04)
        await ctx.message.add_reaction('🇩')
        
        def check(reaction, user):
            if user.id == person and str(reaction.emoji) in ["🇹"]:
                return 'True'
            elif user.id == person and str(reaction.emoji) in ["🇩"]:
                return 'False'
            else:
                pass
        confirmation = await self.bot.wait_for("reaction_add",timeout=60.0, check=check)
        confirmation = str(confirmation[0])
        if confirmation == "🇹":
            
            rannum = randint(0, len(truths) - 1)
            await ctx.reply(truths[rannum], mention_author=False)
        elif confirmation == "🇩":
            
            rannum = randint(0, len(dares)-1)
            await ctx.reply(dares[rannum], mention_author=False)
        else:
            await ctx.channel.send('An error occured')

def setup(bot):
    bot.add_cog(TruthOrDare(bot))