from gpiozero import Button
import time
from data.lcd_library import LCDController
from data.am2120_data import AM2120Sensor
from data.sql_connection import SqlSettings

# Menü seçenekleri
menu_items = ["set_temp_min", "set_temp_max", "set_hum_min",
              "set_hum_max", "set_morning_time", "set_night_time", "back"]

set_pin = Button(17)
increase_pin = Button(27)
decrease_pin = Button(22)


class ButtonController:
    def __init__(self):
        self.items = menu_items
        self.select_item = 0
        self.lcd = LCDController()
        self.am2120sensorvalues = AM2120Sensor()
        self.sqlvalues = SqlSettings()

        self.set_temp_min = 2
        self.set_temp_max = 20
        self.set_hum_min = 65
        self.set_hum_max = 75
        self.set_morning_time = float(08.00)
        self.set_night_time = float(18.00)

    def read_set_values(self):
        set_values = self.sqlvalues.read_set_values()
        if set_values is None:
            self.sqlvalues.insert_set_values(2, 20, 65, 75)
        else:
            self.set_temp_min = set_values[1]
            self.set_temp_max = set_values[2]
            self.set_hum_min = set_values[3]
            self.set_hum_max = set_values[4]

    def read_set_times(self):
        set_times = self.sqlvalues.read_set_update_times()
        if set_times is None:
            self.sqlvalues.insert_set_times(08.00, 18.00)
        else:
            self.set_morning_time = float(set_times[1])
            self.set_night_time = float(set_times[2])

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
                        elif i == 4:
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
                        elif i == 5:
                            self.lcd.clear_screen()
                            self.lcd.lcd.cursor_pos = (0, 0)
                            self.lcd.write("====  Menu  ====")
                            self.lcd.lcd.cursor_pos = (1, 2)
                            self.lcd.write(self.items[i - 3])
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
                            self.lcd.write(self.items[i -2])
                            self.lcd.lcd.cursor_pos = (2, 2)
                            self.lcd.write(self.items[i - 1])
                            self.lcd.lcd.cursor_pos = (3, 0)
                            self.lcd.write("> ")
                            self.lcd.write(self.items[i])
                    if increase_pin.is_pressed:
                        self.increase_pressed()
                        time.sleep(0.1)
                    if decrease_pin.is_pressed:
                        self.decrease_pressed()
                        time.sleep(0.1)
                    if set_pin.is_pressed:
                        time.sleep(0.1)
                        self.show_sub_menu1()
                        return


                    time.sleep(0.15)
        except KeyboardInterrupt:
            self.cleanup()


    def show_sub_menu1(self):
        try:
            self.read_set_values()
            self.read_set_times()
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
                        time.sleep(0.1)
                    if decrease_pin.is_pressed:
                        self.set_temp_min -= 1
                        time.sleep(0.1)
                    if set_pin.is_pressed:
                        self.sqlvalues.insert_set_values(self.set_temp_min, self.set_temp_max, self.set_hum_min, self.set_hum_max)
                        time.sleep(0.1)
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
                    time.sleep(0.1)
                    if increase_pin.is_pressed:
                        self.set_temp_max += 1
                        time.sleep(0.1)
                    if decrease_pin.is_pressed:
                        self.set_temp_max -= 1
                        time.sleep(0.1)
                    if set_pin.is_pressed:
                        self.sqlvalues.insert_set_values(self.set_temp_min, self.set_temp_max, self.set_hum_min,
                                                         self.set_hum_max)
                        time.sleep(0.1)
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
                    time.sleep(0.1)
                    if increase_pin.is_pressed:
                        self.set_hum_min += 1
                        time.sleep(0.1)
                    if decrease_pin.is_pressed:
                        self.set_hum_min -= 1
                        time.sleep(0.1)
                    if set_pin.is_pressed:
                        self.sqlvalues.insert_set_values(self.set_temp_min, self.set_temp_max, self.set_hum_min,
                                                         self.set_hum_max)
                        time.sleep(0.1)
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
                    time.sleep(0.1)
                    if increase_pin.is_pressed:
                        self.set_hum_max += 1
                        time.sleep(0.1)
                    if decrease_pin.is_pressed:
                        self.set_hum_max -= 1
                        time.sleep(0.1)
                    if set_pin.is_pressed:
                        self.sqlvalues.insert_set_values(self.set_temp_min, self.set_temp_max, self.set_hum_min,
                                                         self.set_hum_max)
                        time.sleep(0.1)
                        self.show_menu()
                        break
                if self.select_item == 4:
                    self.lcd.clear_screen()
                    self.lcd.lcd.cursor_pos = (0, 0)
                    self.lcd.write("====  Menu  ====")
                    self.lcd.lcd.cursor_pos = (1, 0)
                    self.lcd.write("> ")
                    self.lcd.write(self.items[3])
                    self.lcd.lcd.cursor_pos = (2, 0)
                    self.lcd.write("Set Degeri =  ")
                    self.lcd.write(str(self.set_morning_time))
                    time.sleep(0.1)
                    if increase_pin.is_pressed:
                        self.set_morning_time += 0.1
                        time.sleep(0.1)
                    if decrease_pin.is_pressed:
                        self.set_morning_time -= 0.1
                        time.sleep(0.1)
                    if set_pin.is_pressed:
                        self.sqlvalues.set_update_time(str(self.set_morning_time), str(self.set_night_time))
                        time.sleep(0.1)
                        self.show_menu()
                        break
                if self.select_item == 5:
                    self.lcd.clear_screen()
                    self.lcd.lcd.cursor_pos = (0, 0)
                    self.lcd.write("====  Menu  ====")
                    self.lcd.lcd.cursor_pos = (1, 0)
                    self.lcd.write("> ")
                    self.lcd.write(self.items[3])
                    self.lcd.lcd.cursor_pos = (2, 0)
                    self.lcd.write("Set Degeri =  ")
                    self.lcd.write(str(self.set_night_time))
                    time.sleep(0.1)
                    if increase_pin.is_pressed:
                        self.set_night_time += 0.1
                        time.sleep(0.1)
                    if decrease_pin.is_pressed:
                        self.set_night_time -= 0.1
                        time.sleep(0.1)
                    if set_pin.is_pressed:
                        self.sqlvalues.set_update_time(str(self.set_morning_time), str(self.set_night_time))
                        time.sleep(0.1)
                        self.show_menu()
                        break
                if self.select_item == 6:
                    if set_pin.is_pressed:
                        time.sleep(0.1)
                        self.show_values()
                        break
                time.sleep(0.15)

        except KeyboardInterrupt:
            self.cleanup()

    def show_values(self):
        try:
            while True:
                values = self.sqlvalues.read_values_lcd()
                data_time = values[3][:-3]

                self.lcd.clear_screen()
                self.lcd.lcd.cursor_pos = (0, 0)
                self.lcd.write("=== ORTAM DEGERI ===")
                self.lcd.lcd.cursor_pos = (1, 0)
                self.lcd.write(f"SICAKLIK : {values[1]}")
                self.lcd.lcd.cursor_pos = (2, 0)
                self.lcd.write(f"NEM      : {values[2]}")
                self.lcd.lcd.cursor_pos = (3, 0)
                self.lcd.write(f"{data_time}")

                time.sleep(0.2)
                if decrease_pin.is_pressed or increase_pin.is_pressed or set_pin.is_pressed:
                    self.select_item = 0
                    self.show_menu()
                    return

        except KeyboardInterrupt:
            self.cleanup()

        except Exception as er:
            print(f"Hata show values : {er}")

    def cleanup(self):
        self.lcd.clear_screen()
        self.lcd.lcd_screen_deactivate()
def main():

    # ButonController sınıfını kullanarak nesne oluştur
    button_controller = ButtonController()
    try:
        button_controller.show_values()

    except Exception as error:
        button_controller.cleanup()
        print(f"hata: {error}")


if __name__ == "__main__":
    main()

