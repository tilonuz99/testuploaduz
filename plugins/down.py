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
    	downloader = SmartDL(url, 'downloads', progress_bar=False)
    	downloader.start(blocking=False)
    except Exception as e:
    	await mes.edit("Xatolik: Bunday manzil mavjud emas!")
    	return
    c_time = time.time()
    while not downloader.isFinished():
        total_length = downloader.filesize if downloader.filesize else None
        await mes.edit("Yuklanmoqda: %d%%" % (downloader.get_progress_bar()))
        await asyncio.sleep(2)
    if downloader.isFinished():
        print(downloader.isSuccessful())
        await mes.edit("Yuborilmoqda...")
        download_file_path = downloader.get_dest()
        if typee(str(kind)) == "v":
        	try:
        		duration = int(get_sec(getvid(custom_file_name)[0]))
        		width = int(getvid(custom_file_name)[1])
        		height = int(getvid(custom_file_name)[2])
        	except Exception as e:
        		mes = await mes.edit("Xatolik: Bunday manzil mavjud emas."+str(e))
        		print(e)
        		return
        	send = await client.send_video(mes.chat.id,video=download_file_path,thumb=thumbs,duration=duration,width=width,height=height,progress=progress_for_pyrogram,progress_args=("Yuborilmoqda...",mes,start_time))
        else:
        	mes = await mes.edit("Xatolik: Bunday manzil mavjud emas.")
        	os.remove(download_file_path)
        	return
        if send:
        	await mes.edit("Yuborildi")
        	os.remove(download_file_path)
