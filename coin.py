import discord

class Coin:
    def __init__(self, name, value, desc, colour, short, img):
        self.name = name
        self.desc = desc
        self.colour = colour
        self.value = value
        self.short = short
        self.img = img
        self.embed = discord.Embed(title=name, description=desc, colour=colour)
        self.embed = self.embed.add_field(
            name=f"Value from {self.short} to USD", value=f"{str(value)}**{self.short}** = 1**USD**\n(the lower the number of coins needed for 1USD the better)"
        )
        self.embed = self.embed.set_image(url=self.img)
    
    def convert_to_usd(self, ammount):
        tmp_embed = discord.Embed(
            title=f"{ammount}{self.short} to USD",
            description=f"{ammount}**{self.short}** = {ammount/self.value}**USD**",
            colour=self.colour
        )
        return tmp_embed
    
    def convert_to_coin(self, ammount):
        tmp_embed = discord.Embed(
            title=f"{ammount}USD to {self.short}",
            description=f"{ammount}**USD** = {ammount*self.value}**{self.short}**",
            colour=self.colour
        )
        return tmp_embed
    
    def buy(self, ammount):
        usd = ammount/self.value
        self.value -= usd
        tmp_embed = discord.Embed(
            title="transaction approved",
            description=f"you have succesfully bought {ammount}**{self.short}**(worth {usd}**USD**)\nthe new value of the coin is {self.value}**{self.short}** = 1**USD**",
            colour=self.colour
        )
        self.embed.clear_fields()
        self.embed = self.embed.add_field(
            name=f"Value from {self.short} to USD", value=f"{self.value}**{self.short}** = 1**USD**\n(the lower the better)"
        )
        self.embed = self.embed.set_image(url=self.img)
        return tmp_embed