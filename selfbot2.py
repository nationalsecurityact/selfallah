import asyncio
import discord
import time
import subprocess
import requests
import string
import aiohttp
import io
import json
from discord.ext import commands
from discord.utils import get


prefix = "."
token = "MTE0OTgyODEyNjc2MzkwOTI4MA.GglU9o.7Xuv9_52Ndr2Ky-89YIrGyjTg_PDgtP6Os0vR4"
Lapsus = commands.Bot(description='Lapsus', command_prefix='.', self_bot=True)


Lapsus.lockgc = []
Lapsus.headers = {
    'authorization': token,
}

@Lapsus.event
async def lockloop():
    while True:
        if not Lapsus.lockgc == []:
            for gcid in Lapsus.lockgc:
                response = requests.put(f'https://discordapp.com/api/v8/channels/{gcid}/recipients/1337',headers=Lapsus.headers)
                if response.status_code == 429:
                    response_c = response.text
                    response_content = json.loads(response_c)
                    lockedsec = response_content.get('retry_after')
                else:
                    headers = {"Authorization": token}
                    for i in range(30):
                        response = requests.put(f'https://discordapp.com/api/v8/channels/{gcid}/recipients/1337',headers=Lapsus.headers)
        await asyncio.sleep(0.8)


@Lapsus.event
async def on_connect():
  print(f"Connected at {token} !")
  await lockloop()


@Lapsus.command()
async def antiveski(ctx, groupid):
    await ctx.send('__**Anti Veski Activé 🤓 !**__')
    Lapsus.lockgc.extend([groupid] * 1)

@Lapsus.command()
async def unlock(ctx, groupid=None):
    await ctx.send('__**Anti Veski Desactivé 🤓 !**__')
    if groupid:
        Lapsus.lockgc.pop(groupid)
        print(f'Unlocking {groupid} in 120 seconds Master !')
    else:
        Lapsus.lockgc.clear()
        print(f'Unlocked All Groups')


Lapsus.run(token, bot=False, reconnect=True)
