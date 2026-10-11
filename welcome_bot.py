import os
import discord
from discord.ext import commands

# ======================================
# PASTE YOUR DETAILS BELOW
# ======================================

BOT_TOKEN = os.getenv("BOT_TOKEN")

WELCOME_CHANNEL_ID = 1557136538398367816
GOODBYE_CHANNEL_ID = 1557136538398367817

# ======================================
# BOT SETUP — LEAVE THIS PART AS IT IS
# ======================================

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Bot is online: {bot.user}")
    print("Welcome and goodbye messages are enabled!")


@bot.event
async def on_member_join(member):
    channel = member.guild.get_channel(WELCOME_CHANNEL_ID)

    if channel is None:
        print("Welcome channel not found. Check its ID.")
        return

    embed = discord.Embed(
        title="🎉 Welcome to the server!",
        description=(
            f"Hey {member.mention}, welcome to **{member.guild.name}**!\n\n"
            "✨ We're glad you're here!\n"
            "📜 Please read the rules and have fun!"
        ),
        color=discord.Color.from_rgb(138, 43, 226)
    )

    embed.set_thumbnail(url=member.display_avatar.url)
    embed.set_footer(
        text=f"Member #{member.guild.member_count}"
    )

    await channel.send(
        content=f"👋 Welcome {member.mention}!",
        embed=embed
    )


@bot.event
async def on_member_remove(member):
    channel = member.guild.get_channel(GOODBYE_CHANNEL_ID)

    if channel is None:
        print("Goodbye channel not found. Check its ID.")
        return

    embed = discord.Embed(
        title="👋 Member left",
        description=(
            f"**{member.display_name}** has left the server.\n"
            "We hope to see you again!"
        ),
        color=discord.Color.orange()
    )

    embed.set_thumbnail(url=member.display_avatar.url)
    await channel.send(embed=embed)


bot.run(BOT_TOKEN)