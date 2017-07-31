from datetime import date
from sound import Sound
import serial


ser = serial.Serial('/dev/tty.usbserial', 9600)

data = ser.readline()

num = int(data)




