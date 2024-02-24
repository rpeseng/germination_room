from RPLCD import *
from RPLCD.i2c import CharLCD

from time import sleep
from am2120_data import AM2120Sensor

framebuffer = [
        '',
        '',
        ]

class LCDController:
    def __init__(self, address=0x27):
        # LCD ekranının I2C adresi
        self.lcd = CharLCD('PCF8574', 0x27)
        self.am2120sensor = AM2120Sensor()

        # Ekran temizleme
        self.clear_screen()


    def clear_screen(self):
        """
                    Function is for clear screen.
        """
        self.lcd.clear()

    def cursor_pos(self):
        self.lcd.cursor_pos()

    def write(self, message):
        self.lcd.write(message)

    def print_on_lcd(self, message, line, alignment='right'):
        """
                    Function is for print on lcd.
        """
        if line == 0:
            self.lcd.cursor_post = (line, 0)
            self.lcd.write(message)
        if line == 1:
            self.lcd.cursor_post = (line, 0)
            self.lcd.write(message)
        if line == 2:
            self.lcd.cursor_post = (line, 0)
            self.lcd.write(message)
        if line == 3:
            self.lcd.cursor_post = (line, 0)
            self.lcd.write(message)


    def write_to_lcd(self,lcd, framebuffer, num_cols):
        """Write the framebuffer out to the specified LCD."""
        lcd.home()
        for row in framebuffer:
            self.lcd.write_string(row.ljust(num_cols)[:num_cols])
            self.lcd.write_string('\r\n')
    def long_text(self,text):
        if len(text) < 20:
            self.lcd.write_string(text)
        for i in range(len(text) - 20 + 1):
            framebuffer[1] = text[i:i + 20]
            self.write_to_lcd(self.lcd, framebuffer, 20)
            sleep(0.2)

    def update_values(self, temp_value, hum_value, time):

        try:
            self.print_on_lcd(f"=== ORTAM DEGERI ===", 0, )
            self.print_on_lcd(f"Temperature =   {temp_value:.2f}", 1, )
            self.print_on_lcd(f"Humudity    =   {hum_value:.2f}", 2, )
            self.print_on_lcd(f"Time:    =   {time:.2f}", 3, )

        except KeyboardInterrupt:
            pass
        except Exception as error:
            print(f"lcd_connection update_values: {error}")
            self.lcd_screen_deactivate()
        finally:
            self.clear_screen()


    def lcd_screen_deactivate(self):
        try:
            self.lcd.cursor_pos = (1, 5)
            self.write("Lcd Screen")
            self.lcd.cursor_pos = (2, 5)
            self.write("Deactivate")
        except KeyboardInterrupt:
            pass
        except Exception as error:
            print(f"lcd_connection lcd_screen_deactivates: {error}")
            print(f"lcd_screen_deactivate : {error}")

"""if __name__ == "__main__":
    lcd = LCDController()
    try:
        while True:
            lcd.update_values()
    except Exception as er:
        print(er)"""
