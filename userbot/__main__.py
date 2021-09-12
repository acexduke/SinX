# made for sinners 
""" Userbot start point """

from importlib import import_module

from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from userbot import LOGS, bot
from userbot.modules import ALL_MODULES


INVALID_PH = '\nERROR: The Phone No. entered is INVALID' \
             '\n Tip: Use Country Code along with number.' \
             '\n or check your phone number and try again !'

try:
    bot.start()
except PhoneNumberInvalidError:
    print(INVALID_PH)
    exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)
print("installing alive.py")
print("installing android.py")
print("installing anime.py")
print("installing anti_spambot.py")
print("installing aria.py")
print("installing base64.py")
print("installing blacklist.py")
print("installing botver.py")
print("installing chat.py")
print("installing chat.py")
print("installing clone.py")
print("installing covid.py")
print("installing create.py")
print("installing date.py")
print("installing deepfry.py")
print("installing direct.py")
print("installing download.py")
print("installing eval.py")
print("installing exec.py")
print("installing file.py")
print("installing filter.py")
print("installing gdrive.py")
print("installing getmusic.py")
print("installing git.py")
print("installing glitch.py")
print("installing hash.py")
print("installing heroku.py")
print("installing lastfm.py")
print("installing lyrics.py")
print("installing mega.py")
print("installing memes.py")
print("installing memify.py")
print("installing nekobot.py")
print("installing nekos.py")
print("installing ping.py")
print("installing pip.py")
print("installing pmpermit.py")
print("installing quotly.py")
print("installing random.py")
print("installing raw.py")
print("installing rbg.py")
print("installing readme.py")
print("installing repeat.py")
print("installing repo.py")
print("installing restart.py")
print("installing sangmata.py")
print("installing shutdown.py")
print("installing sleep.py")
print("installing spam.py")
print("installing spotifynow.py")
print("installing stickers.py")
print("installing sysd.py")
print("installing telegraph.py")
print("installing term.py")
print("installing time.py")
print("installing update.py")
print("installing waifu.py")
print("installing weather.py")
print("installing welcome.py")
print("installing whois.py")
print("installing wordcloud.py")
print ("`____  _      __  __\n/ ___|(_)_ __ \ \/ /\n\___ \| | '_ \ \  / \n ___) | | | | |/  \ \n|____/|_|_| |_/_/\_\`")


LOGS.info("⚡️ Userbot SinX DEPLOYED!SUCCESFULLY ⚡️")
print("send Builg logs to @SinX_Support")
LOGS.info("`____  _      __  __\n/ ___|(_)_ __ \ \/ /\n\___ \| | '_ \ \  / \n ___) | | | | |/  \ \n|____/|_|_| |_/_/\_\`")




bot.run_until_disconnected()
