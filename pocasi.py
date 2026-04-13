import os
from gtts import gTTS
import ftplib

# Text, který bude rádio říkat
text = "Zdravíme posluchače rádia NEO FM. Dnes je venku polojasno a teplota se drží na příjemných patnácti stupních. Přejeme vám fajn poslech."

# Vyrobíme MP3 soubor
tts = gTTS(text=text, lang='cs')
tts.save("pocasi.mp3")

# Pošleme to na tvůj Citrus (s6.citrus3.com)
FTP_HOST = os.environ.get('FTP_HOST')
FTP_USER = os.environ.get('FTP_USER')
FTP_PASS = os.environ.get('FTP_PASS')

with ftplib.FTP(FTP_HOST) as ftp:
    ftp.login(FTP_USER, FTP_PASS)
    with open("pocasi.mp3", "rb") as file:
        ftp.storbinary("STOR pocasi.mp3", file)
