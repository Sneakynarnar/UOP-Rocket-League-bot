
import interactions
from interactions import ActionRow, ButtonStyle
from interactions.utils.get import get
import os
from dotenv import load_dotenv

load_dotenv()
GUILD_ID = 1123417784886497302
WELCOME_CHANNEL = 1123423381132423219
LEAVE_CHANNEL = 1123428819852857345
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID =  1123417784886497302
#GUILD_ID = 819358157569916949

bot = interactions.Client(token=TOKEN,intents=interactions.Intents.ALL)
@bot.event
async def on_ready():
    print("running...")
    global guild
    guild = await get(bot, interactions.Guild, object_id=GUILD_ID)

@bot.event(name="on_guild_member_add")
async def on_guild_member_add(member):
    channel = await get(bot, interactions.Channel, object_id=WELCOME_CHANNEL)
    await channel.send(f"{member.mention} has joined the server!")

@bot.event(name="on_guild_member_remove")
async def on_guild_member_remove(member):
    channel = await get(bot, interactions.Channel, object_id=LEAVE_CHANNEL)
    
    await channel.send(f"**{member.username}** has left the server.") 
@bot.command(name="sendbuttons", scope=GUILD_ID,)
async def sendButtons(ctx: interactions.CommandContext):
    channel = ctx.channel

    
    buttons = [interactions.Button(style=interactions.ButtonStyle.SUCCESS, label="Spoons", custom_id="spoons"),
               interactions.Button(style=interactions.ButtonStyle.SUCCESS, label="2 mans ping", custom_id="2"),
               interactions.Button(style=interactions.ButtonStyle.SUCCESS, label="4 mans ping", custom_id="4m"),
                interactions.Button(style=interactions.ButtonStyle.SUCCESS, label="6 mans ping", custom_id="6")#

    ]
    await ctx.channel.send(content="Click to get the role!", components=[ActionRow(components=buttons)])
    await ctx.send("Buttons sent!", ephemeral=True)



@bot.event()
async def on_component(ctx):
  try:
    print(ctx.custom_id)
    if ctx.custom_id == "4":
        role = await guild.get_role(1123454868452016178)
    
    elif ctx.custom_id == "6":
        role = await guild.get_role(1123454904334307348)
    
    elif ctx.custom_id == "2":
        role = await guild.get_role(1123454808750293032)
    
    elif ctx.custom_id == "spoons":
        role = await guild.get_role(1123454958377906226)

    if role.id in ctx.author.roles:
        await ctx.author.remove_role(role=role, guild_id=GUILD_ID)
        
        await ctx.send(f"{role.name} role removed!", ephemeral=True) 
        return

    await ctx.author.add_role(role=role, guild_id=GUILD_ID)
    await ctx.send(f"{role.name} role added!", ephemeral=True)
  except Exception as e:
      await ctx.send(f"There was an error managing roles\n({e}) customId: {ctx.custom_id}", ephemeral=True)
    
bot.start()