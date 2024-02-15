#!/usr/bin/python

import Adafruit_CharLCD as LCD
import time
"""import commands"""
from subprocess import PIPE, Popen
from time import sleep, strftime, localtime
from datetime import datetime, timedelta

class Utils:

    info = None
    mode = 1
    offset = 0
    maxOffset = 0
    screen = []

    #Display Local Info - Accepted, Rejected, HW Errors \n Average Hashrate
    def dispLocalInfo(self):
        self.dispScreen(self.info.screen1)

    def dispScreen(self, newScreen):
        self.screen = newScreen
        try:
            maxOffset = max((len(self.screen[0]) - 16), (len(self.screen[1]) - 16))
            #lcd.clear()
            speed = self.screen[1]
            speed = speed.replace(' Gh/s','')
            speed = speed[0:-1] + ' Gh/s'
            s = self.screen[0] + '\n' + speed
            lcd.message(s)
        except TypeError:
            lcd.clear()
            lcd.message('connecting\nto cgminer ...')


"""    def ShowWLAN(self):
        wlan = '/bin/echo $(/sbin/ifconfig wlan0 | /bin/grep "inet addr" | /usr/bin/cut -d ":" -f 2 | /usr/bin/cut -d " " -f 1)'
        lcd.clear()
        lcd.message("WLAN IP:")
        lcd.message("\n")
        lcd.message(CmdLine(wlan))"""

"""    def ShowTemperature(self):
        temperature = "/bin/echo $(/opt/vc/bin/vcgencmd measure_temp | /usr/bin/cut -c \"6-9\")"
        lcd.clear()
        lcd.message("Temperature (C):")
        lcd.message("\n")
        lcd.message(CmdLine(temperature))"""

"""    def GetSpace(self):
        space = "/bin/echo $(/bin/df -h / | /bin/sed -n '2p' | /usr/bin/awk '{print $4}')/$(/bin/df -h / | /bin/sed -n '2p' | /usr/bin/awk '{print $3}')"
        percentage = "/bin/echo $(/bin/df -h / | /bin/sed -n '2p' | /usr/bin/awk '{print $5}')"
        lcd.clear()
        lcd.message("Space: " + CmdLine(space))
        lcd.message("\n")
        lcd.message("Percent.: " + CmdLine(percentage))"""
"""
    def ShowDateTime(self):
        lcd.clear()
        while not(lcd.is_pressed(LCD.LEFT) or lcd.is_pressed(LCD.UP) or lcd.is_pressed(LCD.DOWN) or lcd.is_pressed(LCD.RIGHT)):
            time.sleep(0.25)
            lcd.message(strftime('%a %b %d %Y\n%I:%M:%S %p"""     ', localtime()))

"""    def ShowIPAddress(self):
        lcd.clear()
        lcd.message("Local IP: \n" + commands.getoutput("/sbin/ifconfig").split("\n")[1].split()[1][5:])

    def DoShutdown(self):
        lcd.clear()
        lcd.message('Are you sure?\nPress Sel for Y')
        while True:
            if lcd.is_pressed(LCD.LEFT) or lcd.is_pressed(LCD.UP) or lcd.is_pressed(LCD.DOWN) or lcd.is_pressed(LCD.RIGHT):
                break
            if lcd.is_pressed(LCD.SELECT):
                lcd.clear()
                commands.getoutput("sudo shutdown -h now")
                quit()
            time.sleep(0.25)"""

    def DoReboot(self):
        lcd.clear()
        lcd.message('Are you sure?\nPress Sel for Y')
        while 1:
            if lcd.is_pressed(LCD.LEFT):
                break
            if lcd.is_pressed(LCD.SELECT):
                lcd.clear()
                commands.getoutput("sudo reboot")
                quit()
            time.sleep(0.25)


"""def CmdLine(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]"""

def callMethod(o, name):
    getattr(o, name)()

def showMenu(index):
    lcd.clear()
    lcd.message("> Main Menu <")
    lcd.message("\n")
    lcd.message(menu_list[index][0])

utils = Utils()

# Initialize the LCD using the pins
lcd = LCD.Adafruit_CharLCDPlate()

lcd.clear()
lcd.set_color(0.0, 0.0, 0.0)

menu_list = [("Date/Time", "ShowDateTime"),
             ("Disk space", "GetSpace"),
             ("Temperature", "ShowTemperature"),
             ("Show WLAN", "ShowWLAN"),
             ("Bitcoin", "ShowBitcoin"),
             ("Show IP", "ShowIPAddress"),
             ("Shutdown", "DoShutdown"),
             ("Reboot", "DoReboot")]

index = 0
#showMenu(0)
utils.ShowDateTime()

while True:

    if (lcd.is_pressed(LCD.UP) and index > 0):
        index = index - 1
        showMenu(index)
        time.sleep(0.25)

    if (lcd.is_pressed(LCD.DOWN) and (index <= len(menu_list) - 2)):
        index = index + 1
        showMenu(index)
        time.sleep(0.25)

    if (lcd.is_pressed(LCD.RIGHT)):
        showMenu(index)
        time.sleep(0.25)

    if (lcd.is_pressed(LCD.LEFT)):
        showMenu(index)
        time.sleep(0.25)

    if (lcd.is_pressed(LCD.SELECT)):
        lcd.clear()
        callMethod(utils, menu_list[index][1])
        time.sleep(0.25)