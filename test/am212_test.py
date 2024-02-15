from data.am2120_data import AM2120Sensor

try:
    sensor_values = AM2120Sensor()
    while True:
        temp_hum = sensor_values.read_am2120_values()
        print(f"Temp: {temp_hum[0]}  --- Huö: {temp_hum[1]}")

except KeyboardInterrupt:
    print("Program closed.")