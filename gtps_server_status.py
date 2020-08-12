#############################
#####GTPS SERVER STATUS######
#############################
#############################

import os
try:
	import discord, datetime, time, threading
	from discord.ext import commands
	from datetime import datetime
except:
	os.system('pip install discord')

client = commands.Bot(command_prefix='/')
@client.event
async def on_ready():
	print('Bot is Online')
@client.command()
async def s(ctx):
	if ctx.author.id == YOUR ACCOUNT ID:
		player = open('online.txt').readlines()
		tm = datetime.now()
		tim = tm.strftime('%H:%M %p')
		embed = discord.Embed(color=0x00ff00, title='SERVER-STATUS')
		embed.set_thumbnail(url=ctx.guild.icon_url)
		embed.add_field(name='STATUS:', value='UP')
		embed.add_field(name='Players Online:', value=player[0])
		embed.set_footer(text='LAST UPDATE TODAY AT ' + tim + '')
		text = await ctx.send(embed=embed)
		while True:
			players = open('online.txt').readlines()
			listworld = len(os.listdir('worlds'))
			listplayers = len(os.listdir('players'))
			newembed = discord.Embed(color=0x00ff00, title='SERVER-STATUS')
			newembed.set_thumbnail(url=ctx.guild.icon_url)
			newembed.add_field(name='STATUS:', value='UP')
			newembed.add_field(name='Players Online:', value=players[0])
			newembed.add_field(name='Total Players Create', value=listplayers)
			newembed.add_field(name='Total Worlds Create', value=listword)
			newembed.set_footer(text='LAST UPDATE TODAY AT ' + tim + '')
			#start editing
			edit = threading.Thread(target = await text.edit(embed=newembed))
			edit.start()
			time.sleep(2)
			#auto edit after 2 sec
	else:
		await ctx.send('Oops! You dont have permission do that')
		
client.run('Your bot token')
	else:
		await ctx.send('Oops! You dont have permission do that')
		
client.run('YOUR DISCORD BOT TOKEN')
