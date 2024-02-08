import smbus
import time

class I2CLcd:
    def __init__(self, addr=0x27):
        self.bus = smbus.SMBus(1)
        self.addr = addr
        self.lcd_init()

    def lcd_init(self):
        # I2C LCD ekranı başlatma
        self.send_command(0x33)  # Initialization
        self.send_command(0x32)  # Initialization
        self.send_command(0x06)  # Cursor move direction
        self.send_command(0x0C)  # Display On, Cursor Off, Blink Off
        self.send_command(0x28)  # Data length, number of lines, font size
        self.send_command(0x01)  # Clear display
        time.sleep(0.0005)  # Delay to wait for LCD to clear

    def lcd_clear(self):
        # I2C LCD ekranını temizleme
        self.send_command(0x01)
        time.sleep(0.0005)  # Delay to wait for LCD to clear

    def lcd_set_cursor(self, row, col):
        # I2C LCD ekranında imleci belirtilen konuma taşıma
        if row == 0:
            address = 0x80 + col
        elif row == 1:
            address = 0xC0 + col
        elif row == 2:
            address = 0x94 + col
        elif row == 3:
            address = 0xD4 + col
        else:
            return
        self.send_command(address)

    def lcd_send_char(self, char):
        # I2C LCD ekranına karakter gönderme
        self.send_data(ord(char))

    def lcd_send_string(self, string):
        # I2C LCD ekranına string gönderme
        for char in string:
            self.lcd_send_char(char)

    def send_command(self, value):
        self.bus.write_byte_data(self.addr, 0x00, value)
        time.sleep(0.0001)

    def send_data(self, value):
        self.bus.write_byte_data(self.addr, 0x40, value)
        time.sleep(0.0001)

    def lcd_set_text(self, line, text):
        # I2C LCD ekranında belirtilen satıra metin yazma
        if line == 1:
            self.bus.write_byte_data(self.addr, 0x80, 0x00)
        elif line == 2:
            self.bus.write_byte_data(self.addr, 0xC0, 0x00)
        elif line == 3:
            self.bus.write_byte_data(self.addr, 0x94, 0x00)
        elif line == 4:
            self.bus.write_byte_data(self.addr, 0xD4, 0x00)
        self.bus.write_i2c_block_data(self.addr, 0x40, [ord(char) for char in text])

# Kullanım örneği
if __name__ == "__main__":

    lcd = I2CLcd()

    lcd.lcd_clear()
    lcd.lcd_set_cursor(0, 0)
    lcd.lcd_send_string("Hello")
    lcd.lcd_set_cursor(1, 0)
    lcd.lcd_send_string("World")

    time.sleep(2)

    lcd.lcd_clear()
    lcd.lcd_set_cursor(0, 0)
    lcd.lcd_send_string("Custom")
    lcd.lcd_set_cursor(1, 0)
    lcd.lcd_send_string("Message")

    time.sleep(2)

    lcd.lcd_clear()
