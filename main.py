import discord
import time, asyncio, os
from configparser import ConfigParser
from pystyle import *
import colorama
from colorama import Fore, Style
import ctypes
from discord import webhook
from datetime import datetime
now = datetime.now()
time_rn = now.strftime("%H:%M:%S")

#################### CONFIG #########################


role = 1265339454080684123
channelid = 1261129313957187597


######################################################



def read_config():
    config = ConfigParser()
    config.read('Data/config.ini')
    return config

config_data = read_config()

TOKEN = config_data.get('BotConfig', 'TOKEN')

intents = discord.Intents.all()

bot = discord.Bot(command_prefix='!', intents=intents, help_command=None, )

@bot.event
async def on_ready():
  print()


@bot.slash_command(name="verify", description="Verify to the server!")
async def verify(ctx: discord.ApplicationContext):
    if role not in [y.id for y in ctx.user.roles]:
      await ctx.respond(embed = discord.Embed(title = "Verified.", description = "> You have been succesfully verified!"))
      await ctx.user.add_roles(ctx.user.guild.get_role(role))
      print(f"{ctx.user} just verified!")
      with open("Data/verified.txt", "w") as verify:
        verify.write(f"{ctx.user} verified ~ {time_rn}" + '\n')
      time.sleep(1.5)
      await ctx.channel.purge(limit=1)

    else:
       await ctx.respond(embed = discord.Embed(title = "Already Verified.", description = "> You are already verified!"))
       time.sleep(1.5)
       await ctx.channel.purge(limit=1)


@bot.event
async def on_message(message):
  if message.author == bot.user:
    return

  if message.channel.id == channelid:
      await asyncio.sleep(0.1)
      await message.delete()

@bot.slash_command(name="send", description="Send's the verification message!")
async def admir(ctx: discord.ApplicationContext):
    await ctx.respond(embed = discord.Embed(title = "Done.", description = "Sent message below>"), ephemeral=True)
    await ctx.send_followup(embed = discord.Embed(title = "AxLeaks Verification.", description = "> Use the </verify:0> command to verify to this server! "))
logo = f"""

{Fore.CYAN}██╗   ██╗███████╗██████╗ ██╗███████╗██╗   ██╗    ██████╗  ██████╗ ████████╗
{Fore.WHITE}██║   ██║██╔════╝██╔══██╗██║██╔════╝╚██╗ ██╔╝    ██╔══██╗██╔═══██╗╚══██╔══╝
{Fore.BLUE}██║   ██║█████╗  ██████╔╝██║█████╗   ╚████╔╝     ██████╔╝██║   ██║   ██║   
{Fore.WHITE}╚██╗ ██╔╝██╔══╝  ██╔══██╗██║██╔══╝    ╚██╔╝      ██╔══██╗██║   ██║   ██║   
{Fore.CYAN} ╚████╔╝ ███████╗██║  ██║██║██║        ██║       ██████╔╝╚██████╔╝   ██║   
{Fore.BLUE}  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝       ╚═════╝  ╚═════╝    ╚═╝   
                                                    Dev: @.admir.

{Fore.BLUE}  [ ~ ]  {Fore.RESET}{Fore.WHITE}GitHub: https://github.com/justadmir {Fore.RESET}  
{Fore.BLUE}  [ ~ ]  {Fore.RESET}{Fore.WHITE}Discord: https://discord.gg/dMF32wY3x9 {Fore.RESET} 
{Fore.BLUE}  [ ~ ]  {Fore.RESET}{Fore.WHITE}Replit: https://replit.com/@justadmir {Fore.RESET}      
\n\n
\n\n
{Fore.WHITE}  [{Fore.GREEN} +{Fore.WHITE} ]  Logged in as {bot.user}.{Fore.RESET}
{Fore.WHITE}  [{Fore.GREEN} +{Fore.WHITE} ]  Synced commands.{Fore.RESET}
                                                                    
"""

os.system("cls")
ctypes.windll.kernel32.SetConsoleTitleA("Verification Bot • Made with ♥ by Admir • Version: 1.0")
print(logo)
bot.sync_commands
bot.run(TOKEN)


