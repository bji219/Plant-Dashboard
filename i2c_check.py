import busio
import adafruit_bitbangio as bitbangio
import digitalio
import time
from datetime import datetime
import board
from adafruit_seesaw.seesaw import Seesaw
from Send_Data import supa_send

# Define pins for the second I2C bus
i2c2_sda = board.D27 #13 #board.D33 #13
i2c2_scl = board.D22 # 15 # board.D10 # 15

# Create the second I2C bus
i2c2 = bitbangio.I2C(i2c2_scl, i2c2_sda)
# i2c2 = bitbangio.I2C(board.i2c_gpio)

# Initialize the moisture sensor
ss = Seesaw(i2c2, addr=0x36)

# Table list (for now just the one)
table =  "time_temp_humidity_1"

while True:
    # data list create
    datalist = []

    # read moisture level through capacitive touch pad
    touch = ss.moisture_read()

    # read temperature from the temperature sensor
    temp = ss.get_temp()

    # Convert to degrees fahrenheit
    temp_F = temp*(9/5) + 32

    # Time
    now = datetime.now()
    t = now.strftime("%I:%M:%S %p, %m/%d/%Y")

    # package data as a JSON
    data = {'time': t, 'moist': touch, 'temp': temp_F}

    # append the data to the list
    datalist.append(data)
    print(datalist)

#   print("temp: " + str(temp_F) + "  moisture: " + str(touch))
    time.sleep(3) # read data every 5 minutes

'''
while not i2c2.try_lock():
    pass

try:
    while True:
        print(
            "I2C addresses found:",
            [hex(device_address) for device_address in i2c2.scan()],
        )
        time.sleep(2)

finally:  # unlock the i2c bus when ctrl-c'ing out of the loop
    i2c2.unlock()
'''
