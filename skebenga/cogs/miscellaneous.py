from discord.ext import commands

class MiscellaneousCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot

    @commands.command(name='ping')
    async def ping(self, ctx: commands.Context):
        latency: int = round(self.bot.latency * 1000)
        await ctx.reply(content=f'Pong! `{latency}ms`')

async def setup(bot: commands.Bot):
    await bot.add_cog(MiscellaneousCog(bot))
