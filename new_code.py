import RPi.GPIO as GPIO
import time
from data.lcd_library import LCDController
from data.am2120_data import AM2120Sensor

# Menü seçenekleri
menu_items = ["set_temp_min", "set_temp_max", "set_hum_min", "set_hum_max"]

# Submenu seçenekleri
submenus = {
    "set_temp_min": [
        {"name": "Sıcaklığı 1 Derece Artır", "function":""},
        {"name": "Sıcaklığı 1 Derece Azalt", "function":""},
        {"name": "Sıcaklığı Manuel Gir", "function":""},
    ]
}

set_temp_min = 2
set_temp_max = 20
set_hum_min = 65
set_hum_max = 75


class MenuOptions:
    def __init__(self):
        pass


class ButtonController:
    def __init__(self, set_pin, increase_pin, decrease_pin):
        self.items = menu_items
        self.select_item = 0
        self.lcd = LCDController()
        # GPIO modunu belirle
        GPIO.setmode(GPIO.BCM)

        # Buton pinlerini tanımla
        self.set_pin = set_pin
        self.increase_pin = increase_pin
        self.decrease_pin = decrease_pin
        self.button_pins = [self.set_pin]

        self.count = 0
        self.yerdegistirme = 0
        self.set_pin_activate=0

        self.set_temp_min = 2
        self.set_temp_max = 20
        self.set_hum_min = 65
        self.set_hum_max = 75



        # Butonları giriş olarak ayarla
        GPIO.setup(self.set_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.increase_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.decrease_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        # Değişken
        self.count = 0

        # Buton tetikleyicileri atanıyor
        GPIO.add_event_detect(self.set_pin, GPIO.FALLING, callback=self.set_pressed, bouncetime=150)
        GPIO.add_event_detect(self.increase_pin, GPIO.FALLING, callback=self.increase_pressed, bouncetime=150)
        GPIO.add_event_detect(self.decrease_pin, GPIO.FALLING, callback=self.decrease_pressed, bouncetime=150)

    def set_hum_max_function(self):
        print("hade bakalım")
    def set_temp_max_function(self):
        print("hade bakalım2")
    def set_hum_min_function(self):
        print("hade bakalım3")
    def set_temp_min_function(self):
        print("hade bakalım4")
    def set_pressed(self, channel):
        print("Set button pressed")
        "if self.select_item == 0:"
        self.count = 1
        self.show_sub_menu1()



        """ 
       else:
            selected_item = self.items[self.select_item]
            # Seçilen menü öğesine göre işlevi çalıştır
            if selected_item == "set_temp_min":
                self.set_temp_min_function()
            elif selected_item == "set_temp_max":
                self.set_temp_max_function()
            elif selected_item == "set_hum_min":
                self.set_hum_min_function()
            elif selected_item == "set_hum_max":
                self.set_hum_max_function()"""

    def increase_pressed(self, channel):

        self.select_item = (self.select_item - 1) % len(self.items)
        print("increase button pressed")

        #self.lcd.clear_screen()
        #self.lcd.write("Increase button pressed")

    def decrease_pressed(self, channel):

        self.select_item = (self.select_item + 1) % len(self.items)

        print("Decrease button pressed")
        #self.lcd.clear_screen()
        #self.lcd.write("Decrease button pressed")


    """
    # Buton durumlarını kontrol etme fonksiyonu
    def check_buttons(self):
        for pin in self.button_pins:
            if not GPIO.input(pin):
                return pin
        return None"""

    def show_menu(self):
        try:
            while True:
                if self.count == 0:
                    self.lcd.clear_screen()
                    for i in range(len(self.items)):
                        if i == self.select_item:
                            if i == 0:
                                self.lcd.lcd.cursor_pos = (0, 0)
                                self.lcd.write("Menu")
                                self.lcd.lcd.cursor_pos = (1, 0)
                                self.lcd.write("> ")
                                self.lcd.write(self.items[i])
                            elif i == 1:
                                self.lcd.lcd.cursor_pos = (0, 0)
                                self.lcd.write("Menu")
                                self.lcd.lcd.cursor_pos = (1, 0)
                                self.lcd.write("> ")
                                self.lcd.write(self.items[i])
                            elif i == 2:
                                self.lcd.lcd.cursor_pos = (0, 0)
                                self.lcd.write("Menu")
                                self.lcd.lcd.cursor_pos = (1, 0)
                                self.lcd.write("> ")
                                self.lcd.write(self.items[i])
                            else:
                                self.lcd.lcd.cursor_pos = (0, 0)
                                self.lcd.write("Menu")
                                self.lcd.lcd.cursor_pos = (1, 0)
                                self.lcd.write("> ")
                                self.lcd.write(self.items[i])
                else:
                    break
                time.sleep(0.2)
        except KeyboardInterrupt:
            self.lcd.clear_screen()
            self.lcd.print_on_lcd("LCD Deactive", 1)
            print("Program sonlandırılıyor...")
            # GPIO pinlerini temizle
            GPIO.cleanup()

    def show_sub_menu1(self):
        while True:
            print("girildi")
            if self.select_item == 0:
                try:
                    self.lcd.clear_screen()
                    self.lcd.lcd.cursor_pos = (0, 0)
                    self.lcd.write("Menu")
                    self.lcd.lcd.cursor_pos = (1, 0)
                    self.lcd.write("> ")
                    self.lcd.write(self.items[0])
                    self.lcd.lcd.cursor_pos = (2, 0)
                    self.lcd.write("Set Degeri =  ")
                    self.lcd.write(str(self.set_temp_min))
                    if self.yerdegistirme==1:
                        self.set_temp_min += 1
                        self.lcd.clear_screen()
                        self.lcd.lcd.cursor_pos = (0, 0)
                        self.lcd.write("Menu")
                        self.lcd.lcd.cursor_pos = (1, 0)
                        self.lcd.write("> ")
                        self.lcd.write(self.items[0])
                        self.lcd.lcd.cursor_pos = (2, 0)
                        self.lcd.write("Set Degeri =  ")
                        self.lcd.write(str(self.set_temp_min))
                        self.yerdegistirme = 0
                    elif self.yerdegistirme==2:
                        self.set_temp_min -= 1
                        self.lcd.clear_screen()
                        self.lcd.lcd.cursor_pos = (0, 0)
                        self.lcd.write("Menu")
                        self.lcd.lcd.cursor_pos = (1, 0)
                        self.lcd.write("> ")
                        self.lcd.write(self.items[0])
                        self.lcd.lcd.cursor_pos = (2, 0)
                        self.lcd.write("Set Degeri =  ")
                        self.lcd.write(str(self.set_temp_min))
                        self.yerdegistirme = 0
                    elif self.yerdegistirme==1:
                        self.count = 0
                        self.show_menu()
                    time.sleep(0.5)
                except KeyboardInterrupt:
                    GPIO.cleanup()
                    self.lcd.lcd_screen_deactivate()

            print("yazildi")


# ButonController sınıfını kullanarak nesne oluştur
button_controller = ButtonController(set_pin=16, increase_pin=18, decrease_pin=26)

button_controller.show_menu()

"""try:
    while True:
        if button_controller.count == 0:
            button_controller.show_menu()
        else:
            button_controller.show_sub_menu1()

except Exception as error:
    GPIO.cleanup()
    print(f"hata: {error}")
"""
