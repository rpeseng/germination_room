import threading
from multiprocessing import Process, Event
import time
from time import sleep

from data.am2120_data import AM2120Sensor
from data.sql_connection import SqlSettings


class UpdateData():
    def __init__(self):
        self.sensorvalue = AM2120Sensor()
        self.sqlcon = SqlSettings()

        self.stop_event = Event()  # Durdurma olayı
        self.stop_event.clear()

    def insert_sensor_value_database(self):

        try:
            while not self.stop_event.is_set():
                temp_value, hum_value = self.sensorvalue.read_am2120_values()
                temp_value = round(temp_value, 2)
                hum_value = round(hum_value, 2)
                # Her iş parçacığı için ayrı bir bağlantı oluşturun
                self.sqlcon.insert_values(temp_value, hum_value)
                sleep(5)
        except KeyboardInterrupt:
            print("Veriler durduruldu.")

    def stop_process(self):
        # Durdurma olayını tetikle.
        self.stop_event.set()

    def close_sql_connection(self):
        self.sqlcon.close_connection()


def main():
    add_data = UpdateData()
    update_process = None

    try:
        update_process = Process(target=add_data.insert_sensor_value_database)
        update_process.start()

        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Veriler durduruldu.")
        add_data.stop_process()
        add_data.close_sql_connection()
        if update_process is not None:
            update_process.terminate()

    finally:
        print("Bağlantılar kapatıldı.")


if __name__ == "__main__":
    main()
