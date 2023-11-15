from gpiozero import AngularServo
from time import sleep
import keyboard

servo = AngularServo(14, min_angle=0, max_angle=270, min_pulse_width=0.0005, max_pulse_width=0.0025)
current_angle = 135  # Initial angle

def increase_angle():
    global current_angle
    current_angle += 10
    if current_angle > 270:
        current_angle = 270
    servo.angle = current_angle

def decrease_angle():
    global current_angle
    current_angle -= 10
    if current_angle < 0:
        current_angle = 0
    servo.angle = current_angle

try:
    while True:
        if keyboard.is_pressed('up'):
            increase_angle()
        elif keyboard.is_pressed('down'):
            decrease_angle()
        sleep(0.1)  # Add a small delay to reduce CPU usage

except KeyboardInterrupt:
    servo.angle = 135  # Set the servo back to the center position