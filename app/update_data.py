import threading
from threading import Thread, Event
import time
from time import sleep

from data.am2120_data import AM2120Sensor
from data.sql_connection import SqlSettings


class UpdateData():
    def __init__(self):
        self.sensorvalue = AM2120Sensor()

        # Her iş parçacığı için ayrı bir SqlSettings nesnesi oluşturun
        self.sqlcon = SqlSettings()

        self.stop_event = Event()  # Durdurma olayı
        self.stop_event.clear()

    def insert_sensor_value_database(self):
        try:
            while not self.stop_event.is_set():
                temp_value, hum_value = self.sensorvalue.read_am2120_values()
                print(temp_value)
                print(hum_value)
                # Her iş parçacığı için ayrı bir bağlantı oluşturun
                sqlcon = SqlSettings()
                sqlcon.insert_values(temp_value, hum_value)
                sqlcon.close_connection()
                sleep(5)
        except KeyboardInterrupt:
            print("Veriler durduruldu.")

    def stop_thread(self):
        # Durdurma olayını tetikle.
        self.stop_event.set()

    def close_sql_connection(self):
        self.sqlcon.close_connection()


def main():
    add_data = UpdateData()
    update_thread = None

    try:
        update_thread = Thread(target=add_data.insert_sensor_value_database)
        update_thread.start()

        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Veriler durduruldu.")
        add_data.close_sql_connection()
        add_data.stop_thread()
        if update_thread is not None:
            update_thread.join()

    finally:
        add_data.close_sql_connection()


if __name__ == "__main__":
    main()
