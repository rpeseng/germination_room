import RPi.GPIO as GPIO
from RPLCD import CharLCD
import curses

# LCD ayarları
lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])

# Buton pinleri
up_button_pin = 11
down_button_pin = 13
enter_button_pin = 15

# GPIO ayarları
GPIO.setmode(GPIO.BOARD)
GPIO.setup(up_button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(down_button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(enter_button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Değer: 0")

    value = 0

    while True:
        if not GPIO.input(up_button_pin):
            value += 1
        elif not GPIO.input(down_button_pin):
            value -= 1
        elif not GPIO.input(enter_button_pin):
            lcd.clear()
            lcd.write_string(f"Değer: {value}")
            stdscr.addstr(1, 0, f"Değer: {value}")

        lcd.clear()
        lcd.write_string(f"Değer: {value}")
        stdscr.addstr(1, 0, f"Değer: {value}")

curses.wrapper(main)
