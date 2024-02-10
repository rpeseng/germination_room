import RPi.GPIO as GPIO
import time
from data.lcd_library import LCDController
from data.am2120_data import AM2120Sensor


# Menü seçenekleri
menu_items = ["set_temp_min", "set_temp_max", "set_hum_min", "set_hum_max"]
set_temp_min = 0
set_temp_max = 20
set_hum_min = 65
set_hum_max = 75

class MenuOptions:
    def __init__(self):
        pass


class ButtonController:
    def __init__(self, set_pin, increase_pin, decrease_pin):
        self.lcd = LCDController()
        # GPIO modunu belirle
        GPIO.setmode(GPIO.BCM)

        # Buton pinlerini tanımla
        self.set_pin = set_pin
        self.increase_pin = increase_pin
        self.decrease_pin = decrease_pin

        # Butonlar için debouncing süresi
        self.debounce_time = 0.1
        self.last_time_set = time.time()
        self.last_time_increase = time.time()
        self.last_time_decrease = time.time()

        # Butonları giriş olarak ayarla
        GPIO.setup(self.set_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.increase_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.decrease_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        # Değişken
        self.counter = 0

        # Buton tetikleyicileri atanıyor
        GPIO.add_event_detect(self.set_pin, GPIO.FALLING, callback=self.set_pressed, bouncetime=150)
        GPIO.add_event_detect(self.increase_pin, GPIO.FALLING, callback=self.increase_pressed, bouncetime=150)
        GPIO.add_event_detect(self.decrease_pin, GPIO.FALLING, callback=self.decrease_pressed, bouncetime=150)

    def set_pressed(self, channel):
        self.counter = 0
        print("Set button pressed")
        self.lcd.clear_screen()
        self.lcd.write("Set button pressed")


    def increase_pressed(self):
        self.counter += 1
        print("Increase button pressed")
        self.lcd.clear_screen()
        self.lcd.write("Increase button pressed")

    def decrease_pressed(self, channel):
        self.counter -= 1
        print("Decrease button pressed")
        self.lcd.clear_screen()
        self.lcd.write("Decrease button pressed")


    def run(self):
        try:
            while True:
                print("merhaba")
                time.sleep(1)
        except KeyboardInterrupt:
            print("Program sonlandırılıyor...")
            # GPIO pinlerini temizle
            GPIO.cleanup()


# ButonController sınıfını kullanarak nesne oluştur
button_controller = ButtonController(set_pin=16, increase_pin=18, decrease_pin=26)

# Ana döngüyü başlat
button_controller.run()

