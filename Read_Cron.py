# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
import time
from datetime import datetime
import board
from adafruit_seesaw.seesaw import Seesaw
from Send_Data import supa_send
import adafruit_bitbangio as bitbangio
import digitalio

# uses board.SCL and board.SDA
i2c_bus = board.I2C()

# Define pins for the second I2C bus
i2c2_sda = board.D27 #13 #board.D33 #13
i2c2_scl = board.D22 # 15 # board.D10 # 15

# Create the second I2C bus
i2c2 = bitbangio.I2C(i2c2_scl, i2c2_sda)

# Initialize the first moisture sensor
ss = Seesaw(i2c_bus, addr=0x36)

# Initialize the second moisture sensor
ss2 = Seesaw(i2c2, addr=0x36)

# Table list (for now just the one)
table =  "time_temp_humidity_1"

# data list create
datalist = []

# read moisture level through capacitive touch pad
touch = ss.moisture_read()

# Read moisture from second sensor
touch2 = ss2.moisture_read()

# read temperature from the temperature sensor
temp = ss.get_temp()
temp2 = ss2.get_temp()

# Convert to degrees fahrenheit
temp_F = temp*(9/5) + 32
temp2_F = temp2*(9/5) + 32

# Time
now = datetime.now()
t = now.strftime("%I:%M:%S %p, %m/%d/%Y")

# package data as a JSON
data = {'time': t, 'moist': touch, 'temp': temp_F, 'temp2': temp2_F, 'moist2': touch2}

# append the data to the list
datalist.append(data)
print(datalist)

# Send data to the Supabase database
supa_send(data, table)
