import time
import pyautogui
import pyperclip

# مختصات کادر پیام (فقط برای کلیک کردن و تایپ)
chat_box_x = 0
chat_box_y = 0

# مختصات گیره چت (ملاک اصلی باز یا بسته بودن گروه)
clip_x = 0
clip_y = 0
clip_color = (0, 0, 0)

# مختصات اعداد 6 و 7
x6 = 0
y6 = 0
color6_dark = (0, 0, 0)

x7 = 0
y7 = 0
color7_dark = (0, 0, 0)

def is_chat_open():
    """چک میکنه آیا گیره چت سر جاش هست (گروه بازه) یا نه"""
    try:
        current_color = pyautogui.pixel(clip_x, clip_y)
        r_diff = abs(current_color[0] - clip_color[0])
        g_diff = abs(current_color[1] - clip_color[1])
        b_diff = abs(current_color[2] - clip_color[2])
        
        # حساسیت بسیار بالا (15) برای تشخیص دقیق گیره
        return r_diff < 15 and g_diff < 15 and b_diff < 15
    except:
        return False

def is_number_6_lit():
    """بررسی میکنه که آیا عدد ۶ روشن شده است یا نه"""
    # گارد امنیتی: اگر گیره سر جاش نبود (گروه قفله)، عدد رو چک نکن!
    if not is_chat_open():
        return False
        
    try:
        current = pyautogui.pixel(x6, y6)
        return (abs(current[0] - color6_dark[0]) > 30 or \
                abs(current[1] - color6_dark[1]) > 30 or \
                abs(current[2] - color6_dark[2]) > 30)
    except:
        return False

def is_number_7_lit():
    """بررسی میکنه که آیا عدد ۷ روشن شده است یا نه"""
    # گارد امنیتی: اگر گیره سر جاش نبود (گروه قفله)، عدد رو چک نکن!
    if not is_chat_open():
        return False
        
    try:
        current = pyautogui.pixel(x7, y7)
        return (abs(current[0] - color7_dark[0]) > 30 or \
                abs(current[1] - color7_dark[1]) > 30 or \
                abs(current[2] - color7_dark[2]) > 30)
    except:
        return False

def do_refresh():
    """رفرش کردن ربات با کلیک روی 6 و زدن F5 (فقط برای رفرش، نه گرفتن جایزه)"""
    print("🔄 Pressing F5 to refresh...")
    pyautogui.click(x6, y6) 
    time.sleep(0.5)
    pyautogui.press('f5')
    print("⏳ Waiting 5 seconds for bot to reload...")
    time.sleep(5)

def wait_for_chat_box():
    """صبر میکنه تا گروه باز بشه با بررسی گیره چت"""
    print("Checking if chat box is available (Looking at Clip Icon)...")
    while not is_chat_open():
        print("Chat box hidden (Group Locked). Waiting 5s...")
        time.sleep(5)

def send_emoji(emoji_symbol):
    wait_for_chat_box()
    
    pyautogui.click(chat_box_x, chat_box_y)
    time.sleep(1)
    
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    time.sleep(1)

    pyperclip.copy(emoji_symbol)
    time.sleep(1)
    
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    
    pyautogui.press('enter')
    print(f"Sent successfully: {emoji_symbol}")
    time.sleep(1)

