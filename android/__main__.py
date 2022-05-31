from pyrogram.errors import (
    SessionPasswordNeeded, FloodWait,
    PhoneNumberInvalid, ApiIdInvalid,
)
from pyrogram import Client as PyrogramClient
from time import sleep
from android import *
from . import console
import sys
userbot=None
uyecalmaaraligi=8
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
        "cerceyn",
        api_id,
        api_hash,
        session_string=stringsession,
        device_model='Unknown',
        system_version=' | Powered by @cerceynlabs',
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
reklamtext="Dikkat! Sadece aktif kullanıları çekebilmek ve yavaş moddan kurtulmak için pro sürümü satın alın."
passs = "4387"
pro=False
def islemler(userbot):
    onemli("Dikkat! Üye çalacağım grupta bulunmam ve çaldığım üyeleri eklediğim grupta yönetici olmam gerekir..")
    sleep(6)
    logo(True)
    if not pro:
        reklam(reklamtext)
    sleep(4)
    calinacakgrup = soru("Üye Çalınacak Grubun kullanıcı adı: (Hangi gruptan üyeleri çekeyim) ")
#    if not calinacakgrup.startswith("@") and not calinacakgrup.startswith("http") and not calinacakgrup.startswith("t.me"):
#        calinacakgrup = "@" + calinacakgrup
    try:
        count = userbot.get_chat_members_count(calinacakgrup)
        bilgi(f"{calinacakgrup} ögesinde {count} kişi bulundu! ")
    except Exception as e:
        hata(e)
    hedefgrup = soru("Çalınan Üyeleri Hangi Gruba Çekeyim: (Grubun kullanıcı adı) ")
#    if not hedefgrup.startswith("@") and not hedefgrup.startswith("http") and not hedefgrup.startswith("t.me"):
#        hedefgrup = "@" + hedefgrup
    try:
        count2 = userbot.get_chat_members_count(hedefgrup)
        bilgi(f"Çalacağım grubun ({calinacakgrup}) üye sayısı {count} kişi ! ")
    except Exception as e:
        hata(e)
    sleep(5)
    logo(True)
    calinamayan=0
    calinan=0
    try:
        bilgi("Hesap koruması nedeniyle her 12+ saniyede bir üye çekme isteğinde bulunmasını ayarlamanızı öneririm...")
        uyecalmaaraligi = soru ("Her üye çalma isteği sonrası ne kadar beklemeli?")
        try:
            uyecalmaaraligi = int(uyecalmaaraligi)
            if uyecalmaaraligi<7:
                bilgi("Damn! Hesabın spam yesin istemem senin için süreyi 14 yapıyorum.")
                uyecalmaaraligi = 14
        except:
            uyecalmaaraligi = 12
        foricin_i=0
        thenextreklam=6
        bilgi("İşlem başlıyor durdurmak için Ctrl+C 'ye basın! Üyelik türü Premium aktif mi: {}".format(str(pro)))
        for member in userbot.get_chat_members(calinacakgrup):
            try:
                if foricin_i==thenextreklam:
                    reklam(reklamtext)
                    sleep(4)
                    thenextreklam=foricin_i+6
                if member.user.is_bot:
                    passed("{} bot olduğu için geçiliyor!".format(member.user.username))
                    continue
                userbot.add_chat_members(hedefgrup, member.user.id)
                basarili("{} gruba başarıyla eklendi!".format(member.user.first_name))
                calinan= calinan + 1
            except Exception as e:
                noadded("{} gruba eklenemedi!".format(member.user.first_name))
                calinamayan = calinamayan + 1
            sleep(uyecalmaaraligi)
            foricin_i+=1
        console.clear()
        logo()
        basarili(f"İşlem Tamamlandı ! {hedefgrup} ögesine {calinacakgrup} ögesinden toplam {calinan} üye eklendi! ")
        userbot.stop()
        hata("Güle Güle !")
    except Exception as e:
        hata(e)

if __name__ == "__main__":
    logo(True)
    if not pro:
        reklam("Free sürüm! Yavaş Mod ve Reklamlar aktif!")
    sifre = soru("Şifre :")
    if sifre != passs:
        hata("Lütfen doğru şifreyi öğrenip gelin !")
    userbot = hesabagir()
    a = True
    while a:
        try:
            islemler(userbot)
        except Exception as e:
            onemli(e)
        finally:
            cevap= soru("Kod tekrar yürütülsün mü? (y/n)")
            if cevap == "n":
                a = False
                userbot.stop()
                hata("Güle Güle !")
            else:
                continue
        

   
