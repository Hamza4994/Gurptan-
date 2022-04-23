from pyrogram.errors import (
    SessionPasswordNeeded, FloodWait,
    PhoneNumberInvalid, ApiIdInvalid,
)
from pyrogram import Client as PyrogramClient
from time import sleep
from files import *
from . import console
import sys
userbot=None
def hesabagir ():
    api_id = soru("Hesabınızın API ID'i:")
    try:
        check_api = int(api_id)
    except Exception:
        hata("🛑 API ID Hatalı ! 🛑")

    api_hash = soru("Hesabınızın API HASH'i:")
    if not len(api_hash) >= 30:
        hata("🛑 API HASH Hatalı ! 🛑")

    stringsession = soru("Hesabınızın String'i:")
    if not len(api_hash) >= 30:
        hata("🛑 String Hatalı ! 🛑")

    try:
        userbot = PyrogramClient(
        stringsession,
        api_id,
        api_hash,
        device_model='Mac',
        system_version=' | Powered by @cerceyn',
        app_version=str('| 1.0'))
    except FloodWait as e:
        hata(f"Hesabınız flood yemiş! {e.x} saniye")
    except ApiIdInvalid:
        hata("🛑 API ID  veya HASH Hatalı ! 🛑")

    try:
        userbot.connect()
    except ConnectionError:
        userbot.disconnect()
        userbot.connect()
    return userbot


if __name__ == "__main__":
    logo()

    userbot = hesabagir()
    onemli("Üye çalacağım grupta bulunmam ve çaldığım üyeleri eklediğim grupta yönetici olmam gerekir..")
    calinacakgrup = soru("Üye Çalınacak Grubun kullanıcı adı: (Hangi gruptan üyeleri çekeyim) ")
    try:
        count = userbot.get_chat_members_count(calinacakgrup)
        bilgi(f"{calinacakgrup} ögesinde {count} kişi bulundu! ")
    except Exception as e:
        hata(e)
    hedefgrup = soru("Çalınan Üyeleri Hangi Gruba Çekeyim: (Grubun kullanıcı adı) ")
    try:
        count2 = userbot.get_chat_members_count(hedefgrup)
        bilgi(f"Çalacağım grubun ({calinacakgrup}) üye sayısı {count} kişi ! ")
    except Exception as e:
        hata(e)
    console.clear()
    logo()
    calinamayan=0
    calinan=0
    try:
        for member in userbot.iter_chat_members(calinacakgrup):
            try:
                if member.user.is_bot:
                    continue
                userbot.add_chat_members(hedefgrup, member.user.id)
                calinan= calinan + 1
            except Exception as e:
                calinamayan = calinamayan + 1
            sleep(8)
        console.clear()
        logo()
        basarili(f"İşlem Tamamlandı ! {hedefgrup} ögesine {calinacakgrup} ögesinden toplam {calinan} üye eklendi! ")
    except Exception as e:
        hata(e)

    






