import RPi.GPIO as GPIO
import time
from data.lcd_library import I2CLcd
from data.am2320_data import AM2120Sensor

class GerminationRoom:
    def __init__(self):
        self.value = 0
        self.selected_option = 1
        self.lcd = I2CLcd()
        self.temp_and_humudity = AM2120Sensor()

        # Raspberry Pi GPIO konfigürasyonu
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # 17. pin: Arttır butonu
        GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # 27. pin: Azalt butonu
        GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # 22. pin: Ayarlar Menüsü butonu

    def show_main_screen(self):
        temp = self.temp_and_humudity.read_temperature()
        humudity = self.temp_and_humudity.read_humidity()

        self.lcd.lcd_set_text(1, "ORTAM DEGERLERI")
        self.lcd.lcd_set_text(2, f"Sıcaklık: {temp}")
        self.lcd.lcd_set_text(2, f"Nem     : {humudity}")
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
            self.lcd.lcd_set_text(4, options[self.selected_option - 1])

            if self.selected_option == 1:
                print("Ana Menü seçildi")
            elif self.selected_option == 2:
                print("Nem Değeri seçildi")
            elif self.selected_option == 3:
                print("Sıcaklık Değeri seçildi")
            elif self.selected_option == 4:
                print("Çıkış seçildi")
                break

    def get_selected_option(self, options):
        current_option = 1

        while True:
            for idx, option in enumerate(options, start=1):
                print(f"{idx}. {option}")

            key = GPIO.wait_for_edge(22, GPIO.FALLING)

            if key == 22:
                return current_option

            current_option += 1
            if current_option > len(options):
                current_option = 1

            time.sleep(0.2)

if __name__ == "__main__":
    germination_room = GerminationRoom()

    try:
        while True:
            key_increase = GPIO.wait_for_edge(17, GPIO.FALLING)
            key_decrease = GPIO.wait_for_edge(27, GPIO.FALLING)
            key_settings = GPIO.wait_for_edge(22, GPIO.FALLING)

            if key_increase == 17:
                germination_room.increase_value()
            elif key_decrease == 27:
                germination_room.decrease_value()
            elif key_settings == 22:
                germination_room.show_settings_menu()

            time.sleep(0.2)

    except KeyboardInterrupt:
        GPIO.cleanup()
