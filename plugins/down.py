import subprocess
import asyncio
import os,sys
import pyrogram
import time
from helper_funcs.getsize import *
from helper_funcs.gettype import typee
from helper_funcs.display_progress import humanbytes,progress_for_pyrogram
from helper_funcs.getvid import *
from PIL import Image
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
import random
import string,math
from datetime import datetime
import time
from pySmartDL import SmartDL
os.system('ls')
def grs():
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(8))
    return result_str
@pyrogram.Client.on_message(pyrogram.Filters.regex(pattern=".*http.*"))
async def down_load_media(client, message):
    start_time = time.time()
    if os.path.exists(str(message.chat.id)+'.jpg'):
    	thumbs = str(message.chat.id)+'.jpg'
    else:
    	thumbs = "defthumb.jpg"
    if not os.path.isdir('downloads'):
        os.makedirs('downloads')
    start_t = datetime.now()
    url = message.text
    kind = url[-3:]
    #try:
    	#await message.reply_document(url)
    	#return
   # except:
    mes = await message.reply_text("Tekshirilmoqda...")
    custom_file_name = os.path.basename(url)
    try:
    	downloader = SmartDL(url, 'downloads', progress_bar=True)
    	downloader.start(blocking=False)
    except Exception as e:
    	await mes.edit("Xatolik: Bunday manzil mavjud emas!")
    	return
    c_time = time.time()
    if downloader.isSuccessful():
        await mes.edit("Yuborilmoqda...")
        download_file_path = downloader.get_dest()
        width = int(getvid(download_file_path)[1])
        height = int(getvid(download_file_path)[2])
        send = await client.send_video(mes.chat.id,video=download_file_path,thumb=thumbs,width=width,height=height,progress=progress_for_pyrogram,progress_args=("Yuborilmoqda...",mes,start_time))
        if send:
        	await mes.edit("Yuborildi")
        	os.remove(download_file_path)
