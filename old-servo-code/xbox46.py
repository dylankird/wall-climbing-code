import RPi.GPIO as GPIO
import pygame
import time
import bluetooth

# Suppress GPIO warnings
GPIO.setwarnings(False)

# Set up GPIO for servo control
servo_pin1 = 14
servo_pin2 = 2
servo_pin3 = 3

servo_pin4 = 20  # Change to the desired GPIO pin for servo 4
servo_pin5 = 21  # Change to the desired GPIO pin for servo 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin1, GPIO.OUT)
GPIO.setup(servo_pin2, GPIO.OUT)
GPIO.setup(servo_pin3, GPIO.OUT)
GPIO.setup(servo_pin4, GPIO.OUT)
GPIO.setup(servo_pin5, GPIO.OUT)

pwm1 = GPIO.PWM(servo_pin1, 50)
pwm2 = GPIO.PWM(servo_pin2, 50)
pwm3 = GPIO.PWM(servo_pin3, 50)
pwm4 = GPIO.PWM(servo_pin4, 50)
pwm5 = GPIO.PWM(servo_pin5, 50)

pwm1.start(0)
pwm2.start(0)
pwm3.start(0)
pwm4.start(0)
pwm5.start(0)

min_angle4 = 0
max_angle4 = 180
min_duty_cycle4 = 2.5
max_duty_cycle4 = 12.5

min_angle5 = 0
max_angle5 = 180
min_duty_cycle5 = 2.5
max_duty_cycle5 = 12.5

# Initialize the Pygame module
pygame.init()

# Bluetooth address of your controller, replace with the actual address
controller_address = "98:B6:ED:F6:0A:66"

# Initialize a Bluetooth socket
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((controller_address, 1))

try:
    while True:
        data = sock.recv(1024)  # Receive data from the Bluetooth controller
        if not data:
            break

        # Parse and process the received data here based on your Bluetooth controller input.
        # You will need to adapt this part according to the specific Bluetooth controller you are using.

        # Example: If you receive "L1" or "R1" from the controller, adjust servo positions accordingly.
        if data == b'L1':
            # Rotate servo 4 to the left (counterclockwise)
            angle4 = max(min_angle4, min_angle4 + 30)
            angle5 = max(max_angle5, max_angle5 - 30)
        elif data == b'R1':
            # Rotate servo 4 to the right (clockwise)
            angle4 = min(max_angle4, max_angle4 - 30)
            angle5 = min(min_angle5, min_angle5 + 30)

        # Calculate duty cycles based on angles and limits
        duty_cycle4 = (angle4 - min_angle4) / (max_angle4 - min_angle4) * (max_duty_cycle4 - min_duty_cycle4) + min_duty_cycle4
        duty_cycle5 = (angle5 - min_angle5) / (max_angle5 - min_angle5) * (max_duty_cycle5 - min_duty_cycle5) + min_duty_cycle5

        # Update the servos
        pwm4.ChangeDutyCycle(duty_cycle4)
        pwm5.ChangeDutyCycle(duty_cycle5)

except KeyboardInterrupt:
    pass

sock.close()

# Clean up GPIO
pwm1.stop()
pwm2.stop()
pwm3.stop()
pwm4.stop()
pwm5.stop()
GPIO.cleanup()
