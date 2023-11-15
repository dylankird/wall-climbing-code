import RPi.GPIO as GPIO
import pygame
import time

# Suppress GPIO warnings
GPIO.setwarnings(False)

# Set up GPIO
servo_pin = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# Initialize the servo motor
pwm = GPIO.PWM(servo_pin, 50)  # 50Hz PWM frequency
pwm.start(0)  # Start with 0% duty cycle (servo is not moving)

# Initialize the pygame module
pygame.init()

# Initialize the Xbox controller
controller = pygame.joystick.Joystick(0)
controller.init()

try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:  # A button (button index may vary)
                    # Rotate servo to the left (counterclockwise)
                    pwm.ChangeDutyCycle(5)  # Adjust this value as needed
                elif event.button == 3:  # Y button (button index may vary)
                    # Rotate servo to the right (clockwise)
                    pwm.ChangeDutyCycle(10)  # Adjust this value as needed
            elif event.type == pygame.JOYBUTTONUP:
                # Stop the servo when the button is released
                pwm.ChangeDutyCycle(0)
        time.sleep(0.01)

except KeyboardInterrupt:
    pass

# Clean up GPIO
pwm.stop()
GPIO.cleanup()