import RPi.GPIO as GPIO
from RPLCD.i2c import CharLCD
from time import sleep

# LCD ekranı için pin ayarları
lcd = CharLCD('PCF8574', 0x27)

# Buton pinlerini tanımla
BUTTON_PIN_1 = 17
BUTTON_PIN_2 = 18
BUTTON_PIN_3 = 27

# GPIO pinlerini ayarla
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_PIN_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_PIN_3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Başlangıç değerleri
menu_items = ["Setting", "About", "Exit"]
submenu_items = ["Set Hum Value", "Set Temp Value", "Back"]
selected_menu_item = 0
selected_submenu_item = 0
humidity_value = 0
temperature_value = 0

def display_menu():
    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string(menu_items[selected_menu_item])
    lcd.cursor_pos = (1, 0)
    lcd.write_string(submenu_items[selected_submenu_item])

def update_submenu():
    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string(submenu_items[selected_submenu_item])

def increase_value():
    global humidity_value, temperature_value
    if selected_submenu_item == 0:
        humidity_value += 1
    elif selected_submenu_item == 1:
        temperature_value += 1

def decrease_value():
    global humidity_value, temperature_value
    if selected_submenu_item == 0:
        humidity_value -= 1
    elif selected_submenu_item == 1:
        temperature_value -= 1

try:
    while True:
        if GPIO.input(BUTTON_PIN_1) == GPIO.LOW:
            selected_menu_item = (selected_menu_item + 1) % len(menu_items)
            display_menu()
            sleep(0.2)
        elif GPIO.input(BUTTON_PIN_2) == GPIO.LOW:
            if selected_menu_item == 0:  # Setting
                selected_submenu_item = (selected_submenu_item + 1) % len(submenu_items)
                update_submenu()
            elif selected_menu_item == 2:  # Exit
                break
            sleep(0.2)
        elif GPIO.input(BUTTON_PIN_3) == GPIO.LOW:
            if selected_menu_item == 0 and selected_submenu_item == 2:  # Back from Setting submenu
                selected_submenu_item = 0
                display_menu()
            sleep(0.2)

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
