from RPLCD.i2c import CharLCD
import RPi.GPIO as GPIO
import time

# GPIO pin tanımları
SET_PIN = 17
INCREASE_PIN = 16
DECREASE_PIN = 26
ENTER_PIN = 4

# LCD'nin I2C adresi
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=20, rows=4)

# Menü seçenekleri
menu_items = ["CONFIGRATION", "DATE AND TIME", "LOGGING", "OUTPUT", "SETTINGS"]

# Buton pinlerini tanımla
button_pins = [SET_PIN, INCREASE_PIN, DECREASE_PIN, ENTER_PIN]

# Butonların GPIO tanımlarını ayarla
GPIO.setmode(GPIO.BCM)
for pin in button_pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Menüyü tutacak sınıf
class MenuOption:
    def __init__(self, name, next_menu=None, prev_menu=None, child_menu=None, parent_menu=None, menu_function=None):
        self.name = name
        self.next = next_menu
        self.prev = prev_menu
        self.child = child_menu
        self.parent = parent_menu
        self.menu_function = menu_function

# Menü öğelerini oluştur

menu2 = MenuOption("DATE AND TIME")
menu3 = MenuOption("LOGGING")
menu4 = MenuOption("OUTPUT")
menu5 = MenuOption("SETTINGS")
# Alt menü öğelerini oluştur
sub_menu1_1 = MenuOption("Offset")
sub_menu1_2 = MenuOption("Datum")

# Ana menü öğelerini oluştur
menu1 = MenuOption("CONFIGRATION", child_menu=sub_menu1_1)

menu1.next = menu2
menu1.prev = menu5

menu2.next = menu3
menu2.prev = menu1

menu3.next = menu4
menu3.prev = menu2

menu4.next = menu5
menu4.prev = menu3

menu5.next = menu1
menu5.prev = menu4

current_menu = menu1

# LCD'yi temizleme fonksiyonu
def clear_lcd():
    lcd.clear()

# LCD'ye mesaj yazma fonksiyonu
def write_lcd(message):
    lcd.clear()
    lcd.write_string(message)

# Ana döngü
try:
    while True:
        # Ana menüyü ekrana yazdır
        write_lcd("MAIN MENU\n")
        write_lcd("> " + current_menu.name)

        # Butonları kontrol et
        for pin in button_pins:
            if not GPIO.input(pin):
                if pin == SET_PIN:
                    if current_menu.menu_function:
                        current_menu.menu_function()
                    if current_menu.child:
                        current_menu = current_menu.child
                elif pin == INCREASE_PIN:
                    current_menu = current_menu.next
                elif pin == DECREASE_PIN:
                    current_menu = current_menu.prev
                elif pin == ENTER_PIN:
                    if current_menu.parent:
                        current_menu = current_menu.parent

        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
