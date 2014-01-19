import serial
ser = serial.Serial('/dev/ttyUSB0', 115200)

while 1:
    line = ser.readline()
    print line,
