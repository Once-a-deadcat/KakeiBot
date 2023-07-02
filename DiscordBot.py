import asyncio
import discord
import os
import json
from lib.logger import AzureBlobHandler
import logging
from discord import (
    Guild,
    app_commands,
    Interaction,
    SelectOption,
    TextInput,
    User,
    Member,
    Embed,
)
from discord.ui import Select, Button, View, UserSelect
from discord.ext import commands
from typing import List


# Configure logger settings
# CONNECTION_STRING = os.environ["CONNECTION_STRING"]
# CONTAINER_NAME = os.environ["CONTAINER_NAME"]

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
# formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# handler = AzureBlobHandler(
#     connection_string=CONNECTION_STRING,
#     container_name=CONTAINER_NAME,
#     blob_name_prefix="log",
# )
# handler.setFormatter(formatter)
# logger.addHandler(handler)

# インテントの生成
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents = discord.Intents.all()

# クライアントの生成
client = discord.Client(intents=intents, command_prefix="/")
tree = app_commands.CommandTree(client)


# discordと接続した時に呼ばれる
@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    await tree.sync()  # スラッシュコマンドを同期


# slash commandを受信した時に呼ばれる
@tree.command(name="hello", description="hello world")
async def list(interaction: discord.Interaction):
    message = "hello world"
    await interaction.response.send_message(message, ephemeral=False)


# メッセージを受信した時に呼ばれる
@client.event
async def on_message(message):
    # 自分のメッセージを無効
    if message.author == client.user:
        return

    if message.content.startswith("/hello"):
        await message.channel.send("hello world")


# クライアントの実行
token = os.environ["DISCORD_TOKEN"]
client.run(token)
