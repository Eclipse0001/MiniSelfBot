import discord
import datetime
import time
import colorama
colorama.init()
from colorama import Fore, Style
from discord.ext import commands

def error(text):
    print(f'{Fore.RED}[{time.strftime("%H:%M:%S")}] [ERROR] {text}{Style.RESET_ALL}')
def info(text):
    print(f'{Fore.GREEN}[{time.strftime("%H:%M:%S")}] [INFO] {text}{Style.RESET_ALL}')
def check(id):
    return id in [bot.user.id]#Allowed ids
def gcheck(ctx):return True#Метод удалён
def warn(text):
    print(f'{Fore.YELLOW}[{time.strftime("%H:%M:%S")}] [WARN] {text}{Style.RESET_ALL}')

token = "токен юзера "
deftext = "стандартный текст для команд статусов, будет вставлятся если не указать имя статуса"
prefix = "префикс"
bot = commands.Bot(command_prefix = prefix, self_bot=True, intents=discord.Intents.all(), help_command=None)

@bot.event
async def on_ready():
    info(f'Запущен на клиенте {bot.user}')
    info(f'Префикс бота {prefix}')
    if not bot.user.verified: warn('Аккаунт не верифицирован. Некоторые функции не будут работать или могут вызвать блокировку аккаунта!')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=deftext))

@bot.command()
async def musicstatus(ctx, *, text=deftext):
    if check(ctx.author.id):
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=text), status=discord.Status.dnd)
        await ctx.message.delete()
@bot.command()
async def gamestatus(ctx, *, text=deftext):
    if check(ctx.author.id):
        await bot.change_presence(activity=discord.Game(name=text), status=discord.Status.dnd)
        await ctx.message.delete()
@bot.command()
async def streamstatus(ctx, *, text=deftext):
    if check(ctx.author.id):
        await bot.change_presence(activity=discord.Streaming(name=text, url='https://www.twitch.tv/vadfonker'), status=discord.Status.dnd)
        await ctx.message.delete()
@bot.command()
async def watchingstatus(ctx, *, text=deftext):
    if check(ctx.author.id):
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=text), status=discord.Status.dnd)
        await ctx.message.delete()
@bot.command()
async def competingstatus(ctx, *, text=deftext):
    if check(ctx.author.id):
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name=text), status=discord.Status.dnd)
        await ctx.message.delete()         
@bot.command()
async def clearstatus(ctx):
    if check(ctx.author.id):
        await bot.change_presence(activity=None, status=discord.Status.dnd)
        await ctx.message.delete()

@bot.command()
async def s(ctx, *, text):
    await ctx.message.delete()
    await ctx.send(embed=discord.Embed(description=text, color=0xBBB9D9))
    
bot.run(token, bot=False)
