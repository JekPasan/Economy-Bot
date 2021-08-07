import discord
import time
from coin import Coin

client = discord.Client()
token = ""
with open("token.txt") as token_file:
    token = token_file.read() # no access for you

help_embed = discord.Embed(
    title="Help",
    description="",
    colour=discord.Colour.green()
)
help_embed = help_embed.add_field(
    name=".info <coin name>",
    value="gives you the general info of the coin you're searching for",
    inline=False
)
help_embed = help_embed.add_field(
    name=".coin-to-usd <coin name> <ammount to convert>",
    value="gives you how much a certain ammount of a specific coin is worth in United States Dollars",
    inline=False
)
help_embed = help_embed.add_field(
    name=".usd-to-coin <coin name> <ammount to convert>",
    value="gives you how much a certain ammount of Unites States Dollars is worth in a specific coin",
    inline=False
)
help_embed = help_embed.add_field(
    name=".buy <coin name> <ammount you want to buy>",
    value="buy a certain ammount of a specific coin",
    inline=False
)

charlie_coin = Coin(
    "Charlie Coin",
    1000000.0,
    "From the creators of Doge Coin, we present to you **Charlie Coin**.",
    discord.Colour.green(),
    "CC",
    "https://cdn.discordapp.com/attachments/729395729310941227/873487347243692112/charlie_coin.png"
)

bitcoin = Coin(
    "Bitcoin",
    0.000023,
    "Creator: unknown, Origins: unknown\nAll we know is that you can buy a house with one, the one and only\n**BIIIIIITCOOOOOOIIIIN**",
    discord.Colour.gold(),
    "BTC",
    "https://cdn.discordapp.com/attachments/729395729310941227/873557053531111434/unknown.png"
)

async def conversatie(msg):
    if msg.content.lower() == "am depresie clinica":
        await msg.channel.send("si ce-o sa faci? o sa plangi? o sa te pisi si-o sa te caci?")
    
    if msg.content.lower() == "ce vrei ma tu":
        await msg.channel.send("pe ma-ta")
    
    if msg.content.lower() == "hai ma hai s-o dam daca esti smecher":
        await msg.channel.send("hai ma")
    
    if msg.content.lower() == "pai hai ma ce facem ti-e frica?":
        await msg.channel.send("!ban @You#4444")
    
    if msg.content.lower() == "ha ha ce prost":
        await msg.channel.send("prost esti tu c-ai luat 7 la testul cu triunghiuri la mate")
    
    if msg.content.lower() == "ma-ta":
        await msg.channel.send("ca tot veni vorba de mame spunei a ta sa puna muzica aia sexy pe fundal de-mi place mie atunci cand vin azi seara")
    
    if msg.content.lower() == "good bot":
        await msg.channel.send("\"good\" e ma-ta-n pat")
    
    if msg.content.lower() == "ok asta-i ultima picatura":
        await msg.channel.send("asta a zis si ma-ta ieri")

@client.event
async def on_ready():
    print(f"up and running as {client.user}")

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    
    if msg.content.startswith(".help"):
        await msg.channel.send(embed=help_embed)

    if msg.content.startswith(".ping"):
        print(msg.content)
        await msg.channel.send("pong")
    
    if msg.content.startswith(".marco"):
        await msg.channel.send("polo")
    
    if msg.content.startswith(".info"):
        if "charlie coin" in msg.content.lower():
            await msg.channel.send(embed=charlie_coin.embed)
        if "bitcoin" in msg.content.lower():
            await msg.channel.send(embed=bitcoin.embed)
    
    if msg.content.startswith(".coin-to-usd"):
        words = msg.content.split(" ")
        if "charlie coin" in msg.content.lower():
            await msg.channel.send(embed=charlie_coin.convert_to_usd(float(words[3])))
    if msg.content.startswith(".usd-to-coin"):
        words = msg.content.split(" ")
        if "charlie coin" in msg.content.lower():
            await msg.channel.send(embed=charlie_coin.convert_to_coin(float(words[3])))
    
    if msg.content.startswith(".buy"):
        words=msg.content.split(" ")
        if "charlie coin" in msg.content.lower():
            await msg.channel.send(embed=charlie_coin.buy(float(words[3])))
    
    await conversatie(msg)

client.run(token)
