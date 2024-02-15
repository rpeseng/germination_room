from gpiozero import Button
import time
from data.lcd_library import LCDController
from data.am2120_data import AM2120Sensor

# Menü seçenekleri
menu_items = ["set_temp_min", "set_temp_max", "set_hum_min", "set_hum_max", "back"]


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
        self.am2120sensorvalues = AM2120Sensor()

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
                            self.lcd.clear_screen()
                            self.lcd.lcd.cursor_pos = (0, 0)
                            self.lcd.write("====  Menu  ====")
                            self.lcd.lcd.cursor_pos = (1, 0)
                            self.lcd.write("> ")
                            self.lcd.write(self.items[i])
                            self.lcd.lcd.cursor_pos = (2, 2)
                            self.lcd.write(self.items[(i+1)])
                            self.lcd.lcd.cursor_pos = (3, 2)
                            self.lcd.write(self.items[(i+2)])
                        elif i == 1:
                            self.lcd.clear_screen()
                            self.lcd.lcd.cursor_pos = (0, 0)
                            self.lcd.write("====  Menu  ====")
                            self.lcd.lcd.cursor_pos = (1, 2)
                            self.lcd.write(self.items[i-1])
                            self.lcd.lcd.cursor_pos = (2, 0)
                            self.lcd.write("> ")
                            self.lcd.write(self.items[i])
                            self.lcd.lcd.cursor_pos = (3, 2)
                            self.lcd.write(self.items[i+1])
                        elif i == 2:
                            self.lcd.clear_screen()
                            self.lcd.lcd.cursor_pos = (0, 0)
                            self.lcd.write("====  Menu  ====")
                            self.lcd.lcd.cursor_pos = (1, 2)
                            self.lcd.write(self.items[i-2])
                            self.lcd.lcd.cursor_pos = (2, 2)
                            self.lcd.write(self.items[i-1])
                            self.lcd.lcd.cursor_pos = (3, 0)
                            self.lcd.write("> ")
                            self.lcd.write(self.items[i])
                        elif i == 3:
                            self.lcd.clear_screen()
                            self.lcd.lcd.cursor_pos = (0, 0)
                            self.lcd.write("====  Menu  ====")
                            self.lcd.lcd.cursor_pos = (1, 2)
                            self.lcd.write(self.items[i - 2])
                            self.lcd.lcd.cursor_pos = (2, 2)
                            self.lcd.write(self.items[i - 1])
                            self.lcd.lcd.cursor_pos = (3, 0)
                            self.lcd.write("> ")
                            self.lcd.write(self.items[i])
                        else:
                            self.lcd.clear_screen()
                            self.lcd.lcd.cursor_pos = (0, 0)
                            self.lcd.write("====  Menu  ====")
                            self.lcd.lcd.cursor_pos = (1, 2)
                            self.lcd.write(self.items[i - 3])
                            self.lcd.lcd.cursor_pos = (2, 2)
                            self.lcd.write(self.items[i - 3])
                            self.lcd.lcd.cursor_pos = (3, 0)
                            self.lcd.write("> ")
                            self.lcd.write(self.items[i])
                    if increase_pin.is_pressed:
                        self.increase_pressed()
                        time.sleep(0.15)
                    if decrease_pin.is_pressed:
                        self.decrease_pressed()
                        time.sleep(0.15)
                    if set_pin.is_pressed:
                        time.sleep(0.15)
                        self.show_sub_menu1()
                        return


                    time.sleep(0.15)
        except KeyboardInterrupt:
            self.lcd.clear_screen()
            self.lcd.lcd_screen_deactivate()


    def show_sub_menu1(self):
        try:
            while True:
                if self.select_item == 0:
                    self.lcd.clear_screen()
                    self.lcd.lcd.cursor_pos = (0, 0)
                    self.lcd.write("====  Menu  ====")
                    self.lcd.lcd.cursor_pos = (1, 0)
                    self.lcd.write("> ")
                    self.lcd.write(self.items[0])
                    self.lcd.lcd.cursor_pos = (2, 0)
                    self.lcd.write("Set Degeri =  ")
                    self.lcd.write(str(self.set_temp_min))
                    time.sleep(0.15)
                    if increase_pin.is_pressed:
                        self.set_temp_min += 1
                        time.sleep(0.15)
                    if decrease_pin.is_pressed:
                        self.set_temp_min -= 1
                        time.sleep(0.15)
                    if set_pin.is_pressed:
                        time.sleep(0.15)
                        self.show_menu()
                        break
                if self.select_item == 1:
                    self.lcd.clear_screen()
                    self.lcd.lcd.cursor_pos = (0, 0)
                    self.lcd.write("====  Menu  ====")
                    self.lcd.lcd.cursor_pos = (1, 0)
                    self.lcd.write("> ")
                    self.lcd.write(self.items[1])
                    self.lcd.lcd.cursor_pos = (2, 0)
                    self.lcd.write("Set Degeri =  ")
                    self.lcd.write(str(self.set_temp_max))
                    time.sleep(0.15)
                    if increase_pin.is_pressed:
                        self.set_temp_max += 1
                        time.sleep(0.15)
                    if decrease_pin.is_pressed:
                        self.set_temp_max -= 1
                        time.sleep(0.15)
                    if set_pin.is_pressed:
                        time.sleep(0.15)
                        self.show_menu()
                        break
                if self.select_item == 2:
                    self.lcd.clear_screen()
                    self.lcd.lcd.cursor_pos = (0, 0)
                    self.lcd.write("====  Menu  ====")
                    self.lcd.lcd.cursor_pos = (1, 0)
                    self.lcd.write("> ")
                    self.lcd.write(self.items[2])
                    self.lcd.lcd.cursor_pos = (2, 0)
                    self.lcd.write("Set Degeri =  ")
                    self.lcd.write(str(self.set_hum_min))
                    time.sleep(0.15)
                    if increase_pin.is_pressed:
                        self.set_hum_min += 1
                        time.sleep(0.15)
                    if decrease_pin.is_pressed:
                        self.set_hum_min -= 1
                        time.sleep(0.15)
                    if set_pin.is_pressed:
                        time.sleep(0.15)
                        self.show_menu()
                        break
                if self.select_item == 3:
                    self.lcd.clear_screen()
                    self.lcd.lcd.cursor_pos = (0, 0)
                    self.lcd.write("====  Menu  ====")
                    self.lcd.lcd.cursor_pos = (1, 0)
                    self.lcd.write("> ")
                    self.lcd.write(self.items[3])
                    self.lcd.lcd.cursor_pos = (2, 0)
                    self.lcd.write("Set Degeri =  ")
                    self.lcd.write(str(self.set_hum_max))
                    time.sleep(0.15)
                    if increase_pin.is_pressed:
                        self.set_hum_max += 1
                        time.sleep(0.15)
                    if decrease_pin.is_pressed:
                        self.set_hum_max -= 1
                        time.sleep(0.15)
                    if set_pin.is_pressed:
                        time.sleep(0.15)
                        self.show_menu()
                        break
                if self.select_item == 4:
                    if set_pin.is_pressed:
                        time.sleep(0.15)
                        self.show_values()
                        break
                time.sleep(0.15)

        except KeyboardInterrupt:
            self.lcd.clear_screen()
            self.lcd.lcd_screen_deactivate()


    def show_values(self):
        try:

            while True:
                sensor_values = self.am2120sensorvalues.read_am2120_values()
                temp_value = "{:.2f}".format(sensor_values[0])
                hum_value = "{:.2f}".format(sensor_values[1])

                self.lcd.clear_screen()
                self.lcd.lcd.cursor_pos = (0, 0)
                self.lcd.write("=== ORTAM DEGERI ===")
                self.lcd.lcd.cursor_pos = (1, 0)
                self.lcd.write("SICAKLIK :")
                self.lcd.lcd.cursor_pos = (1, 12)
                self.lcd.write(temp_value)
                self.lcd.lcd.cursor_pos = (2, 0)
                self.lcd.write("NEM      :")
                self.lcd.lcd.cursor_pos = (2, 12)
                self.lcd.write(hum_value)

                if set_pin.is_pressed:
                    time.sleep(0.15)
                    self.show_menu()
                    return
                time.sleep(0.2)

        except Exception as er:
            print(f"Hataa : {er}")


def main():
    # ButonController sınıfını kullanarak nesne oluştur
    button_controller = ButtonController()
    try:
        button_controller.show_values()

    except Exception as error:
        button_controller.lcd.lcd_screen_deactivate()
        print(f"hata: {error}")


if __name__ == "__main__":
    main()

