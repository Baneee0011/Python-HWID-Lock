import subprocess
import requests
import time
import sys
import os

hwid = str(str(subprocess.check_output('wmic csproduct get uuid')).strip().replace(r"\r", "").split(r"\n")[1].strip())
r = requests.get("https://pastebin.com/raw/yourrawlinkhere")

def printSlow(text):
    for char in text:
        print(char, end="")
        sys.stdout.flush()
        time.sleep(.1)

def Main_Program():
    if hwid in r.text:
        printSlow("Access granted...")
        time.sleep(.1)
    else:
        print("Error! HWID Not I Database!")
        print("Please contact (Your Discord Here) for help. HWID: " + hwid)
        os.system('pause >NUL')

if __name__ == "__main__":
    Main_Program()
