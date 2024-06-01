import discord
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # メッセージ内容のイベントを有効にする
intents.members = True  # オプション: メンバー関連のイベントを有効にする場合

bot = commands.Bot(command_prefix='!', intents=intents)
TOKEN = os.environ.get("TOKEN")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    # メッセージがBotからのものであれば無視する
    if message.author.bot:
        return

    await bot.process_commands(message)  # 他のコマンドを処理

    # 変換するURLを検出する
    if 'x.com' in message.content or 'twitter.com' in message.content:
        new_content = message.content
        if 'x.com' in message.content:
            new_content = new_content.replace('x.com', 'fxtwitter.com')
        if 'twitter.com' in message.content:
            new_content = new_content.replace('twitter.com', 'fxtwitter.com')

        # 送信者をメンションして変換したURLを送信する
        await message.channel.send(f'送信者: {message.author.mention}\n{new_content}')
        # 元のメッセージを削除する
        await message.delete()

# Botのトークンを設定する
bot.run(TOKEN)
