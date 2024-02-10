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


# Seçilen menü öğesi
selected_item = 0

class GerminationRoom:
    def __init__(self):
        self.value = 0
        self.selected_option = 1
        self.lcd = LCDController()
        self.temp_and_humudity = AM2120Sensor()

        # Raspberry Pi GPIO konfigürasyonu
        # GPIO pin numaraları
        SET_PIN = 26
        INCREASE_PIN = 18
        DECREASE_PIN = 21

        # Butonlar
        set_button = Button(SET_PIN)
        increase_button = Button(INCREASE_PIN)
        decrease_button = Button(DECREASE_PIN)

    def show_main_screen(self):
        values = self.temp_and_humudity.read_am2120_values()
        temp = values[0]
        humudity = values[1]

        self.lcd.print_on_lcd(1, "ORTAM DEGERLERI")
        self.lcd.print_on_lcd(2, f"Sıcaklık: {temp}")
        self.lcd.print_on_lcd(3, f"Nem     : {humudity}")
        time.sleep(2)


    def increase_value(self):
        self.value += 1
        print(f"Arttır: {self.value}")
        self.lcd.lcd_set_text(3, f"Nem Değeri: {self.value}")

    def decrease_value(self):
        self.value -= 1
        print(f"Azalt: {self.value}")
        self.lcd.lcd_set_text(3, f"Nem Değeri: {self.value}")

    def show_settings_menu(self):
        print("Ayarlar Menüsü")
        options = ["Ana Menü", "Nem Değeri", "Sıcaklık Değeri", "Çıkış"]

        while True:
            self.selected_option = self.get_selected_option(options)
            self.lcd.print_on_lcd(4, options[self.selected_option - 1])

            if self.selected_option == 1:
                print("set_temp_min")

            elif self.selected_option == 2:
                print("Nem Değeri seçildi")
            elif self.selected_option == 3:
                print("Sıcaklık Değeri seçildi")
            elif self.selected_option == 4:
                print("Çıkış seçildi")
                break
    """
    def get_selected_option(self, options):
        current_option = 1

        while True:
            for idx, option in enumerate(options, start=1):
                print(f"{idx}. {option}")

            #key = GPIO.wait_for_edge(22, GPIO.FALLING)

            if key == 22:
                return current_option

            current_option += 1
            if current_option > len(options):
                current_option = 1

            time.sleep(0.2)"""


class ButtonController:
    def __init__(self, set_pin=26, increase_pin=18, decrease_pin=21):
        # Butonlar oluşturuluyor
        self.set_button = Button(set_pin)
        self.increase_button = Button(increase_pin)
        self.decrease_button = Button(decrease_pin)

        # Değişken
        self.counter = 0

        # Buton tetikleyicileri atanıyor
        self.set_button.when_pressed = self.set_pressed
        self.increase_button.when_pressed = self.increase_pressed
        self.decrease_button.when_pressed = self.decrease_pressed

    def set_pressed(self):
        self.counter = 0  # Sıfırla
        print("Set button pressed")

    def increase_pressed(self):
        self.counter += 1  # Artır
        print("Increase button pressed")

    def decrease_pressed(self):
        self.counter -= 1  # Azalt
        print("Decrease button pressed")

    def run(self):
        try:
            while True:
                # Her saniyede bir sayaç değerini göster
                print("Counter:", self.counter)
                time.sleep(1)
        except KeyboardInterrupt:
            print("Program sonlandırılıyor...")



if __name__ == "__main__":
    germination_room = GerminationRoom()
    button_controller = ButtonController()

    try:
        while True:
            germination_room.show_settings_menu()


    except KeyboardInterrupt:
        print("Program is closed.")
