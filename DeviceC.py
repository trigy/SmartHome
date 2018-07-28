from Adafruit_BME280 import *
import curses
import RPi.GPIO as GPIO
import time

FanPin = 11
GPIO.setup(FanPin, GPIO.OUT)


def FanControl():
    for i in range (0,5):
        GPIO.output(FanPin, True)
        GPIO.output(FanPin, False)
        time.sleep(4)

def DataInHouse():
    sensor = BME280(p_mode=BME280_OSAMPLE_8, t_mode=BME280_OSAMPLE_2, h_mode=BME280_OSAMPLE_1, filter=BME280_FILTER_16)
    tstart = time.time()

    for i in range(0,10):
        degrees = sensor.read_temperature()
        pascals = sensor.read_pressure()
        hectopascals = pascals / 100  
        humidity = sensor.read_humidity()
#        stdscr.addstr(0, 0, 'Timestamp = %0.3f sec' % (time.time() - tstart))
#        stdscr.addstr(1, 0, 'Temp      = %0.3f deg C (%0.3f deg F)' % (degrees, ((degrees*9/5)+32)))
#        stdscr.addstr(2, 0, 'Pressure  = %0.2f hPa' % hectopascals)
#        stdscr.addstr(3, 0, 'Humidity  = %0.2f %%' % humidity)
#        stdscr.addstr(5, 0, 'Press any key to exit...')
        print('Timestamp = %0.3f sec' % (time.time() - tstart))
        print('Temp      = %0.3f deg C (%0.3f deg F)' % (degrees, ((degrees*9/5)+32)))
        print('Pressure  = %0.2f hPa' % hectopascals)
        print('__________________________')
#        stdscr.refresh()

        time.sleep(3)

#        stdscr.erase()
