from gpiozero import Button
import time
from data.lcd_library import LCDController
from data.am2120_data import AM2120Sensor

# Menü seçenekleri
menu_items = ["set_temp_min", "set_temp_max", "set_hum_min", "set_hum_max", "back"]

set_pin = Button(26)
increase_pin = Button(16)
decrease_pin = Button(18)


class ButtonController:
    def __init__(self):
        self.items = menu_items
        self.select_item = 0
        self.lcd = LCDController()
        self.am2120sensorvalues = AM2120Sensor()

        self.set_temp_min = 2
        self.set_temp_max = 20
        self.set_hum_min = 65
        self.set_hum_max = 75

    def increase_pressed(self):
        self.select_item = (self.select_item - 1) % len(self.items)

    def decrease_pressed(self):
        self.select_item = (self.select_item + 1) % len(self.items)

    """def set_pressed(self):
        self.show_sub_menu(self.select_item)"""

    def show_menu(self):
        try:
            while True:
                self.render_menu()
                time.sleep(0.2)
        except KeyboardInterrupt:
            self.cleanup()

    def render_menu(self):
        self.lcd.clear_screen()
        self.lcd.write("====  Menu  ====")
        for i, item in enumerate(self.items):
            if i == self.select_item:
                self.lcd.write(f"> {item}")
            else:
                self.lcd.write(item)
        time.sleep(0.1)

    def show_sub_menu(self, item_index):
        options = [
            ("set_temp_min", "Set Degeri =", self.set_temp_min),
            ("set_temp_max", "Set Degeri =", self.set_temp_max),
            ("set_hum_min", "Set Degeri =", self.set_hum_min),
            ("set_hum_max", "Set Degeri =", self.set_hum_max),
        ]
        option_name, prefix, value = options[item_index]
        try:
            while True:
                self.lcd.clear_screen()
                self.lcd.cursor_pos = (0, 0)
                self.lcd.write(f"====  Menu  ====")
                self.lcd.cursor_pos = (1, 0)
                self.lcd.write(f"> {option_name}")
                self.lcd.cursor_pos = (2, 0)
                self.lcd.write(f"{prefix} {value}")
                time.sleep(0.2)
                if increase_pin.is_pressed:
                    value += 1
                    time.sleep(0.1)
                elif decrease_pin.is_pressed:
                    value -= 1
                    time.sleep(0.1)
                elif set_pin.is_pressed:
                    time.sleep(0.1)
                    return
        except KeyboardInterrupt:
            self.cleanup()

    def show_values(self):
        try:
            while True:
                temp_value, hum_value = self.am2120sensorvalues.read_am2120_values()
                self.lcd.clear_screen()
                self.lcd.cursor_pos = (0, 0)
                self.lcd.write("=== ORTAM DEGERI ===")
                self.lcd.cursor_pos = (1, 0)
                self.lcd.write(f"SICAKLIK : {temp_value:.2f}")
                self.lcd.cursor_pos = (2, 0)
                self.lcd.write(f"NEM      : {hum_value:.2f}")
                time.sleep(0.2)
                if decrease_pin.is_pressed or increase_pin.is_pressed or set_pin.is_pressed:
                    self.show_menu()
                    return
        except KeyboardInterrupt:
            self.cleanup()

    def cleanup(self):
        self.lcd.clear_screen()
        self.lcd.lcd_screen_deactivate()


def main():
    button_controller = ButtonController()
    try:
        button_controller.show_values()
    except Exception as error:
        button_controller.cleanup()
        print(f"Hata: {error}")


if __name__ == "__main__":
    main()
