import RPi.GPIO as GPIO
from RPLCD import CharLCD
import time

# LCD parametreleri
lcd = CharLCD(pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23],
              numbering_mode=GPIO.BOARD,
              cols=16, rows=2, dotsize=8)

# Buton pinleri
btn_up = 16
btn_down = 18
btn_select = 26

# Butonlar için GPIO ayarı
GPIO.setmode(GPIO.BOARD)
GPIO.setup(btn_up, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn_down, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn_select, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Değişkenler
menu_items = ['Setting', 'About', 'Exit']
sub_menu_items = ['Set Hum Value', 'Set Temp Value', 'Back']
current_menu_index = 0
current_sub_menu_index = 0
hum_value = 0
temp_value = 0

# Ana menüyü göster
def display_menu():
    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string("Menu: " + menu_items[current_menu_index])
    lcd.cursor_pos = (1, 0)
    lcd.write_string("-> " + sub_menu_items[current_sub_menu_index])

# Menü seçimi
def select_menu_item():
    global current_menu_index, current_sub_menu_index
    current_menu_index = (current_menu_index + 1) % len(menu_items)
    display_menu()

# Alt menü seçimi
def select_sub_menu_item():
    global current_menu_index, current_sub_menu_index
    current_sub_menu_index = (current_sub_menu_index + 1) % len(sub_menu_items)
    display_menu()

# Buton kontrolleri
try:
    while True:
        if GPIO.input(btn_up) == GPIO.HIGH:
            select_menu_item()
            time.sleep(0.2)

        if GPIO.input(btn_down) == GPIO.HIGH:
            select_sub_menu_item()
            time.sleep(0.2)

        if GPIO.input(btn_select) == GPIO.HIGH:
            if current_menu_index == 0:  # Setting
                if current_sub_menu_index == 0:  # Set Hum Value
                    hum_value += 1
                    print("Humidity value set to:", hum_value)
                elif current_sub_menu_index == 1:  # Set Temp Value
                    temp_value += 1
                    print("Temperature value set to:", temp_value)
                elif current_sub_menu_index == 2:  # Back
                    current_sub_menu_index = 0
                    display_menu()
            elif current_menu_index == 1:  # About
                print("About")
            elif current_menu_index == 2:  # Exit
                GPIO.cleanup()
                exit()
            time.sleep(0.2)

finally:
    GPIO.cleanup()
