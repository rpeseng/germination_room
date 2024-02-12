from gpiozero import Button
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

set_pin = Button(26)
increase_pin = Button(16)
decrease_pin = Button(18)


class ButtonController:
    def __init__(self):
        self.items = menu_items
        self.select_item = 0
        self.lcd = LCDController()

        self.set_temp_min = 2
        self.set_temp_max = 20
        self.set_hum_min = 65
        self.set_hum_max = 75

    def increase_pressed(self):

        self.select_item = (self.select_item - 1) % len(self.items)
        print("increase button pressed")

    def decrease_pressed(self):

        self.select_item = (self.select_item + 1) % len(self.items)
        print("Decrease button pressed")



    def show_menu(self):
        try:
            while True:
                for i in range(len(self.items)):
                    if i == self.select_item:
                        if i == 0:
                            self.lcd.lcd.cursor_pos = (0, 0)
                            self.lcd.write("Menu")
                            self.lcd.lcd.cursor_pos = (1, 0)
                            self.lcd.write("> ")
                            self.lcd.write(self.items[i])
                        elif i == 1:
                            self.lcd.clear_screen()
                            self.lcd.lcd.cursor_pos = (0, 0)
                            self.lcd.write("Menu")
                            self.lcd.lcd.cursor_pos = (1, 0)
                            self.lcd.write("> ")
                            self.lcd.write(self.items[i])
                        elif i == 2:
                            self.lcd.clear_screen()
                            self.lcd.lcd.cursor_pos = (0, 0)
                            self.lcd.write("Menu")
                            self.lcd.lcd.cursor_pos = (1, 0)
                            self.lcd.write("> ")
                            self.lcd.write(self.items[i])
                        else:
                            self.lcd.clear_screen()
                            self.lcd.lcd.cursor_pos = (0, 0)
                            self.lcd.write("Menu")
                            self.lcd.lcd.cursor_pos = (1, 0)
                            self.lcd.write("> ")
                            self.lcd.write(self.items[i])
                    if increase_pin.is_pressed:
                        self.increase_pressed()
                        time.sleep(0.15)
                    if decrease_pin.is_pressed:
                        self.decrease_pressed()
                        time.sleep(0.15)
                    if set_pin.is_pressed:
                        if self.select_item == 0:
                            return self.show_sub_menu1()

                        time.sleep(0.15)
                    time.sleep(0.1)
        except KeyboardInterrupt:
            self.lcd.clear_screen()
            self.lcd.lcd_screen_deactivate()


    def show_sub_menu1(self):
        try:
            while True:
                if self.select_item == 0:
                    self.lcd.clear_screen()
                    self.lcd.lcd.cursor_pos = (0, 0)
                    self.lcd.write("Menu")
                    self.lcd.lcd.cursor_pos = (1, 0)
                    self.lcd.write("> ")
                    self.lcd.write(self.items[0])
                    self.lcd.lcd.cursor_pos = (2, 0)
                    self.lcd.write("Set Degeri =  ")
                    self.lcd.write(str(self.set_temp_min))
                if increase_pin.is_pressed:
                    self.set_temp_min += 1
                    time.sleep(0.15)
                if decrease_pin.is_pressed:
                    self.set_temp_min -= 1
                    time.sleep(0.15)
                if set_pin.is_pressed:
                    time.sleep(0.15)
                    print("Basildi")
                    return self.show_menu()
                time.sleep(0.1)

        except KeyboardInterrupt:
            self.lcd.clear_screen()
            self.lcd.lcd_screen_deactivate()


def main():
    # ButonController sınıfını kullanarak nesne oluştur
    button_controller = ButtonController()

    try:
        button_controller.show_menu()


    except Exception as error:
        button_controller.lcd.lcd_screen_deactivate()
        print(f"hata: {error}")


if __name__ == "__main__":
    main()

