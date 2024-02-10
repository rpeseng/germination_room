from gpiozero import Button
import time
from data.lcd_library import LCDController
from data.am2120_data import AM2120Sensor


# Menü seçenekleri
menu_items = ["set_temp_min", "set_temp_max", "set_hum_min", "set_hum_max"]
set_temp_min = 0
set_temp_max = 20
set_hum_min = 65
set_hum_max = 75


# GPIO pin numaraları
SET_PIN = 17
INCREASE_PIN = 18
DECREASE_PIN = 19

# Butonlar
set_button = Button(SET_PIN)
increase_button = Button(INCREASE_PIN)
decrease_button = Button(DECREASE_PIN)


# Değişkenler
counter = 0

# Tuş işlevleri
def set_pressed():
    global counter
    print("Set button pressed")
    counter = 0  # Sıfırla

def increase_pressed():
    global counter
    print("Increase button pressed")
    counter += 1  # Artır

def decrease_pressed():
    global counter
    print("Decrease button pressed")
    counter -= 1  # Azalt

# Buton tetikleyicileri
set_button.when_pressed = set_pressed
increase_button.when_pressed = increase_pressed
decrease_button.when_pressed = decrease_pressed

try:
    while True:
        # Her saniyede bir sayaç değerini göster
        print("Counter:", counter)
        time.sleep(1)
except KeyboardInterrupt:
    print("Program sonlandırılıyor...")
finally:
    pass  # GPIO temizleme kodu buraya eklenecek