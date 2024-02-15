import RPi.GPIO as GPIO
from RPLCD import CharLCD

# Buton pinleri
buton_yukari = 23
buton_asagi = 24
buton_secim = 25

# LCD ekran pinleri
lcd_i2c_adres = 0x27
lcd_kolonlar = 20
lcd_satirlar = 4



# Fonksiyonlar
def fonksiyon1():
    print("func1")

def fonksiyon2():
    print("func1")

def fonksiyon3():
    print("func1")

def alt_fonksiyon1():
    print("func1")

def alt_fonksiyon2():
    print("func1")

def alt_fonksiyon3():
    print("func1")


    # Menü ve submenüler
menu = {
    "Ana Menü": {
        "1. Fonksiyon": fonksiyon1,
        "2. Fonksiyon": fonksiyon2,
        "3. Fonksiyon": fonksiyon3
    },
    "1. Fonksiyon Alt Menüsü": {
        "1.1. Alt Fonksiyon": alt_fonksiyon1,
        "1.2. Alt Fonksiyon": alt_fonksiyon2
    },
    "2. Fonksiyon Alt Menüsü": {
        "2.1. Alt Fonksiyon": alt_fonksiyon3
    }
}

# LCD ekranı başlat
lcd = CharLCD('PCF8574', 0x27)

# Butonları ayarla
GPIO.setmode(GPIO.BCM)
GPIO.setup(buton_yukari, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buton_asagi, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buton_secim, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Mevcut menü ve seçilen öğeyi takip et
mevcut_menu = "Ana Menü"
secilen_oge = 0

# Ana döngü
while True:
    # Buton basışlarını kontrol et
    if GPIO.input(buton_yukari) == GPIO.LOW:
        secilen_oge -= 1
    elif GPIO.input(buton_asagi) == GPIO.LOW:
        secilen_oge += 1
    elif GPIO.input(buton_secim) == GPIO.LOW:
        # Seçilen öğeyi çalıştır
        if mevcut_menu in menu and secilen_oge in menu[mevcut_menu]:
            menu[mevcut_menu][list(menu[mevcut_menu].keys())[secilen_oge]]()

    # Ekranı güncelle
    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write(mevcut_menu)
    for i, oge in enumerate(menu[mevcut_menu]):
        lcd.cursor_pos = (1, i)
        if i == secilen_oge:
            lcd.write("> " + oge)
        else:
            lcd.write("  " + oge)

    # Seçilen öğenin sınırlarını kontrol et
    if secilen_oge < 0:
        secilen_oge = len(menu[mevcut_menu]) - 1
    elif secilen_oge >= len(menu[mevcut_menu]):
        secilen_oge = 0


"""from lib.upymenu import Menu, MenuAction, MenuNoop
from data.lcd_library import LCDController
from RPLCD import *
from RPLCD.i2c import CharLCD

def action_callback():
    print("callback action choosen")

submenu = Menu("Submenu")
submenu_action_1 = MenuAction("Submenu Action", callback=action_callback)
submenu_action_2 = MenuAction("Submenu Action 1", callback=action_callback)
submenu.add_option(submenu_action_1)
submenu.add_option(submenu_action_2)

menu_action = MenuAction("Action", callback=action_callback)
menu = Menu("Main Menu")
menu.add_option(submenu)
menu.add_option(menu_action)
menu.add_option(MenuNoop("Nothing here"))

lcd = CharLCD('PCF8574', 0x27)

current_manu = menu.start(lcd)

menu.focus_next()
menu.focus_prev()

menu = menu.choose()

menu = menu.parent()"""