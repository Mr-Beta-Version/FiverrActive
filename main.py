# ====================================================
# 📜 Fiverr Auto Refresher Script
# 🔧 Script to auto-open Fiverr app and refresh tabs
# 🧑‍💻 Author: Muhammad Walid (YT@CodeHobbyist)
# 🌐 Website: https://mr-beta-version.github.io/walid.github.io/
# 🐱‍💻 GitHub: https://github.com/Mr-Beta-Version
# 📅 Created: July 7, 2025
# 🛠️ Tools Used: uiautomator2, Python
# ====================================================

import uiautomator2 as u2
import time
import sys
import os
import random

os.system("git pull")

if "win" in sys.platform:
    os.system("cls")
else:
    os.system("clear")

d = u2.connect()

total = 0

d.freeze_rotation(True)

print("===[Lower your screen brightness within 10 seconds...]===")

time.sleep(10)

def sleepS():
    count = random.randint(3, 5)
    print(f"Sleeping for {count} seconds...")
    time.sleep(count)

def sleepM():
    count = random.randint(10, 15)
    print(f"Sleeping for {count} minutes...")
    time.sleep(count * 60)

def scrollDown():
    d.swipe(500, 300, 500, 1000)

def scrollUp():
    d.swipe(500, 1500, 500, 500)

d.app_stop("com.fiverr.fiverr")


while True:
    print("Opening Fiverr App...")
    d.app_start("com.fiverr.fiverr")
    sleepS()

    if d(description="Inbox").exists:
        print("Opening Inbox...")
        d(description="Inbox").click()
        sleepS()
        scrollDown()
        
    
    if d(description="Home",className='android.widget.FrameLayout').exists:
        print("Opening Home...")
        d(description="Home",className='android.widget.FrameLayout').click()
        sleepS()
        scrollUp()

    
    if d(description="Manage orders").exists:
        print("Opening Manage Orders...")
        d(description="Manage orders").click()
        sleepS()

    if d(description="Account").exists:
        print("Opening Account...")
        d(description="Account").click()
        sleepS()
        scrollUp()


    print("Waiting 10-15 Minutes...")
    now = datetime.now().strftime("%I:%M %p")
    print(f"⏰ Pausing at {now}")
    d.press("home")
    total += 1
    print(f"[>] Total refreshes: {total}")

    sleepM()



