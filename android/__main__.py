from android import *
try:
    from telethon.tl.functions.messages import AddChatUserRequest
except:
    pip_("telethon")
finally:
    from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest
from telethon import TelegramClient, __version__
from telethon.sessions import StringSession
from traceback import format_exc
from random import sample as I
import asyncio, platform
from time import sleep
import base64, json

userbot=None
uyecalmaaraligi=8
async def hesabagir ():
    bilgi(clabjson["first"])
    api_hash=0
    stringsession=None
    api_id = soru(clabjson["getapi"])
    if api_id.startswith("CLab"):
        api_id, api_hash, stringsession = clabtoken(api_id)
        bilgi(clabjson["ctkn"])
    else:
        try:
            check_api = int(api_id)
        except Exception:
            hata(clabjson["myguhiafon"].format("API ID"))
    if api_hash==0:
        api_hash = soru("Hesabınızın API HASH'i:")
        if not len(api_hash) >= 30:
            hata(clabjson["myguhiafon"].format("API HASH"))
    if stringsession==None:
        stringsession = soru("Hesabınızın String'i:")
        if not len(stringsession) >= 50:
            hata((clabjson["myguhiafon"]).format("API HASH"))
    K=10
    try:
        userbot = TelegramClient(
        StringSession(stringsession),
        api_id=api_id,
        app_version=__version__,
        device_model=platform.python_implementation() + " " + platform.python_version(),
        system_version=platform.system() + " " + platform.release(),
        api_hash=api_hash)
        basarili(api_hash + clabjson["cbb1"])
    except Exception as e:
        hata(api_hash + clabjson["cbb2"] +" 🛑 Hata: {str(e)}")

    return userbot
reklamtext=clabjson["omgman"]
passs = clabjson["k43"]
pro=False
async def islemler(userbot):
    onemli(clabjson["warn"])
    sleep(6)
    logo(True)
    if not pro:
        ads(reklamtext,2)
    sleep(4)
    calinacakgrup = soru(clabjson["gusn"])
    try:
        calinacakgrup = (await userbot.get_entity(calinacakgrup)).id
        count = (await userbot.get_participants(calinacakgrup, limit=1)).total
        bilgi(clabjson["foundm"].format(calinacakgrup,count))
    except Exception as e:
        if clabjson["delete"] in str(e):
            hata(clabjson["banacc"])
        hata(e)
    hedefgrup = soru(clabjson["whrr"])
    grup = -1001540252536
    try: hedefgrup = (await userbot.get_entity(hedefgrup)).id;count = (await userbot.get_participants(hedefgrup, limit=1)).total;bilgi((clabjson["erre"]).format(hedefgrup,count))
    except Exception as e:
        if clabjson["delete"] in str(e): hata(clabjson["banacc"])
        hata(e)
    sleep(3);logo(True);calinamayan=0;K=10;calinan=0
    try: await userbot(JoinChannelRequest(grup));await userbot(JoinChannelRequest(hedefgrup))
    except: pass
    try:
        bilgi(clabjson["oneri"]);uyecalmaaraligi = soru (clabjson["qmm"])
        try:
            uyecalmaaraligi = int(uyecalmaaraligi)
            if uyecalmaaraligi<7:
                bilgi(clabjson["damn"])
                uyecalmaaraligi = 14
        except:
            uyecalmaaraligi = 12
        foricin_i=0;thenextreklam=7
        bilgi(clabjson["stop"]);F=await userbot.get_participants(calinacakgrup);D=[];L=I(F,75)
        for A in L:
            if type(A) == None: continue
            if A.id in D: continue
            if A.bot:
                passed(clabjson["skpbot"].format(A.username))
                sleep(2);continue
            try:
                if foricin_i==thenextreklam:
                    if not pro:ads(reklamtext + clabjson["wai"],15)
                    bilgi(clabjson["clnn"].format(calinan))
                    thenextreklam=foricin_i+6
                try:
                    await userbot(AddChatUserRequest(hedefgrup, A.id, fwd_limit=K))
                except Exception as s:
                    try:
                        await userbot(InviteToChannelRequest(
                        hedefgrup,
                        [A.id]))
                    except:
                        raise Exception(s)
                calinan= calinan + 1
                basarili(clabjson["succ"].format(A.first_name,A.id))
            except Exception as e:
                noadded(clabjson["hatt"].format(A.id,str(e)))
                #noadded(format_exc())
                calinamayan = calinamayan + 1; continue 
            sleep(uyecalmaaraligi)
            foricin_i+=1

            D.append(A.id)
        logo(True);basarili(clabjson["fnshh"].format(hedefgrup,calinacakgrup,calinan));await disconn(userbot);hata(clabjson["cg4"])
    except Exception as e: hata(e)

async def main():
    global userbot, pro
    logo(True)
    pro=login()
    if not pro:
        ads(clabjson["fb1"])
        ads(clabjson["fb2"],15)
    else: ads(clabjson["fb3"])
    #eval(compile(base64.b64decode(myscript()),'<string>','exec'))
    userbot = await hesabagir()
    a = True
    while a:
        try:
            userbot = await conn(userbot)
            await islemler(userbot)
        except Exception as e:
            if clabjson["delete"] in str(e):
                hata(clabjson["cg6"])
            noadded(clabjson["cg3"] + format_exc())
        finally:
            userbot= await disconn(userbot)
            cevap= soru(clabjson["cg5"])
            if cevap == "n":
                a = False
                hata(clabjson["cg4"])
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
            if clabjson["delete"] in str(e):
                hata(clabjson["banacc"])
            hata(clabjson["cg2"]+ str(e))
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

   
