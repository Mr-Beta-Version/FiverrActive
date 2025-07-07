# Fiverr Auto Refresh 🔄

A simple automation script that opens the Fiverr app and refreshes the inbox and other tabs every 10–15 minutes — keeping your profile active and responsive without manual effort.

---

## 🚀 Features
- Opens the Fiverr app automatically
- Refreshes the Inbox, My Orders, and Profile tabs
- Runs in a loop every X minutes
- Works with Android using Python (`uiautomator2`) or ADB shell
- No root required

---

## ⚙️ Requirements

- Android device (7.0+)
- USB Debugging enabled
- Python 3.x 
- Termux or PC with ADB
- Fiverr app installed

---

## 📦 Installation (Termux + Python)

```bash
pkg upgrade -y && pkg install python git
pip install uiautomator2
cd 
git clone --depth=1 https://github.com/Mr-Beta-Version/FiverrActive

------------------------------------
▶️ Run the Script:
------------------------------------
   cd FiverrActive
   python main.py

   (Make sure your device is connected via ADB or Wi-Fi and Fiverr is installed)

------------------------------------
🧑‍💻 Author:
------------------------------------
Muhammad Walid  
GitHub: @Mr-Beta-Version  
Telegram: @mdwalidmahmud

------------------------------------
🛡️ Disclaimer:
------------------------------------
This script is intended for educational and personal use only. Fiverr does not officially support automation tools. Use at your own risk.
