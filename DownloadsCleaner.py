from pathlib import Path
import os
import datetime
import time
import json
import shutil
import psutil
from infi.systray import SysTrayIcon
import pyautogui


def KillExistingProcess():
    try:
        PROCNAME = "DownloadsCleaner.exe"

        for proc in psutil.process_iter():
            # check whether the process name matches
            if proc.name() == PROCNAME and proc.pid != os.getpid():
                proc.kill()
    except Exception:
        pass

KillExistingProcess()

def readConfig():
    f = open("config.json", "r+")
    data = json.load(f)
    if data["firstSetup"] == True or data["freq"] == -1:
        pyautogui.alert('Welcome to DownloadsCleaner\nPlease navigate to \"config.json\" and set how frequent do you want your files to get deleted (in days).', "Error")
        os._exit(1)

    else:
        data["firstSetup"] = False
        global daysFreq
        daysFreq = data["freq"]
        execFolder = data["exec"]
    if data["logs"] == True:
        isLogActive = True
    else:
        isLogActive = False

    f.seek(0)
    json.dump(data, f, indent=4)

    return isLogActive, execFolder


isLogActive, execFolder = readConfig()


def main(path):
    files = os.listdir(path)
    for f in files:
        fileDate = datetime.date.fromtimestamp(os.path.getmtime(path + "/" + f))
        numOfDays = fileDate - datetime.date.fromtimestamp(time.time())
        if str(numOfDays) == "0:00:00":
            pass
        else:
            numOfDays = str(numOfDays)[0: str(numOfDays).index(" ")]
            if abs(int(numOfDays)) > daysFreq and f not in execFolder:
                if isLogActive == True:
                    try:
                        os.remove(path + "\\" + f)
                        fileLog = open("logs.txt", "a", encoding='utf-8')
                        fileLog.write("Deleted " + path + "\\" + f + "\n")
                        fileLog.close()
                    except Exception:
                        try:
                            shutil.rmtree(path + "\\" + f)
                            fileLog = open("logs.txt", "a", encoding='utf-8')
                            fileLog.write("Deleted " + path + "\\" + f + "\n")
                            fileLog.close()
                        except OSError as e:
                            print("Error: %s : %s" % (path + "\\" + f, e.strerror))





# SystemTray Icon
def openlogs(systray):
    try:
        os.system('logs.txt')
    except Exception:
        pyautogui.alert('Either you have disabled logs or there are no logs', "Error")

def on_quit_callback(systray):
    os._exit(1)

menu_options = (("Open Logs", None, openlogs),)
systray = SysTrayIcon("logo.ico", "DownloadsCleaner", menu_options, on_quit=on_quit_callback)
systray.start()



while True:
    main(str(Path.home() / "Downloads"))
    print("Deleted files from older than " + str(daysFreq) + " days")
    time.sleep(21600)
