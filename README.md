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
