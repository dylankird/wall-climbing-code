import RPi.GPIO as GPIO
import pygame
import time

# Suppress GPIO warnings
GPIO.setwarnings(False)

# Set up GPIO for servo control
servo_pin1 = 14
servo_pin2 = 2  # Change to the desired GPIO pin
servo_pin3 = 3  # Change to the desired GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin1, GPIO.OUT)
GPIO.setup(servo_pin2, GPIO.OUT)
GPIO.setup(servo_pin3, GPIO.OUT)

# Initialize the servo motors
pwm1 = GPIO.PWM(servo_pin1, 50)  # 50Hz PWM frequency
pwm2 = GPIO.PWM(servo_pin2, 50)  # 50Hz PWM frequency
pwm3 = GPIO.PWM(servo_pin3, 50)  # 50Hz PWM frequency
pwm1.start(0)  # Start with 0% duty cycle (servo 1 is not moving)
pwm2.start(0)  # Start with 0% duty cycle (servo 2 is not moving)
pwm3.start(0)  # Start with 0% duty cycle (servo 3 is not moving)

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
                    # Rotate servo 1 to the left (counterclockwise)
                    pwm1.ChangeDutyCycle(5)  # Adjust this value as needed
                elif event.button == 3:  # Y button (button index may vary)
                    # Rotate servo 1 to the right (clockwise)
                    pwm1.ChangeDutyCycle(10)  # Adjust this value as needed
            elif event.type == pygame.JOYBUTTONUP:
                # Stop servo 1 when the button is released
                pwm1.ChangeDutyCycle(0)

            if event.type == pygame.JOYHATMOTION:
                # Handle D-Pad events
                x, y = event.value
                if x == 1:
                    # Move servo 3 to the right (clockwise)
                    pwm3.ChangeDutyCycle(10)  # Adjust this value as needed
                elif x == -1:
                    # Move servo 3 to the left (counterclockwise)
                    pwm3.ChangeDutyCycle(5)  # Adjust this value as needed
                else:
                    pwm3.ChangeDutyCycle(0)  # Stop servo 3

                if y == 1:
                    # Move servo 2 up
                    pwm2.ChangeDutyCycle(10)  # Adjust this value as needed
                elif y == -1:
                    # Move servo 2 down
                    pwm2.ChangeDutyCycle(5)  # Adjust this value as needed
                else:
                    pwm2.ChangeDutyCycle(0)  # Stop servo 2

        time.sleep(0.01)

except KeyboardInterrupt:
    pass

# Clean up GPIO
pwm1.stop()
pwm2.stop()
GPIO.cleanup()