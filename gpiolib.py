import RPi.GPIO as GPIO
import time
from data.lcd_library import LCDController
from data.am2120_data import AM2120Sensor

# Menü seçenekleri
menu_items = ["set_temp_min", "set_temp_max", "set_hum_min", "set_hum_max", "set_morning_time", "set_night_time", "back"]

# GPIO pin tanımlamaları
set_pin = 26
increase_pin = 16
decrease_pin = 18

# Buton durumlarını izlemek için GPIO pinlerini giriş olarak ayarla
GPIO.setmode(GPIO.BCM)
GPIO.setup(set_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(increase_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(decrease_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)




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



    def increase_pressed(self, channel):

        self.select_item = (self.select_item - 1) % len(self.items)
        print("increase button pressed")

    def decrease_pressed(self, channel):

        self.select_item = (self.select_item + 1) % len(self.items)
        print("Decrease button pressed")

    def set_pressed(self, channel):

        print("set button pressed")


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
                    if GPIO.input(increase_pin) == GPIO.LOW:
                        self.increase_pressed(increase_pin)
                        time.sleep(0.1)
                    if GPIO.input(decrease_pin) == GPIO.LOW:
                        self.decrease_pressed(decrease_pin)
                        time.sleep(0.1)
                    if GPIO.input(set_pin) == GPIO.LOW:
                        time.sleep(0.1)
                        self.set_pressed(set_pin)
                        self.show_values()
                        return


                    time.sleep(0.15)
        except KeyboardInterrupt:
            self.cleanup()


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
                    if GPIO.input(increase_pin) == GPIO.LOW:
                        setattr(self, f"set_{self.items[self.select_item]}", self.set_temp_min + 1)
                        time.sleep(0.1)
                    if GPIO.input(decrease_pin) == GPIO.LOW:
                        setattr(self, f"set_{self.items[self.select_item]}", self.set_temp_min - 1)
                        time.sleep(0.1)
                    if GPIO.input(set_pin) == GPIO.LOW:
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
                    if GPIO.input(increase_pin) == GPIO.LOW:
                        setattr(self, f"set_{self.items[self.select_item]}", self.set_temp_min + 1)
                        time.sleep(0.1)
                    if GPIO.input(decrease_pin) == GPIO.LOW:
                        setattr(self, f"set_{self.items[self.select_item]}", self.set_temp_min - 1)
                        time.sleep(0.1)
                    if GPIO.input(set_pin) == GPIO.LOW:
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
                    if GPIO.input(increase_pin) == GPIO.LOW:
                        setattr(self, f"set_{self.items[self.select_item]}", self.set_temp_min + 1)
                        time.sleep(0.1)
                    if GPIO.input(decrease_pin) == GPIO.LOW:
                        setattr(self, f"set_{self.items[self.select_item]}", self.set_temp_min - 1)
                        time.sleep(0.1)
                    if GPIO.input(set_pin) == GPIO.LOW:
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
                    if GPIO.input(increase_pin) == GPIO.LOW:
                        setattr(self, f"set_{self.items[self.select_item]}", self.set_temp_min + 1)
                        time.sleep(0.1)
                    if GPIO.input(decrease_pin) == GPIO.LOW:
                        setattr(self, f"set_{self.items[self.select_item]}", self.set_temp_min - 1)
                        time.sleep(0.1)
                    if GPIO.input(set_pin) == GPIO.LOW:
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
                    self.lcd.write(str(self.set_hum_max))
                    time.sleep(0.1)
                    if GPIO.input(increase_pin) == GPIO.LOW:
                        setattr(self, f"set_{self.items[self.select_item]}", self.set_temp_min + 1)
                        time.sleep(0.1)
                    if GPIO.input(decrease_pin) == GPIO.LOW:
                        setattr(self, f"set_{self.items[self.select_item]}", self.set_temp_min - 1)
                        time.sleep(0.1)
                    if GPIO.input(set_pin) == GPIO.LOW:
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
                    self.lcd.write(str(self.set_hum_max))
                    time.sleep(0.1)
                    if GPIO.input(increase_pin) == GPIO.LOW:
                        setattr(self, f"set_{self.items[self.select_item]}", self.set_temp_min + 1)
                        time.sleep(0.1)
                    if GPIO.input(decrease_pin) == GPIO.LOW:
                        setattr(self, f"set_{self.items[self.select_item]}", self.set_temp_min - 1)
                        time.sleep(0.1)
                    if GPIO.input(set_pin) == GPIO.LOW:
                        time.sleep(0.1)
                        self.show_menu()
                        break
                if self.select_item == 6:
                    if GPIO.input(set_pin) == GPIO.LOW:
                        time.sleep(0.1)
                        self.show_values()
                        break
                time.sleep(0.15)

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
                self.lcd.write(f"    NEM      : {hum_value:.2f}")
                time.sleep(0.2)
                if GPIO.input(decrease_pin) == GPIO.LOW or GPIO.input(increase_pin) == GPIO.LOW or GPIO.input(
                        set_pin) == GPIO.LOW:
                    self.select_item = 0
                    self.show_menu()
                    return


        except KeyboardInterrupt:
            self.cleanup()

        except Exception as er:
            print(f"Hataa : {er}")


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

