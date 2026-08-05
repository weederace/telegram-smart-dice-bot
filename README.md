# 🎲🎰 Telegram Smart Dice & Slot Automator

<div align="center">
  <p>A highly robust, fully automated Python bot designed to flawlessly execute Telegram Dice and Slot minigames using <b>Advanced Pixel Color Detection</b> and <b>UI-Shift Protection</b>.</p>
</div>

---

## 🚀 Overview | معرفی پروژه
This project is an open-source Python script that automates the process of playing Telegram-based Dice and Slot minigames. Unlike basic macro recorders, this bot dynamically reads screen pixels, adapts to UI changes, and implements strict cooldowns to mimic human behavior and bypass rate limits.

این پروژه یک ربات کاملاً هوشمند پایتونی است که مینی‌گیم‌های تلگرامی (تاس و اسلات) را به صورت خودکار بازی کرده و جوایز را دریافت می‌کند. این ربات برخلاف ماکروهای ساده، صفحه نمایش را به صورت زنده اسکن می‌کند، تغییرات رابط کاربری (مثل قفل شدن گروه) را تشخیص می‌دهد و محدودیت‌های زمانی تلگرام را برای جلوگیری از بن شدن به دقت رعایت می‌کند.

---

## ⚡ Core Features | ویژگی‌های کلیدی

- 🛡️ **UI-Shift Protection (گارد امنیتی قفل گروه):** 
  The bot actively monitors the Telegram "Attachment Clip" icon. If an admin locks the group and the chat box disappears (causing the UI to shift downwards), the bot safely pauses all scanning to prevent false-positive clicks.
  
- ⏱️ **Anti-Ban Cooldown System (سیستم ضد مسدودی):** 
  Strict 60-second operational cooldowns are implemented after every successful match or action, completely avoiding Telegram's spam limits.

- 🎯 **Smart Pixel Detection (تشخیص هوشمند پیکسل):** 
  Uses `PyAutoGUI` to calculate RGB tolerances in real-time. It distinguishes between the "Dark/Off" state and the "Lit/On" state of target numbers instantly.

- 🎁 **Auto-Claim Mechanism (دریافت خودکار جایزه):** 
  Once both targeted numbers (6 and 7) are matched, the bot executes a precise synchronized double-click to claim the reward automatically.

- 🔄 **Auto-Refresh (رفرش خودکار):** 
  Handles infinite loops securely and refreshes the minigame instance dynamically using `F5` key bindings without disrupting the OS environment.

---

## 🛠️ Tech Stack & Requirements | تکنولوژی‌ها و نیازمندی‌ها
- **Python 3.8+**
- `PyAutoGUI`: For mouse/keyboard automation and screen pixel scanning.
- `Pyperclip`: For flawless clipboard injection of emojis (bypassing keyboard language conflicts).

### Installation | نصب
```bash
git clone https://github.com/weederace/telegram-smart-dice-bot.git
cd telegram-smart-dice-bot
pip install -r requirements.txt