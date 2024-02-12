import RPi.GPIO as GPIO
from RPLCD import i2c

# Buton Pinleri
BUTTON_UP = 23
BUTTON_DOWN = 24
BUTTON_SELECT = 25

# LCD Ekran I2C Adresi
LCD_ADDRESS = 0x3f

# Ekran Boyutları
LCD_WIDTH = 16
LCD_HEIGHT = 2

# Menü Seçenekleri
MENU_OPTIONS = ["Setting Set Value", "About", "Exit"]
SUBMENU_OPTIONS = ["Set Hum Value", "Set Temp Value", "Back"]

# Değişkenler
current_menu = 0
current_submenu = 0
set_hum_value = 50
set_temp_value = 20

# GPIO Kurulumu
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_UP, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_DOWN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_SELECT, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# LCD Ekran Kurulumu
lcd = i2c(LCD_ADDRESS, LCD_WIDTH, LCD_HEIGHT)

# Fonksiyonlar
def display_menu():
  lcd.clear()
  for i in range(len(MENU_OPTIONS)):
    if i == current_menu:
      lcd.cursor_pos((0, i))
      lcd.write("> ")
    lcd.write(MENU_OPTIONS[i])

def display_submenu():
  lcd.clear()
  for i in range(len(SUBMENU_OPTIONS)):
    if i == current_submenu:
      lcd.cursor_pos((0, i))
      lcd.write("> ")
    lcd.write(SUBMENU_OPTIONS[i])

def set_hum_value_up():
  global set_hum_value
  set_hum_value += 1
  if set_hum_value > 100:
    set_hum_value = 100

def set_hum_value_down():
  global set_hum_value
  set_hum_value -= 1
  if set_hum_value < 0:
    set_hum_value = 0

def set_temp_value_up():
  global set_temp_value
  set_temp_value += 1
  if set_temp_value > 30:
    set_temp_value = 30

def set_temp_value_down():
  global set_temp_value
  set_temp_value -= 1
  if set_temp_value < 10:
    set_temp_value = 10

try:
    # Ana Döngü
    while True:
      # Buton Basma Olayları
      if GPIO.input(BUTTON_UP) == GPIO.LOW:
        if current_menu == 0:
          current_submenu = 0
          display_submenu()
        elif current_menu == 1:
          # Hakkında Bilgileri Göster
          pass
        elif current_menu == 2:
          # Çıkış
          break
      elif GPIO.input(BUTTON_DOWN) == GPIO.LOW:
        if current_menu == 0:
          current_submenu = 0
          display_submenu()
        elif current_menu == 1:
          # Hakkında Bilgileri Göster
          pass
        elif current_menu == 2:
          # Çıkış
          break
      elif GPIO.input(BUTTON_SELECT) == GPIO.LOW:
        if current_menu == 0:
          if current_submenu == 0:
            # Nem Değerini Ayarla
            pass
          elif current_submenu == 1:
            # Sıcaklık Değerini Ayarla
            pass
          elif current_submenu == 2:
            current_menu = 0
            display_menu()
        elif current_menu == 1:
          # Hakkında Bilgileri Göster
          pass
        elif current_menu == 2:
            print("qqq")
          # Çık
except:
    print("hata")