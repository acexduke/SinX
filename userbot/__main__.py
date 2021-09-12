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
LOGS.info("installing alive.py")
LOGS.info("installing android.py")
LOGS.info("installing anime.py")
LOGS.info("installing anti_spambot.py")
LOGS.info("installing aria.py")
LOGS.info("installing base64.py")
LOGS.info("installing blacklist.py")
LOGS.info("installing botver.py")
LOGS.info("installing chat.py")
LOGS.info("installing chat.py")
LOGS.info("installing clone.py")
LOGS.info("installing covid.py")
LOGS.info("installing create.py")
LOGS.info("installing date.py")
LOGS.info("installing deepfry.py")
LOGS.info("installing direct.py")
LOGS.info("installing download.py")
LOGS.info("installing eval.py")
LOGS.info("installing exec.py")
LOGS.info("installing file.py")
LOGS.info("installing filter.py")
LOGS.info("installing gdrive.py")
LOGS.info("installing getmusic.py")
LOGS.info("installing git.py")
LOGS.info("installing glitch.py")
LOGS.info("installing hash.py")
LOGS.info("installing heroku.py")
LOGS.info("installing lastfm.py")
LOGS.info("installing lyrics.py")
LOGS.info("installing mega.py")
LOGS.info("installing memes.py")
LOGS.info("installing memify.py")
LOGS.info("installing nekobot.py")
LOGS.info("installing nekos.py")
LOGS.info("installing ping.py")
LOGS.info("installing pip.py")
LOGS.info("installing pmpermit.py")
LOGS.info("installing quotly.py")
LOGS.info("installing random.py")
LOGS.info("installing raw.py")
LOGS.info("installing rbg.py")
LOGS.info("installing readme.py")
LOGS.info("installing repeat.py")
LOGS.info("installing repo.py")
LOGS.info("installing restart.py")
LOGS.info("installing sangmata.py")
LOGS.info("installing shutdown.py")
LOGS.info("installing sleep.py")
LOGS.info("installing spam.py")
LOGS.info("installing spotifynow.py")
LOGS.info("installing stickers.py")
LOGS.info("installing sysd.py")
LOGS.info("installing telegraph.py")
LOGS.info("installing term.py")
LOGS.info("installing time.py")
LOGS.info("installing update.py")
LOGS.info("installing waifu.py")
LOGS.info("installing weather.py")
LOGS.info("installing welcome.py")
LOGS.info("installing whois.py")
LOGS.info("installing wordcloud.py")
LOGS.info ("`____  _      __  __\n/ ___|(_)_ __ \ \/ /\n\___ \| | '_ \ \  / \n ___) | | | | |/  \ \n|____/|_|_| |_/_/\_\`")


LOGS.info("⚡️ Userbot SinX DEPLOYED!SUCCESFULLY ⚡️")
LOGS.info("send Builg logs to @SinX_Support")
LOGS.info("`____  _      __  __\n/ ___|(_)_ __ \ \/ /\n\___ \| | '_ \ \  / \n ___) | | | | |/  \ \n|____/|_|_| |_/_/\_\`")




bot.run_until_disconnected()
