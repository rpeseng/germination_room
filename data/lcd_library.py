
from rpi_lcd import LCD
import time
from data.am2120_data import AM2120Sensor
import logging


class LCDController:
    def __init__(self, address=0x27):
        # LCD ekranının I2C adresi
        self.lcd = LCD()
        self.am2120sensor = AM2120Sensor()

        # Ekran temizleme
        self.clear_screen()
        logging.basicConfig(filename='/logs/lcd_tools_log.txt', level=logging.ERROR,
                            format='%(asctime)s - %(levelname)s - %(message)s')

    def clear_screen(self):
        """
                    Function is for clear screen.
        """
        self.lcd.clear()

    def print_on_lcd(self, message, line, alignment='right'):
        """
                    Function is for print on lcd.
        """
        self.lcd.text(message, line, alignment)

    def find_none_values(self, control_value):
        """
        This function checks if the incoming data is none.
        If it is None, replaces it with 0.
        """
        if control_value is None:
            return 0
        return control_value

    def update_values(self, water_temp, ph, ec, air_temp):

        try:
            pass
            while True:
                avg_temp,avg_hum = self.am2120sensor.read_am2120_values()
                self.print_on_lcd(f"Temperature =   {avg_temp:.2f}", 1, 'right')
                self.print_on_lcd(f"Humudity    =   {avg_hum:.2f}", 2, 'right')


        except KeyboardInterrupt:
            pass
        except Exception as error:
            logging.error(f"lcd_connection update_values: {error}", exc_info=True)
            self.lcd_screen_deactivate()
        finally:
            self.clear_screen()



    def lcd_screen_deactivate(self):
        try:
            self.print_on_lcd("Lcd Screen,", 1, 'left')
            self.print_on_lcd("Deactivate", 2, 'left')
        except KeyboardInterrupt:
            pass
        except Exception as error:
            logging.error(f"lcd_connection lcd_screen_deactivates: {error}")
            print(f"lcd_screen_deactivate : {error}")




            """            
            count = 0
            incoming_value_array = [water_temp, ph, ec, air_temp]
            for i in range(4):
                incoming_value_array[i] = self.find_none_values(incoming_value_array[i])
            # print(incoming_value_array)
            while count < 2:

                # LCD ekranına metinleri ve verileri yazdır
                self.print_on_lcd(f"Water_temp =   {incoming_value_array[0]:.2f}", 1, 'right')
                self.print_on_lcd(f"Ph          =   {incoming_value_array[1]:.2f}", 2, 'right')
                self.print_on_lcd(f"Ec         =   {incoming_value_array[2]:.2f}", 3, 'right')
                self.print_on_lcd(f"Air_temp   =   {incoming_value_array[3]:.2f}", 4, 'right')

                time.sleep(2)  # 3 saniye beklet
                count += 1 """