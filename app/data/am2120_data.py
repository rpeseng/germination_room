import Adafruit_DHT

class AM2120Sensor:
    def __init__(self, sensor_pin1=20, sensor_pin2=21):
        self.sensor_pin1 = sensor_pin1    # Raspberry Pi üzerinde BCM numarasına göre pin ayarlayın
        self.sensor_pin2 = sensor_pin2
        self.sensor_type = Adafruit_DHT.DHT22  # DHT11 sensörü tipini belirtin


    def read_am2120_values(self):
        try:
            # Sensörden sıcaklık ve nem değerlerini oku
            humidity_1, temperature_1 = Adafruit_DHT.read_retry(self.sensor_type, self.sensor_pin1)
            humidity_2, temperature_2 = Adafruit_DHT.read_retry(self.sensor_type, self.sensor_pin2)

            avg_humidity = (round(humidity_1, 3) + round(humidity_2, 3)) / 2
            avg_temperature = (round(temperature_1, 3) + round(temperature_2, 3)) / 2
            """if temperature_1 and humidity_1 is None:
                print("temperature and humidity 1 is None.")
                pass
            elif temperature_2 and humidity_2 is None:
                print("temperature and humidity 2 is None.")
                pass"""
            if avg_humidity is not None and avg_temperature is not None:
                #print(f"Sıcaklık: {temperature:.1f}°C, Nem: {humidity:.1f}%")
                return avg_temperature, avg_humidity
            else:
                print("Sensörden veri okunamadı. Hata olabilir.")
                return None, None
        except Exception as error:
            print(f"Hata oluştu! read_am2120_value: {error}")

