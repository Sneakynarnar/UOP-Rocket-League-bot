
import interactions
from interactions import ActionRow, ButtonStyle
from interactions.utils.get import get
import os
from dotenv import load_dotenv

load_dotenv()
GUILD_ID = 1123417784886497302
WELCOME_CHANNEL = 1123423381132423219
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
    channel = await get(bot, interactions.Channel, object_id=1015061937727484055)
    
    await channel.send(f"**{member.username}** has left the server.") 
@bot.command(name="sendbuttons", scope=GUILD_ID)
async def sendButtons(ctx: interactions.CommandContext):
    channel = ctx.channel
    message = await channel.get_message(1063432347011260538)
    
    buttons = [interactions.Button(style=interactions.ButtonStyle.SUCCESS, label="Spoons", custom_id="spoons"),
               interactions.Button(style=interactions.ButtonStyle.SUCCESS, label="2 mans ping", custom_id="2mans"),
               interactions.Button(style=interactions.ButtonStyle.SUCCESS, label="4 mans ping", custom_id="4mans"),
                interactions.Button(style=interactions.ButtonStyle.SUCCESS, label="6 mans ping", custom_id="6mans")#

    ]
    await message.edit(content="Select your peak rank in competitive playlists", components=[ActionRow(components=buttons), ActionRow(components=buttons2)])



@bot.event()
async def on_component(ctx):
  try:
    if ctx.custom_id == "4mans":
        role = await guild.get_role(1060976014894829610)
    
    elif ctx.custom_id == "6mans":
        role = await guild.get_role(1060976010281103420)
    
    elif ctx.custom_id == "2mans":
        role = await guild.get_role(1060975587885318254)
    
    elif ctx.custom_id == "spoons":
        role = await guild.get_role(1060974547366588557)

        if role.id in ctx.author.roles:
            await ctx.author.remove_role(role=role, guild_id=819358157569916949)
            
            await ctx.send(f"{role.name} role removed!", ephemeral=True) 
            return

        await ctx.author.add_role(role=role, guild_id=819358157569916949)
        await ctx.send(f"{role.name} role applied!", ephemeral=True)
  except Exception as e:
      await ctx.send(f"There was an error managing roles\n({e}) customId: {ctx.custom_id}", ephemeral=True)
    
bot.start(TOKEN)