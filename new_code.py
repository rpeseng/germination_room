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

class MenuOptions:
    def __init__(self):
        pass

class ButtonController:
    def __init__(self, set_pin, increase_pin, decrease_pin):
        self.set_button = Button(set_pin)
        self.increase_button = Button(increase_pin)
        self.decrease_button = Button(decrease_pin)

        self.lcd = LCDController()

        self.counter = 0

        # Buton tetikleyicileri atanıyor
        self.set_button.when_pressed = self.set_pressed
        self.increase_button.when_pressed = self.increase_pressed
        self.decrease_button.when_pressed = self.decrease_pressed

        # Butonlar için debouncing süresi
        self.debounce_time = 0.1
        self.last_time_set = time.time()
        self.last_time_increase = time.time()
        self.last_time_decrease = time.time()

    def set_pressed(self):
        current_time = time.time()
        if current_time - self.last_time_set > self.debounce_time:
            self.counter = 0
            print("Set button pressed")
            self.last_time_set = current_time

    def increase_pressed(self):
        current_time = time.time()
        if current_time - self.last_time_increase > self.debounce_time:
            self.counter += 1
            print("Increase button pressed")
            self.last_time_increase = current_time

    def decrease_pressed(self):
        current_time = time.time()
        if current_time - self.last_time_decrease > self.debounce_time:
            self.counter -= 1
            print("Decrease button pressed")
            self.last_time_decrease = current_time

    def run(self):
        try:
            while True:
                self.lcd.clear_screen()
                self.lcd.print_on_lcd(1, self.counter)
                time.sleep(1)
        except KeyboardInterrupt:
            print("Program sonlandırılıyor...")


# ButonController sınıfını kullanarak nesne oluştur
button_controller = ButtonController(set_pin=17, increase_pin=18, decrease_pin=19)

# Ana döngüyü başlat
button_controller.run()
