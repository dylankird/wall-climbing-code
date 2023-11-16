# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""Simple test for a standard servo on channel 0 and a continuous rotation servo on channel 1."""
import time
from adafruit_servokit import ServoKit

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)

#Center the camera
kit.servo[4].angle = 70     
kit.servo[5].angle = 150
time.sleep(1)

#Pan Left
kit.servo[4].angle = 70 + 40     
time.sleep(1)

#Pan Right
kit.servo[4].angle = 70 - 40     
time.sleep(1)

#Pan Center
kit.servo[4].angle = 70
time.sleep(1)

#Tilt Down
kit.servo[5].angle = 150 + 30     
time.sleep(1)

#Tilt Up
kit.servo[5].angle = 150 - 30     
time.sleep(1)

#Tilt Center
kit.servo[5].angle = 150     
time.sleep(1)
