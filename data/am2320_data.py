import board
import busio
import adafruit_am2320
import time

class AM2120Sensor:
    def __init__(self, i2c_bus=1):
        # I2C bağlantısını başlat
        self.i2c = busio.I2C(board.SCL, board.SDA)

        # AM2120 sensörünü başlat
        self.sensor = adafruit_am2320.AM2320(self.i2c)

    def read_temperature(self):
        # Sıcaklık değerini oku ve döndür
        return self.sensor.temperature

    def read_humidity(self):
        # Nem değerini oku ve döndür
        return self.sensor.relative_humidity

if __name__ == "__main__":
    # AM2120Sensor sınıfından bir nesne oluştur
    sensor = AM2120Sensor()

    try:
        while True:
            # Sıcaklık ve nem değerlerini oku
            temperature = sensor.read_temperature()
            humidity = sensor.read_humidity()

            # Okunan değerleri ekrana yazdır
            print(f"Sıcaklık: {temperature} °C")
            print(f"Nem: {humidity}%")

            # 2 saniye beklet
            time.sleep(2)

    except KeyboardInterrupt:
        print("Program kapatıldı.")




"""import time
import board
import adafruit_am2320

i2c = board.I2C()  # Raspberry Pi üzerindeki I2C bağlantı noktasını alın
sensor = adafruit_am2320.AM2320(i2c)


while True:
    try:
        temperature = sensor.temperature
        humidity = sensor.relative_humidity

        print("Sıcaklık: {:.2f} °C".format(temperature))
        print("Nem: {:.2f}%".format(humidity))

        time.sleep(2)  # 2 saniye bekleme süresi
    except Exception as e:
        print("Hata oluştu:", e)"""
