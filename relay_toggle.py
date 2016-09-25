#!/usr/bin/env python

import time 
import RPi.GPIO as io 
io.setmode(io.BCM) 

from Adafruit_IO import Client
aio = Client('')

#use software pin numbering
relay1_pin = 23
relay2_pin = 24

#configure the pins to be used as outputs
io.setup(relay1_pin, io.OUT) 
io.setup(relay2_pin, io.OUT)

#set inital pin states to off
io.output(relay1_pin, False)
io.output(relay1_pin, False)

relay1_status = 'OFF'
relay2_status = 'OFF'

while True:
    data1 = aio.receive('relay-1')
    data2 = aio.receive('relay-2')

    if data1.value != relay1_status:
        relay1_status = data1.value

        if relay1_status == 'OFF':
            print("Switching Relay 1 Off")
            #io.output(relay1_pin, False)

        if relay1_status == 'ON':
            print("Switching Relay 1 On")
            #io.output(relay1_pin, True)

    if data2.value != relay2_status:
        relay2_status = data2.value
        
        if relay2_status == 'OFF':
            print("Switching Relay 2 Off")
            #io.output(relay2_pin, False)

        if relay2_status == 'ON':
            print("Switching Relay 2 On")
            #io.output(relay2_pin, True)

    time.sleep(20);
