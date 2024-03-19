from gpiozero import LED
from time import sleep
from datetime import datetime

import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from data.sql_connection import SqlSettings


class RelayFunction():

    def __init__(self):
        self.sqlvalues = SqlSettings()

        self.set_min_temp_control = LED(5)
        self.set_max_temp_control = LED(6)
        self.set_min_hum_control = LED(13)
        self.set_max_hum_control = LED(19)
        self.set_led_control = LED(26)


    def relay_control(self):
        try:
            set_values = self.sqlvalues.read_set_values_for_relay()

            min_temp_values = set_values[1]
            max_temp_values = set_values[2]
            min_hum_values = set_values[3]
            max_hum_values = set_values[4]

            instant_value = self.sqlvalues.read_values_relay()
            instant_temp_value = instant_value[1]
            instant_hum_value = instant_value[2]

            if instant_temp_value < min_temp_values:
                self.set_min_temp_control.on()
                sleep(3)
                self.set_min_temp_control.off()
            elif instant_temp_value > max_temp_values:
                self.set_max_temp_control.on()
                sleep(3)
                self.set_max_temp_control.off()
            elif instant_hum_value < min_hum_values:
                self.set_min_hum_control.on()
                sleep(3)
                self.set_min_hum_control.off()
            elif instant_hum_value > max_hum_values:
                self.set_max_hum_control.on()
                sleep(3)
                self.set_max_hum_control.off()
        except KeyboardInterrupt:
            print("Finish.")
        except Exception as er:
            print(f"control Relay Error: {er}")


    def led_control(self):
        time_values =  self.sqlvalues.read_set_update_times_for_relay()
        morning_time = time_values[1]
        night_time = time_values[2]
        now = datetime.now()
        current_hour = now.hour
        current_minute = now.minute

        if 8 <= current_hour < 20:
            self.set_led_control.on()
        else:
            self.set_led_control.off()

        print(f"Anlık Zaman: {current_hour:02d}:{current_minute:02d}")
        sleep(60)  # Her dakika kontrol et

def main():
    relay_control = RelayFunction()
    try:
        while True:
            relay_control.relay_control()
            sleep(2)
    except Exception as er:
        print(f"Relay Function Error:  {er}")


if __name__ == "__main__":
    main()