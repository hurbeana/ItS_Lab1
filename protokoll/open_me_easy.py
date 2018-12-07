import subprocess as sp   # brauchen wir um 7zip auszuf�hren
from threading import Thread  # threading um den Prozess zu beschleunigen
import sys  # um das erste Kommandozeilenargument zu lesen

found = False       # ob das Passwort schon gefunden wurde
start = 0           # ab welcher Zahl gesucht werden soll
end = 10000         # bis zu welcher Zahl gesucht werden soll   
file = sys.argv[1]  # Pfad zur 7z Datei

def run_sev_zip(pwd):
    """ Run 7z.exe with given password on 7z file given in argument """
    global found    # found als globalen Wert nehmen
    if found is True: # wenn Passwort gefunden, stoppen
            return
    sevzip = sp.run(  # subprocess starten
            ['7z.exe', 'e', file], # 7zip mit e f�r extract und dem Archiv Pfad
            input=pwd, # Als erste Zeile das Passwort senden wenn 7zip danach fragt
            encoding='ascii',   # Als ASCII Text codieren
            stdout=sp.PIPE, stderr=sp.PIPE) # pipen setzen damit err und out nicht ausgegeben werden
    rc = sevzip.returncode  # return code holen
    if rc is 0:  # wenn return code 0 ist war das Passwort erfolgreich
        print(f"Password for 7z file is {pwd}")  # Passwort ausgeben
        found = True  # Programm anhalten

for i in range(start, end):  # von start zu end iterieren
    if found is True: # wenn passwort gefunden wurde, anhalten
        break
    pwd = f'{i:04}'  # Passwort mit bis zu 4 Nullen padden
    print(f"At trying {pwd}")
    # Ausgabe wo wir gerade sind
    th = Thread(target=run_sev_zip, args=(pwd,))
    # neuen Thread starten mit der run_sev_zip Funktion und dem Test-Passwort als Argument
    th.start() # Thread starten