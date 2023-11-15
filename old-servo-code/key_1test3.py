from gpiozero import AngularServo
import threading
import keyboard

servo = AngularServo(14, min_angle=0, max_angle=270, min_pulse_width=0.0005, max_pulse_width=0.0025)
current_angle = 135  # Initial angle
rotation_step = 5  # Angle increment for rotation

#Function to continuously rotate the servo in one direction
def rotate_clockwise():
    global current_angle
    while keyboard.is_pressed('up'):
        current_angle += rotation_step
        if current_angle > 270:
            current_angle = 270
        servo.angle = current_angle

#Function to continuously rotate the servo in the other direction
def rotate_counterclockwise():
    global current_angle
    while keyboard.is_pressed('down'):
        current_angle -= rotation_step
        if current_angle < 0:
            current_angle = 0
        servo.angle = current_angle

try:
    while True:
        if keyboard.is_pressed('up'):
            # Start rotating clockwise
            clockwise_thread = threading.Thread(target=rotate_clockwise)
            clockwise_thread.start()
        elif keyboard.is_pressed('down'):
            # Start rotating counterclockwise
            counterclockwise_thread = threading.Thread(target=rotate_counterclockwise)
            counterclockwise_thread.start()
        else:
            # Stop rotation if no key is pressed
            servo.angle = current_angle

except KeyboardInterrupt:
    servo.angle = 135  # Set the servo back to the center position