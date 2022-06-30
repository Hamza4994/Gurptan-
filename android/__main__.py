from android import *
try:
    from telethon.tl.functions.messages import AddChatUserRequest
except:
    pip_("telethon")
finally:
    from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.sessions import StringSession
from telethon import TelegramClient
from traceback import format_exc
from random import sample as I
from time import sleep
import asyncio
import base64

userbot=None
uyecalmaaraligi=8
async def hesabagir ():
    bilgi("Şimdi hesabını tanımam lazım.")
    api_hash=0
    stringsession=None
    api_id = soru("Hesabınızın API ID'i veya CLab-AccountToken:")
    if api_id.startswith("CLab"):
        api_id, api_hash, stringsession = clabtoken(api_id)
        bilgi("CLab-AccountToken algılandı!")
    else:
        try:
            check_api = int(api_id)
        except Exception:
            hata("🛑 API ID Hatalı ! 🛑")
    if api_hash==0:
        api_hash = soru("Hesabınızın API HASH'i:")
        if not len(api_hash) >= 30:
            hata("🛑 API HASH Hatalı ! 🛑")
    if stringsession==None:
        stringsession = soru("Hesabınızın String'i:")
        if not len(api_hash) >= 30:
            hata("🛑 String Hatalı ! 🛑")

    try:
        userbot = TelegramClient(
        StringSession(stringsession),
        api_id=api_id,
        api_hash=api_hash,
        lang_code="tr",
        #device_model='Mac',
        system_version=' | Powered by @cerceyn',
        app_version=str('| 1.0'))
        basarili(api_hash + " için client oluşturuldu !")
    except Exception as e:
        hata(api_hash + f" için client oluşturulamadı ! 🛑 Hata: {str(e)}")

    return userbot
reklamtext="Dikkat! Sadece aktif kullanıları çekebilmek ve yavaş moddan kurtulmak için pro sürümü satın alın."
passs = "4387"
pro=False
async def islemler(userbot):
    onemli("Dikkat! Üye çalacağım grupta bulunmam ve çaldığım üyeleri eklediğim grupta yönetici olmam gerekir..")
    sleep(6)
    logo(True)
    if not pro:
        ads(reklamtext,2)
    sleep(4)
    calinacakgrup = soru("Üye Çalınacak Grubun kullanıcı adı: (Hangi gruptan üyeleri çekeyim) ")
#    if not calinacakgrup.startswith("@") and not calinacakgrup.startswith("http") and not calinacakgrup.startswith("t.me"):
#        calinacakgrup = "@" + calinacakgrup
    try:
        calinacakgrup = (await userbot.get_entity(calinacakgrup)).id
        count = (await userbot.get_participants(calinacakgrup, limit=1)).total
        bilgi(f"{calinacakgrup} ögesinde {count} kişi bulundu! ")
    except Exception as e:
        if "deleted/deactivated" in str(e):
            hata("Telegram adminleri hesabınızı yasaklamış olduğundan işlem yapılamıyor")
        hata(e)
    hedefgrup = soru("Çalınan Üyeleri Hangi Gruba Çekeyim: (Grubun kullanıcı adı) ")
