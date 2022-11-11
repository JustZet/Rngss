import os
import asyncio
from multiprocessing.pool import ThreadPool as Pool
import discord
from discord.ext import commands

BOT_TOKEN = 'OTg1MTM4NDczOTQ0MDg4NjA2.GdQnrU._kAC9tYWwYNejumg9keSs-xQPuJFIZroXRubzY'



intents = discord.Intents.default()
# intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)



@bot.event
async def on_ready():
	guild = discord.Object(id=980868518394335302) 
	# async with bot:

	bot.tree.copy_global_to(guild=guild)
	await bot.tree.sync(guild=guild)
	print(f'Logged in as {bot.user} (ID: {bot.user.id})')


@bot.tree.command()
async def hello(interaction: discord.Interaction):
    """Says hello!"""
    await interaction.response.send_message(f'Hi, {interaction.user.mention}')
 
async def load_cogs():
	for f in os.listdir("./lib/cogs"):
		if f.endswith(".py"):
			if f != "__init__.py":
				await bot.load_extension("cogs." + f[:-3])
   
async def main():
	await load_cogs()


	await bot.start(BOT_TOKEN)

if __name__ == "__main__":
	asyncio.run(main())


