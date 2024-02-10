from gpiozero import Button
import time
from RPLCD import CharLCD
from data.lcd_library import LCDController
from data.am2120_data import AM2120Sensor


# Menü seçenekleri
menu_items = ["set_temp_min", "set_temp_max", "set_hum_min", "set_hum_max"]
set_temp_min = 0
set_temp_max = 20
set_hum_min = 65
set_hum_max = 75


# I2C ayarları
i2c_address = 0x27  # Ekranınızın I2C adresini ayarlayın
i2c_bus = 1  # I2C veri yolunu ayarlayın (genellikle 1)

# Ekran boyutları
lcd_columns = 16
lcd_rows = 2


class Menu:
    def __init__(self, items):
        self.items = items
        self.selected_item = 0

    def show_menu(self, lcd):
        lcd.clear()
        for i in range(len(self.items)):
            if i == self.selected_item:
                lcd.cursor_pos = (i, 0)
                lcd.write("> ")
            lcd.write(self.items[i])

    def select_item(self):
        return self.items[self.selected_item]

    def move_up(self):
        self.selected_item = (self.selected_item - 1) % len(self.items)

    def move_down(self):
        self.selected_item = (self.selected_item + 1) % len(self.items)


class LCD:
    def __init__(self, i2c_address, i2c_bus, columns, rows):
        self.i2c_address = i2c_address
        self.i2c_bus = i2c_bus
        self.lcd = CharLCD(self.i2c_address, self.i2c_bus, columns=columns, rows=rows, i2c_expander="PCF8574")

    def clear(self):
        self.lcd.clear()

    def write(self, text):
        self.lcd.write(text)

    def cursor_pos(self, position):
        self.lcd.cursor_pos = position


# Değer ayarlama fonksiyonu
def set_value(item):
    lcd.clear()
    lcd.write(f"{item}: ")
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
lcd = LCD(i2c_address, i2c_bus, lcd_columns, lcd_rows)

# Ana döngü
while True:
    menu.show_menu(lcd)
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