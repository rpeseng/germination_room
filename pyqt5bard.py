#Try RPLCD Liberary
# from RPLCD-master import *
# from RPLCD import RPLCD
from RPLCD import *
from time import sleep
from RPLCD.i2c import CharLCD
lcd = CharLCD('PCF8574', 0x27)
lcd.cursor_pos = (0, 5)
lcd.write_string('Wlcomme to')
lcd.cursor_pos = (1, 3)
lcd.write_string('Circuit Digest')
sleep(2)
framebuffer = [
        '',
        '',
        ]
def write_to_lcd(lcd, framebuffer, num_cols):
        """Write the framebuffer out to the specified LCD."""
        lcd.home()
        for row in framebuffer:
            lcd.write_string(row.ljust(num_cols)[:num_cols])
            lcd.write_string('\r\n')
def long_text(text):
        if len(text)<20:
            lcd.write_string(text)
        for i in range(len(text) - 20 + 1):
            framebuffer[1] = text[i:i+20]
            write_to_lcd(lcd, framebuffer, 20)
            sleep(0.2)
face_LB=(
  0b10000,
  0b10100,
  0b10011,
  0b10000,
  0b11100,
  0b11111,
  0b01111,
  0b00111
    )
face_LT=(
  0b10111,
  0b10111,
  0b01000,
  0b01000,
  0b10000,
  0b10001,
  0b10001,
  0b10000
)
face_RT=(
  0b10101,
  0b11101,
  0b00010,
  0b00010,
  0b00001,
  0b10001,
  0b10001,
  0b00001
)
face_RB=(
  0b00001,
  0b00101,
  0b11001,
  0b00001,
  0b01111,
  0b11111,
  0b11110,
  0b11100
)
battery_EMP = (
  0b00000,
  0b01110,
  0b11111,
  0b10001,
  0b10001,
  0b10001,
  0b10001,
  0b11111
)
battery_HLF = (
  0b00000,
  0b01110,
  0b11111,
  0b10001,
  0b10001,
  0b11111,
  0b11111,
  0b11111
)
battery_FULL = (
  0b00000,
  0b01110,
  0b11111,
  0b11111,
  0b11111,
  0b11111,
  0b11111,
  0b11111
)
Locked = (
  0b00000,
  0b01110,
  0b10001,
  0b10001,
  0b11111,
  0b11111,
  0b11011,
  0b11111
)
Un_Locked = (
  0b00000,
  0b01110,
  0b00001,
  0b00001,
  0b11111,
  0b11111,
  0b11011,
  0b11111
)
lcd.create_char(0, battery_EMP)
lcd.create_char(1, battery_HLF)
lcd.create_char(2, battery_FULL)
lcd.create_char(3, Locked)
# lcd.create_char(4, Un_Locked)
lcd.create_char(4, face_LT)
lcd.create_char(5, face_RT)
lcd.create_char(6, face_LB)
lcd.create_char(7, face_RB)
# U_L_Ch='\x04'
L_Ch='\x03'
B_F_Ch='\x02'
B_H_Ch='\x01'
B_E_Ch='\x00'
while 1:
    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string('Chargerging')
    lcd.cursor_pos = (0, 19)
    lcd.write_string(B_E_Ch)
    sleep(.4)
    lcd.cursor_pos = (0, 19)
    lcd.write_string(B_H_Ch)
    sleep(.4)
    lcd.cursor_pos = (0, 19)
    lcd.write_string(B_F_Ch)
    sleep(1)
    lcd.cursor_pos = (1, 0)
    long_text('This is a Scrolling text')
#     lcd.cursor_pos = (3, 19)
#     lcd.write_string(U_L_Ch)
#     sleep(.6)
    lcd.cursor_pos = (2, 4)
    lcd.write_string('\x04')
    lcd.cursor_pos = (2, 5)
    lcd.write_string('\x05')
    lcd.cursor_pos = (3, 4)
    lcd.write_string('\x06')
    lcd.cursor_pos = (3, 5)
    lcd.write_string('\x07')
#     sleep(2)
    lcd.cursor_pos = (3, 19)
    lcd.write_string(L_Ch)
    sleep(2)
