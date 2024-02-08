import Adafruit_DHT
import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO
import time

# GPIO pin tanımlamaları
BUTTON_1_PIN = 17  # Ayarlar menüsüne giriş için buton
BUTTON_2_PIN = 27  # Değeri azaltmak için buton
BUTTON_3_PIN = 22  # Değeri artırmak için buton

# DHT11 sensörü için pin tanımlaması
DHT_SENSOR_PIN = 4
DHT_SENSOR_TYPE = Adafruit_DHT.DHT11

# Fan kontrolü için pin tanımlaması
FAN_PIN = 18

# LCD ekran tanımlamaları
lcd_columns = 16
lcd_rows = 2
lcd = LCD.Adafruit_CharLCDPlate()

# Ayarlanacak sıcaklık ve nem değerleri
hedef_sicaklik = 25
hedef_nem = 50

# GPIO ayarları
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_1_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_2_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_3_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(FAN_PIN, GPIO.OUT)

# Fanı başlat
GPIO.output(FAN_PIN, GPIO.HIGH)

def okuma():
    # DHT11 sensöründen sıcaklık ve nem değerlerini oku
    nem, sicaklik = Adafruit_DHT.read_retry(DHT_SENSOR_TYPE, DHT_SENSOR_PIN)
    return nem, sicaklik

def fan_kontrol():
    global hedef_sicaklik, hedef_nem
    nem, sicaklik = okuma()

    # Sıcaklık kontrolü
    if sicaklik > hedef_sicaklik:
        GPIO.output(FAN_PIN, GPIO.LOW)
    else:
        GPIO.output(FAN_PIN, GPIO.HIGH)

    # Nem kontrolü
    if nem > hedef_nem:
        GPIO.output(FAN_PIN, GPIO.LOW)
    else:
        GPIO.output(FAN_PIN, GPIO.HIGH)

def ayarlar_menu():
    global hedef_sicaklik, hedef_nem

    while True:
        lcd.clear()
        lcd.message("Ayarlar Menusu\n")
        lcd.message("1. Sicaklik: {}\n2. Nem: {}".format(hedef_sicaklik, hedef_nem))

        while True:
            if not GPIO.input(BUTTON_1_PIN):
                lcd.clear()
                lcd.message("Sicaklik Secimi\n")
                while GPIO.input(BUTTON_1_PIN):
                    pass
                ayar_secim(1)
                break
            elif not GPIO.input(BUTTON_2_PIN):
                ayar_secim(2)
            elif not GPIO.input(BUTTON_3_PIN):
                ayar_secim(3)

def ayar_secim(secim):
    global hedef_sicaklik, hedef_nem

    deger = None
    lcd.clear()
    lcd.message("Deger Secimi\n")

    while True:
        if secim == 1:
            lcd.message("Sicaklik: ")
        elif secim == 2:
            lcd.message("Nem: ")

        lcd.set_cursor(0, 1)
        lcd.message(str(deger) if deger is not None else "")

        if not GPIO.input(BUTTON_2_PIN):
            deger -= 1
        elif not GPIO.input(BUTTON_3_PIN):
            deger += 1

        lcd.set_cursor(0, 1)
        lcd.message(str(deger) if deger is not None else "")

        time.sleep(0.2)

        if GPIO.input(BUTTON_1_PIN):
            if secim == 1:
                hedef_sicaklik = deger if deger is not None else hedef_sicaklik
            elif secim == 2:
                hedef_nem = deger if deger is not None else hedef_nem
            break

def main():
    try:
        while True:
            fan_kontrol()
            nem, sicaklik = okuma()
            lcd.clear()
            lcd.message("Sicaklik: {:.2f}C\nNem: {:.2f}%".format(sicaklik, nem))
            time.sleep(2)

    except KeyboardInterrupt:
        pass

    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    try:
        ayarlar_menu_thread = threading.Thread(target=ayarlar_menu)
        ayarlar_menu_thread.start()
        main()

    except KeyboardInterrupt:
        pass

    finally:
        GPIO.cleanup()
