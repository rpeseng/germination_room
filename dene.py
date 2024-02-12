from RPLCD.i2c import CharLCD
from gpiozero import Button
import time

# LCD ekranını başlat
lcd = CharLCD('PCF8574', address=0x27, port=1)

# Buton pinlerini tanımla
UP_PIN = 16
DOWN_PIN = 18
ENTER_PIN = 26

# Butonları tanımla
up_button = Button(UP_PIN)
down_button = Button(DOWN_PIN)
enter_button = Button(ENTER_PIN)

# Ana menü ve alt menü gösterme fonksiyonları
def show_main_menu():
    while True:
        lcd.clear()
        lcd.cursor_pos = (0, 0)
        lcd.write_string("=== Ana Menu ===")
        lcd.cursor_pos = (1, 0)
        lcd.write_string("1. Value1 Ayarla")
        lcd.cursor_pos = (2, 0)
        lcd.write_string("2. Value2 Ayarla")
        lcd.cursor_pos = (3, 0)
        lcd.write_string("0. Cikis")
        time.sleep(0.5)

        if enter_button.is_pressed:
            selected_menu = select_submenu()
            selected_menu()
            time.sleep(0.2)  # Buton basılı tutulmasını engelle

def select_submenu():
    while True:
        lcd.clear()
        lcd.cursor_pos = (0, 0)
        lcd.write_string("Alt Menu secin")
        lcd.cursor_pos = (1, 0)
        lcd.write_string("1. Value1")
        lcd.cursor_pos = (2, 0)
        lcd.write_string("2. Value2")
        time.sleep(0.2)

        if up_button.is_pressed:
            return set_value1_menu
        elif down_button.is_pressed:
            return set_value2_menu

def set_value1_menu():
    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string("=== Value1 Ayarla ===")
    lcd.cursor_pos = (1, 0)
    lcd.write_string("1. Artır")
    lcd.cursor_pos = (2, 0)
    lcd.write_string("2. Azalt")
    lcd.cursor_pos = (3, 0)
    lcd.write_string("0. Geri")
    time.sleep(0.2)


    if enter_button.is_pressed:
        return

    while True:
        if up_button.is_pressed:
            increment_value1()
            time.sleep(0.2)  # Buton basılı tutulmasını engelle
        elif down_button.is_pressed:
            decrement_value1()
            time.sleep(0.2)  # Buton basılı tutulmasını engelle
        elif enter_button.is_pressed:
            break

def set_value2_menu():
    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string("=== Value2 Ayarla ===")
    lcd.cursor_pos = (1, 0)
    lcd.write_string("1. Artır")
    lcd.cursor_pos = (2, 0)
    lcd.write_string("2. Azalt\n")
    lcd.cursor_pos = (3, 0)
    lcd.write_string("0. Geri")
    time.sleep(0.1)

    if enter_button.is_pressed:
        return

    while True:
        if up_button.is_pressed:
            increment_value2()
            time.sleep(0.2)  # Buton basılı tutulmasını engelle
        elif down_button.is_pressed:
            decrement_value2()
            time.sleep(0.2)  # Buton basılı tutulmasını engelle
        elif enter_button.is_pressed:
            break

# Değerler
value1 = 0
value2 = 0

# Ekranı güncelleme fonksiyonu
def update_screen():
    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string("Value1: {}".format(value1))
    lcd.cursor_pos = (1, 0)
    lcd.write_string("Value2: {}".format(value2))
    time.sleep(0.05)

# Arttırma fonksiyonu
def increment_value1():
    global value1
    value1 += 1
    update_screen()

# Azaltma fonksiyonu
def decrement_value1():
    global value1
    value1 -= 1
    update_screen()

# Arttırma fonksiyonu
def increment_value2():
    global value2
    value2 += 1
    update_screen()

# Azaltma fonksiyonu
def decrement_value2():
    global value2
    value2 -= 1
    update_screen()

try:
    # Ana menüyü göster
    show_main_menu()

except KeyboardInterrupt:
    # Ctrl+C'ye basıldığında programı sonlandır
    pass
