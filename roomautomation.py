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
        self.items = 0
        self.lcd = LCDController()
        self.temp_and_humudity = AM2120Sensor()


    def show_main_screen(self):
        values = self.temp_and_humudity.read_am2120_values()
        temp = values[0]
        humudity = values[1]

        self.lcd.print_on_lcd(1, "ORTAM DEGERLERI")
        self.lcd.print_on_lcd(2, f"Sıcaklık: {temp}")
        self.lcd.print_on_lcd(3, f"Nem     : {humudity}")
        time.sleep(2)


    def increase_button(self):
        self.items = (self.items - 1) % len(menu_items)
        self.show_main_screen()

    def decrease_button(self):
        self.items = (self.items + 1) % len(menu_items)
        self.show_main_screen()

    def select_item(self):
        return self.items[self.items]


    def show_settings_menu(self):
        print("Ayarlar Menüsü")
        options = ["Ana Menü", "Nem Değeri", "Sıcaklık Değeri", "Çıkış"]

        while True:
            for i in range(len(menu_items)):
                self.items
                self.lcd.print_on_lcd(4, options[self.items - 1])

            if self.items == 1:
                print("set_temp_min")

            elif self.items == 2:
                print("Nem Değeri seçildi")
            elif self.items == 3:
                print("Sıcaklık Değeri seçildi")
            elif self.items == 4:
                print("Çıkış seçildi")
                break



class Menu:
    def __init__(self, items):
        self.items = items
        self.selected_item = 0
        self.ger = GerminationRoom()

    def show_menu(self):
        self.ger.lcd.clear_screen()
        for i in range(len(self.items)):
            if i == self.selected_item:
                self.ger.lcd.print_on_lcd(i, "> ")
            self.ger.lcd.print_on_lcd(self.items[i])

    def select_item(self):
        return self.items[self.selected_item]

    def move_up(self):
        self.selected_item = (self.selected_item - 1) % len(self.items)

    def move_down(self):
        self.selected_item = (self.selected_item + 1) % len(self.items)




# GPIO pin numaraları
SET_PIN = 26
INCREASE_PIN = 18
DECREASE_PIN = 21

# Butonlar
btn_select = Button(SET_PIN)
btn_up = Button(INCREASE_PIN)
btn_down = Button(DECREASE_PIN)

if __name__ == "__main__":
    germination_room = GerminationRoom()
    button_controller = Menu(germination_room)
    menu = Menu(menu_items)
    try:
        while True:
            menu.show_menu()
            # Ekran güncelleme kodunuzu buraya ekleyin
            # Örnek kod:
            time.sleep(0.1)

            # Düğme olaylarını işleyin
            if btn_up.is_pressed:
                menu.move_up()
            elif btn_down.is_pressed:
                menu.move_down()
            elif btn_select.is_pressed:
                selected_item = menu.select_item()
                set_value(selected_item)

    except KeyboardInterrupt:
        print("Program is closed.")
