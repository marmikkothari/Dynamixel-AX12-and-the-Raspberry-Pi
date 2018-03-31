Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import serial
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

port = serial.Serial("/dev/ttyAMA0", baudrate=1000000, timeout=3.0)

while True:
        GPIO.output(18, GPIO.HIGH)
        port.write(bytearray.fromhex("FF FF 01 05 03 1E 32 03 A3"))
        time.sleep(0.1)
        GPIO.output(18, GPIO.LOW)
        time.sleep(3)

        GPIO.output(18,GPIO.HIGH)
        port.write(bytearray.fromhex("FF FF 01 05 03 1E CD 00 0b"))
        time.sleep(0.1)
        GPIO.output(18,GPIO.LOW)
        time.sleep(3)

