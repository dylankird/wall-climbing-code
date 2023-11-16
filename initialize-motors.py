# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""Simple test for a standard servo on channel 0 and a continuous rotation servo on channel 1."""
import time
from adafruit_servokit import ServoKit

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)

#Motor 0 is front steering
#Motor 1 is rear steering
#Motor 2 is front drive
#Motor 3 is back drive

kit.servo[0].angle = 80
kit.servo[1].angle = 90

kit.servo[2].angle = 92.5
kit.servo[3].angle = 92.5


