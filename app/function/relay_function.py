
from gpiozero import LED
from time import sleep
import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from app.data.sql_connection import SqlSettings


class RelayFunction():

    def __init__(self):
        self.sqlvalues = SqlSettings()

        self.set_min_temp_control = LED(5)
        self.set_max_temp_control = LED(6)
        self.set_min_hum_control = LED(13)
        self.set_max_hum_control = LED(19)
        self.set_led_control = LED(26)


    def control_relay(self):
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
                print("111111")
            elif instant_temp_value > max_temp_values:
                self.set_max_temp_control.on()
                sleep(3)
                self.set_max_temp_control.off()
                print("22222")
            elif instant_hum_value < min_hum_values:
                self.set_min_hum_control.on()
                sleep(3)
                self.set_min_hum_control.off()
                print("3333")
            elif instant_hum_value > max_hum_values:
                self.set_max_hum_control.on()
                sleep(3)
                self.set_max_hum_control.off()
                print("44444")
        except KeyboardInterrupt:
            print("Finish.")
        except Exception as er:
            print(f"control Relay Error: {er}")


def main():
    relay_control = RelayFunction()
    try:
        while True:
            relay_control.control_relay()
            sleep(2)
    except Exception as er:
        print(f"Relay Function Error:  {er}")


if __name__ == "__main__":
    main()