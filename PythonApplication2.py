# インストールした discord.py を読み込む
import discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'NjM3NzQ4ODQzNDUwMjA0MjEx.Xdwp5A.HUnf1uVXFIxdCs4dOk2ajhFG0xc'

#予約格納
YOYAKU_1 = []
YOYAKU_2 = []
YOYAKU_3 = []
YOYAKU_4 = []
YOYAKU_5 = []

DAMAGE_1 = []
DAMAGE_2 = []
DAMAGE_3 = []
DAMAGE_4 = []
DAMAGE_5 = []

BOSS_NAME = ["ボス１","ボス２","ボス３","ボス４","ボス５"]

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content.split(',')[0] == '！予約':
        if message.content.split(',')[1] == BOSS_NAME[0]:
            if len(message.content.split(',')) <= 2:
                #DAMAGE_1.append(0)
                await message.channel.send("aa")
            else:
                DAMAGE_1.append(ulong.Parse(message.Content.split(',')[2]))
                await message.channel.send("aa")


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)