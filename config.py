import re, os, time

id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "27744380")
    API_HASH  = os.environ.get("API_HASH", "08f3fd61ccd1aa4aa6ccdb716fb68fed")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6067754375:AAEbwJB_DkWT9UAwQ9UMUfQUQ2MAWvo-viQ")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "RenameSnowProBot")
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","Snow_User_Data")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://RENAMESNOWPROBOT:RENAMESNOWPROBOT@cluster0.uaf4ivm.mongodb.net/?retryWrites=true&w=majority")
 
    # other configs
    DOWNLOAD_LOCATION = "./MEGA_DOWNLOADS"
    TG_MAX_SIZE = 2040108421
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://telegra.ph/file/3b7050b8b5d918a00b490.jpg")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6065594762').split()]
    FORCE_SUB   = os.environ.get("FORCE_SUB", "Kdramaland_Official") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001971176803"))
    FLOOD = int(os.environ.get("FLOOD", '10'))
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))



class Txt(object):
    # part of text configuration
    START_TXT = """<b><b>Hey {mention} ,</b>
I'm a Simple File Renamer + File to Video bot with support for features like thumbnail, custom caption support and more! 

This bot is managed by @SupernovaNetwork!
"""

    ABOUT_TXT = """<b>⋉ Owner : <a href=https://t.me/xenov7x>𝙓𝙚𝙣𝙤𝙫</a>

❐ Bot Name : <a href=https://t.me/xen_renamer_bot>Xen Renamer</a>
❐ Instagram: <a href=https://instagram.com/not_xenov?igshid=eHplZXZ5anlkbmQ0>not xenov</a>
❐ Language: <a href=https://www.python.org/>Python 3</a>
❐ Library: <a href=https://github.com/pyrogram>Pyrogram</a>
❐ Support Group: <a href=https://t.me/sn_botsupport>Bot Support</a>
❐ Powered by: <a href=https://t.me/supernovanetwork>Supernova™</a>
━━━━━━━━━━━━━━━━━━━━━━━━━━━
➮ Want your own Bot?: <a href=https://t.me/not_xenov>Contact here</a>"""

    HELP_TXT = """
🤔 <b><u>How to Set Thumbnail</u></b>
  
<b>➩</b> /start The Bot and Send Any Pic to Automatically Set as Thumbnail .
<b>➩</b> /del_thumb Use it to Delete Your Old Thumbnail 
<b>➩</b> /view_thumb Use it to View Your Current Thumbnail.

📑 <b><u>How to Set Custom Caption </u></b>

<b>➩</b> /set_caption - Use it to Set a Custom Caption 
<b>➩</b> /see_caption - Use it to View Your Custom Caption 
<b>➩</b> /del_caption - Use it to delete your custom caption 
Exᴀᴍᴩʟᴇ:- /set_caption 📕 Fɪʟᴇ Nᴀᴍᴇ: {filename}
💾 Sɪᴢᴇ: {filesize}
⏰ Dᴜʀᴀᴛɪᴏɴ: {duration}

✏️ <b><u>Hᴏᴡ Tᴏ Rᴇɴᴀᴍᴇ A Fɪʟᴇ</u></b>

<b>➩</b> Send Any File and Type a New File Name and Select Your Format [Document, Video, Audio]. 
          
🥷 <b><u>Need Assistance? Contact</u></b> : <a href=https://t.me/xenov7x>Xenov</a>
"""


    PROGRESS_BAR = """<b>\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ Dᴏɴᴇ : {0}%
┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ Eᴛᴀ: {4}
╰━━━━━━━━━━━━━━━➣ </b>"""
