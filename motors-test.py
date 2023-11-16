# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""Simple test for a standard servo on channel 0 and a continuous rotation servo on channel 1."""
import time
from adafruit_servokit import ServoKit

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)

#Turn off drive motors
kit.servo[2].angle = 92.5
kit.servo[3].angle = 92.5

#Steering forward
kit.servo[0].angle = 80
kit.servo[1].angle = 90
time.sleep(1)

#Steering Right
kit.servo[0].angle = 80 + 30
kit.servo[1].angle = 90 - 30
time.sleep(1)

#Steering forward
kit.servo[0].angle = 80
kit.servo[1].angle = 90
time.sleep(1)

#Steering Left
kit.servo[0].angle = 80 - 30
kit.servo[1].angle = 90 + 30
time.sleep(1)

#Steering forward
kit.servo[0].angle = 80
kit.servo[1].angle = 90
time.sleep(1)


#Drive forwards
kit.servo[2].angle = 92.5 + 10
kit.servo[3].angle = 92.5 - 10
time.sleep(0.2)

#Stop
kit.servo[2].angle = 92.5
kit.servo[3].angle = 92.5
time.sleep(0.5)

#Drive backwards
kit.servo[2].angle = 92.5 - 10
kit.servo[3].angle = 92.5 + 10
time.sleep(0.2)

#Stop
kit.servo[2].angle = 92.5
kit.servo[3].angle = 92.5
time.sleep(0.5)




