from subprocess import PIPE, Popen
from time import sleep as antripp
from .clabtoken import CLabToken
try: 
    from rich.console import Console
    from rich.panel import Panel
except:
    pip_("rich")
finally:
    from rich.console import Console
    from rich.panel import Panel
import os, shutil
import sys,json

console = Console()
def hata (text):
    console.print(Panel(f'[bold red]{text}[/]',width=70),justify="center")    
    sys.exit()
def pip_(module):
    onemli(f"installing {module} for cerceynlab")
    pip_cmd = ["pip", "install", f"{module}"]
    process = Popen(pip_cmd, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    return stdout
           
def bilgi (text):
    console.print(Panel(f'[blue]{text}[/]',width=70),justify="center")  
with open("strings.json","r",encoding="utf-8") as dosya:
    clabjson = json.loads(dosya.read())
def myscript ():
    return clabjson["cerceynlablisanskodu"]      
def clabtoken(text,coz=True):
    data = [1, 2, 3, 4, 5]
    ktext=None
    key=None
    with console.status("[bold blue] Clabtoken İşlemi Sürüyor...") as status:
        while data:
            num = data.pop(0)
            antripp(2)
            if num==1:
                console.log(f"[green] Şifrelenmiş keyler ayrıştırılıyor...[/green]")
                try:
                    ktext=text.split('&&')[1]
                    key=text.split('&&')[2]
                except IndexError:
                    hata(clabjson["nottoken"])
            elif num==2:
                test_crpt = CLabToken()
                console.log(f"[green]Token nesnesi oluşturuldu![/green]")
            elif num==3 and coz==False:
                test_enctext = test_crpt.yap(ktext, key)
                console.log(f"[green]Token Şifreleniyor.[/green]")
                antripp(2)
                test_enc_text = f"CLab&&{test_enctext}&&{key}"
                console.log(f"[green]Token Formatı Ayarlandı![/green]")
            elif num==4 and coz:
                console.log(f"[green]Token çözülüyor..[/green]")
                test_dec_text = test_crpt.coz(ktext, key)
                console.log(f"[green]Bilgiler ayrıştırılıyor...[/green]")
                antripp(2)
                api_id = test_dec_text.split("|")[0]
                api_hash = test_dec_text.split("|")[1]
                string = test_dec_text.split("|")[2]
            elif num==5:
                if not coz:
                    console.log(f"[green]Token oluşturma işlemi başarılı![/green]")
                    return test_enc_text
                else:
                    console.log(f"[green]Token çözme işlemi başarılı![/green]")
                    return api_id, api_hash, string 

    try:
        ss = text.split('|')
        if len(ss[1]) <29:
            hata("Bu bir CLab-AccountToken değil!")
        return ss[2], ss[1], ss[3]
    except IndexError:
        hata("Bu bir CLab-AccountToken değil!")
    return None, None, None
def login():
    dogrupass= [clabjson["cg1"],clabjson["cg0"]]
    
    sifre = soru(clabjson["hi"])
    try:
        sifre = int(sifre)
        if sifre not in dogrupass:
            hata(clabjson["ump"])
        if sifre == dogrupass[1]:
            return True
        else:return False
    except TypeError:
        hata(clabjson["ump"])
    except Exception as e:
        hata("Hata: "+str(e))
def passed (text):
    console.print(Panel(f'[yellow]{text}[/]',width=70),justify="center") 
def noadded (text):
    console.print(Panel(f'[red]{text}[/]',width=70),justify="center")  
def basarili (text):
    console.print(Panel(f'[bold green] {text}[/]',width=70),justify="center")                         
def onemli (text):
    console.print(Panel(f'[bold cyan]{text}[/]',width=70),justify="center")      
def ads (text,time=5):
   console.print(Panel(f'[green]{text}[/]',width=70),justify="center")     
   antripp(time)              
def soru (soru):
    console.print(Panel(f'[bold yellow]{soru}[/]',width=70),justify="center")                         
    return console.input(f"[bold yellow]>> [/]")
def logo (satirbırak=False):
    text = "█▀▀ █▀▀ █▀█ █▀▀ █▀▀ █▄█ █▄░█\n█▄▄ ██▄ █▀▄ █▄▄ ██▄ ░█░ █░▀█\n\n█░░ ▄▀█ █▄▄\n█▄▄ █▀█ █▄█"
    if satirbırak:
        for i in range(25):
            console.print("\n")
    console.print(Panel(f'[bold cyan]{text}[/]',width=90),justify="center")
