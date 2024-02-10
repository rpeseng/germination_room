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




class Menu:
    def __init__(self, items):
        self.items = items
        self.selected_item = 0
        self.lcd = LCDController()

    def show_menu(self, lcd):
        self.lcd.clear_screen()
        for i in range(len(self.items)):
            if i == self.selected_item:
                self.lcd.print_on_lcd(i, "> ")
            self.lcd.write_to_lcd(self.items[i])

    def select_item(self):
        return self.items[self.selected_item]

    def move_up(self):
        self.selected_item = (self.selected_item - 1) % len(self.items)

    def move_down(self):
        self.selected_item = (self.selected_item + 1) % len(self.items)





# Değer ayarlama fonksiyonu
def set_value(item):
    menu = Menu(menu_items)
    menu.lcd.clear_screen()
    menu.lcd.write_to_lcd(f"{item}: ")
    # Değer ayarlama kodunuzu buraya ekleyin
    # Örnek kod:
    new_value = input("Yeni değeri girin: ")
    # Değeri kaydedin


# Düğme pinleri
btn_up = 17
btn_down = 16
btn_select = 12

# Düğme nesneleri
btn_up = Button(btn_up)
btn_down = Button(btn_down)
btn_select = Button(btn_select)

# Menü ve LCD nesneleri
menu = Menu(menu_items)

# Ana döngü
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