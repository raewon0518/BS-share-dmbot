
# 봉순#4888 : MASS DM BOT SOURCE
# 오픈소스 이용하여 제작되었습니다


import discord
import asyncio
import datetime

client = discord.Client()

@client.event
async def on_ready():
    print("봇이 정상적으로 실행되었습니다.")
    game = discord.Game('계정거래방 운영중')
    await client.change_presence(status=discord.Status.online, activity=game)

#/dm {할말}로 전체DM 전송
@client.event
async def on_message(message):
    if message.content.startswith('/dm'):
        for i in message.guild.members:
            if i.bot == True:
                pass
            else:
                try:
                    msg = message.content[4:]
                    if message.author.id == ★자신의 디스코드ID를 적어주세요(퍼미션):
                        embed = discord.Embed(colour=0x1DDB16, timestamp=message.created_at, title="계정거래방 KR")
                        embed.add_field(name="DM 봇", value=msg, inline=True)
                        embed.set_footer(text=f"discord.gg/이 메시지는 게정거래방 에서 발송 했습니다")
                        await i.send(embed=embed)
                except:
                    pass


client.run('NzMxNTA3MTA3MTE4OTcyOTY5.XwnD1A.hijlo7wi5GW7CMSf4nWwpcgofhI')