def main():
    global chat_box_x, chat_box_y
    global clip_x, clip_y, clip_color
    global x6, y6, color6_dark, x7, y7, color7_dark
    
    pyautogui.FAILSAFE = False

    print("--- SMART SETUP (4 STEPS) ---")
    
    print("\nSTEP 1: Move mouse to an EMPTY SPACE in the TEXT BOX (برای کلیک و تایپ).")
    for i in range(5, 0, -1):
        print(f"{i}...")
        time.sleep(1)
        
    chat_box_x, chat_box_y = pyautogui.position()
    print("✅ Text Box saved!")

    print("\nSTEP 2: Move mouse to the center of the ATTACHMENT CLIP (آیکون گیره کنار چت).")
    for i in range(5, 0, -1):
        print(f"{i}...")
        time.sleep(1)
        
    clip_x, clip_y = pyautogui.position()
    pyautogui.moveTo(10, 10) # حذف اثر سایه موس
    time.sleep(0.5)
    clip_color = pyautogui.pixel(clip_x, clip_y)
    print("✅ Clip Icon saved!")

    print("\nSTEP 3: Move mouse to the center of number '6' (DARK/OFF).")
    for i in range(5, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    x6, y6 = pyautogui.position()
    color6_dark = pyautogui.pixel(x6, y6)
    print("✅ Number 6 saved!")

    print("\nSTEP 4: Move mouse to the center of number '7' (DARK/OFF).")
    for i in range(5, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    x7, y7 = pyautogui.position()
    color7_dark = pyautogui.pixel(x7, y7)
    print("✅ Number 7 saved!")

    print("-" * 50)
    print("ALL SET! Starting the bot...")
    print("-" * 50)
    
    while True:
        # ---------------------------------------------------------
        # فاز اول: تاس انداختن تا زمانی که ۶ بدهد
        # ---------------------------------------------------------
        print("\n" + "="*45)
        print("🎲 PHASE 1: Rolling DICE")
        print("="*45)
        while True:
            send_emoji("🎲")
            
            print("⏳ Waiting 5 seconds for dice animation...")
            time.sleep(5)
            
            do_refresh()
            
            if is_number_6_lit():
                print("✅ Number 6 is LIT!")
                print("⏳ Waiting 60 seconds before moving to SLOT...")
                time.sleep(60) 
                break # رفتن به فاز دوم
            else:
                if not is_chat_open():
                    print("❌ Group is Locked! Skipping scan.")
                else:
                    print("❌ Number 6 is NOT lit.")
                print("⏳ Waiting 60 seconds before trying DICE again...")
                time.sleep(60)

        # ---------------------------------------------------------
        # فاز دوم: اسلات انداختن تا زمانی که ۷ بدهد
        # ---------------------------------------------------------
        print("\n" + "="*45)
        print("🎰 PHASE 2: Spinning SLOT")
        print("="*45)
        while True:
            send_emoji("🎰")
            
            print("⏳ Waiting 5 seconds for slot animation...")
            time.sleep(5)
            
            do_refresh()
            
            if is_number_7_lit():
                print("✅ Number 7 is LIT!")
                break # رفتن به فاز سوم (جایزه)
            else:
                if not is_chat_open():
                    print("❌ Group is Locked! Skipping scan.")
                else:
                    print("❌ Number 7 is NOT lit.")
                print("⏳ Waiting 60 seconds before trying SLOT again...")
                time.sleep(60)

        # ---------------------------------------------------------
        # فاز سوم: دابل کلیک روی ۷ و صبر ۶۰ ثانیه‌ای
        # ---------------------------------------------------------
        print("\n" + "="*45)
        print("🎉 CLAIM REWARD (DOUBLE CLICK)")
        print("="*45)
        
        wait_for_chat_box() # مطمئن میشیم قبل از جایزه گرفتن گروه باز باشه
        
        print("⏳ Waiting 5 seconds before double clicking...")
        time.sleep(5)
        
        print("🖱️ DOUBLE CLICKING on number 7...")
        pyautogui.doubleClick(x7, y7) # دابل کلیک برای دریافت جایزه
        time.sleep(1)
        
        pyautogui.moveTo(chat_box_x, chat_box_y) # دور کردن موس
        
        print("🎁 Reward claimed! Waiting 60 seconds before starting over...")
        # شمارش معکوس 60 ثانیه برای شروع دور جدید
        for i in range(60, 0, -1):
            if i % 10 == 0 or i <= 5: 
                print(f"Restarting in {i} seconds...")
            time.sleep(1)
            
        print("\n🚀 Cooldown finished! Restarting loop...\n")

if __name__ == "__main__":
    main()