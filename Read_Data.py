# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
import time
from datetime import datetime
import board
from adafruit_seesaw.seesaw import Seesaw
from Send_Data import supa_send

# uses board.SCL and board.SDA
i2c_bus = board.I2C()

# Initialize the moisture sensor
ss = Seesaw(i2c_bus, addr=0x36)

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

    # Send data to the Supabase database
    supa_send(data, table)

#    print("temp: " + str(temp_F) + "  moisture: " + str(touch))
    time.sleep(3) # read data every 5 minutes

