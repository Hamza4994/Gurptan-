from pyrogram import Client as PyrogramClient
from files import *
from . import console
import sys
userbot=None
def hesabagir ():
  api_id = soru("Hesabınızın API ID'i:)
  try:
      check_api = int(api_id)
  except Exception:
      hata("🛑 API ID Hatalı ! 🛑")
      exit(1)
  api_hash = soru("Hesabınızın API HASH'i:)
  if not len(api_hash) >= 30:
      hata("🛑 API HASH Hatalı ! 🛑")
      exit(1)
  stringsession = soru("Hesabınızın String'i:)
  if not len(api_hash) >= 30:
      hata("🛑 String Hatalı ! 🛑")
      exit(1)
  userbot = PyrogramClient(
    stringsession,
    api_id,
    api_hash,
    device_model='Mac',
    system_version=' | Powered by @cerceyn',
    app_version=str('| 1.0'))

if __name__ == "__main__":
  logo()
  
  hesabagir()
  
