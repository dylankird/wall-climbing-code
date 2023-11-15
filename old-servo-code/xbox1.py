import time
import math
import evdev
from adafruit_servokit import ServoKit

#Initialize the PCA9685 and ServoKit
kit = ServoKit(channels=16)

#Define the servo parameters
min_pulse = 500
max_pulse = 2500
servo_range = max_pulse - min_pulse

#Define servo angles and initial values
servo_angles = [90, 90, 90, 90]
current_angles = servo_angles.copy()

#Define function to map controller input to servo angles
def map_range(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

#Initialize the Xbox controller
devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
controller = None

for device in devices:
    if "Xbox" in device.name:
        controller = evdev.InputDevice(device.path)

if not controller:
    print("Xbox controller not found. Make sure it's connected.")
    exit()

print("Xbox controller found and connected.")
try:
    for event in controller.read_loop():
        if event.type == evdev.ecodes.EV_ABS:
            if event.code == evdev.ecodes.ABS_X:
                # Left stick horizontal (Thumbstick X-axis)
                current_angles[0] = int(map_range(event.value, 0, 255, 0, servo_range) + min_pulse)
            elif event.code == evdev.ecodes.ABS_Y:
                # Left stick vertical (Thumbstick Y-axis)
                current_angles[1] = int(map_range(event.value, 0, 255, 0, servo_range) + min_pulse)
            elif event.code == evdev.ecodes.ABS_RX:
                # Right stick horizontal (Thumbstick X-axis)
                current_angles[2] = int(map_range(event.value, 0, 255, 0, servo_range) + min_pulse)
            elif event.code == evdev.ecodes.ABS_RY:
                # Right stick vertical (Thumbstick Y-axis)
                current_angles[3] = int(map_range(event.value, 0, 255, 0, servo_range) + min_pulse)

        # Update servo positions
        for i in range(4):
            kit.servo[i].angle = current_angles[i]

except KeyboardInterrupt:
    kit.deinit()
    print("Exiting...")