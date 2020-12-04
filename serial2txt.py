## This script reads lines from arduino serial communication and saves it to 'output.txt'
## Requires package: pyserial

import serial
# from time import sleep                           # uncomment if sleep is required to change sampling

serial = serial.Serial("COM_PORT_NAME", 115200, timeout = 1) # Open serial port at required baude rate
f = open("output.txt","w")                         # open txt file to write
print(serial)                                      # show serial port info on terminal
#time.sleep(5)                                     # wait 5 sec (changes sampling frequency)

# Serial readline loop
while True:
    data = serial.readline()
    data = data.decode("utf-8")  # decode utf-8 unicode characters as str
    print(data)                  # show on terminal
    f.write(data)                # write to txt file 