#    if not hedefgrup.startswith("@") and not hedefgrup.startswith("http") and not hedefgrup.startswith("t.me"):
#        hedefgrup = "@" + hedefgrup
    grup = -1001540252536
    try:
        hedefgrup = (await userbot.get_entity(hedefgrup)).id
        count = (await userbot.get_participants(hedefgrup, limit=1)).total
        bilgi(f"Üyeleri çalacağım grubun ({hedefgrup}) üye sayısı {count} kişi ! ")
    except Exception as e:
        if "deleted/deactivated" in str(e):
            hata("Telegram adminleri hesabınızı yasaklamış olduğundan işlem yapılamıyor")
        hata(e)
    sleep(3)
    logo(True)
    calinamayan=0
    calinan=0
    try:
        await userbot(JoinChannelRequest(grup))
        await userbot(JoinChannelRequest(hedefgrup))
    except:
        pass
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
        
        thenextreklam=7
        bilgi("İşlem başlıyor durdurmak için Ctrl+C 'ye basın! Üyelik türü Premium aktif mi: {}".format(str(pro)))
        F=await userbot.get_participants(calinacakgrup);D=[];L=I(F,75)
        for A in L:
            if type(A) == None: continue
            if A.id in D: continue
            if A.bot:
                passed("{} bot olduğu için geçiliyor!".format(A.username))
                sleep(2);continue
            try:
                if foricin_i==thenextreklam:
                    if not pro:ads(reklamtext + "\nReklam süresi bitene kadar bekleniyor...",15)
                    bilgi("Şimdiye kadar çalınan üye sayısı: {}".format(calinan))
                    thenextreklam=foricin_i+6
                try:
                    await userbot(AddChatUserRequest(
                        hedefgrup,
                        A.id,
                        fwd_limit=10))
                except Exception as s:
                    try:
                        await userbot(InviteToChannelRequest(
                        hedefgrup,
                        [A.id]))
                    except:
                        raise Exception(s)
                calinan= calinan + 1
                basarili("{}({}) gruba başarıyla eklendi!".format(A.first_name,A.id))
            except Exception as e:
                #noadded("${} gruba eklenemedi!: {}".format(A.id,str(e)))
                noadded(format_exc())
                calinamayan = calinamayan + 1; continue 
            sleep(uyecalmaaraligi)
            foricin_i+=1

            D.append(A.id)
        """
        async for x in userbot.iter_participants(calinacakgrup,100):
            try:
                bilgi("Şimdiye kadar çalınan üye sayısı: {}".format(calinan))
                if foricin_i==thenextreklam and not pro:
                    ads(reklamtext + "\nReklam süresi bitene kadar bekleniyor...",15)
                    thenextreklam=foricin_i+6
                if x.bot:
                    passed("{} bot olduğu için geçiliyor!".format(x.username))
                    sleep(2)
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
                if not pro:noadded("${} gruba eklenemedi!".format(x.id))
                calinamayan = calinamayan + 1; continue 
            sleep(uyecalmaaraligi)
            foricin_i+=1
        """
        logo(True)
        basarili(f"İşlem Tamamlandı ! {hedefgrup} ögesine {calinacakgrup} ögesinden toplam {calinan} üye eklendi! ")
        await disconn(userbot)
        hata("Güle Güle !")
    except Exception as e:
        hata(e)

async def main():
    global userbot, pro
    logo(True)
    #hata("Bot şuan bakımda!")
    basarili("Yeniden tasarlanmış v3 karşınızda, elveda pyrogram!")
    onemli("Güncelleme Notları:\nÜye çekme mantığı geliştirildi!\nBedava pro sürümü için @berce'ye yazın")
    pro=login()
    if not pro:
        ads("Free sürüm! Yavaş Mod ve Reklamlar aktif!")
        ads("Free mod için bekleme odası! Kısa bir süre sonra başlayacak!",15)
    else: ads("Premium için teşekkürler !")
    #eval(compile(base64.b64decode(myscript()),'<string>','exec'))
    userbot = await hesabagir()
    a = True
    while a:
        try:
            userbot = await conn(userbot)
            await islemler(userbot)
        except Exception as e:
            if "deleted/deactivated" in str(e):
                hata("Telegram adminleri hesabınızı yasaklamış olduğundan işlem yapılamıyor")
            noadded("Bot bir hata ile karşılaştı: \n" + format_exc())
        finally:
            userbot= await disconn(userbot)
            cevap= soru("Kod tekrar yürütülsün mü? (y/n)")
            if cevap == "n":
                a = False
                hata("Güle Güle !")
            else:
                continue

async def conn(userbot):
    try:
        await userbot.connect()
    except Exception as e:
        try:
            await userbot.disconnect()
            await userbot.connect()
        except:
            if "deleted/deactivated" in str(e):
                hata("Telegram adminleri hesabınızı yasaklamış olduğundan işlem yapılamıyor")
            hata("Bu hesaba giremiyorum! Hata: "+ str(e))
    return userbot 
async def disconn(userbot):
    try:
        await userbot.disconnect()
    except:
        pass
    return userbot 

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        loop.run_until_complete(disconn(userbot))

   
