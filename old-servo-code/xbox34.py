import RPi.GPIO as GPIO
import pygame
import time

# Suppress GPIO warnings
GPIO.setwarnings(False)

# Set up GPIO for the joystick-controlled servo
servo_pin_joystick = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin_joystick, GPIO.OUT)

# Set up GPIO for the button-controlled servo
servo_pin_buttons = 15
GPIO.setup(servo_pin_buttons, GPIO.OUT)

# Initialize both servo motors
pwm_joystick = GPIO.PWM(servo_pin_joystick, 50)  # 50Hz PWM frequency
pwm_buttons = GPIO.PWM(servo_pin_buttons, 50)
pwm_joystick.start(0)  # Start with 0% duty cycle (servo is not moving)
pwm_buttons.start(0)

# Initialize the pygame module
pygame.init()

# Initialize the Xbox controller
pygame.joystick.init()
controller = pygame.joystick.Joystick(0)
controller.init()

try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:  # A button (button index may vary)
                    # Rotate servo to the left (counterclockwise)
                    pwm_buttons.ChangeDutyCycle(5)  # Adjust this value as needed
                elif event.button == 3:  # Y button (button index may vary)
                    # Rotate servo to the right (clockwise)
                    pwm_buttons.ChangeDutyCycle(10)  # Adjust this value as needed
            elif event.type == pygame.JOYAXISMOTION:
                if event.axis == 0:
                    # Control servo with the 6th axis (left/right)
                    duty_cycle_joystick = 7.5 + event.value * 2.5  # Adjust this value as needed
                    pwm_joystick.ChangeDutyCycle(duty_cycle_joystick)

            elif event.type == pygame.JOYBUTTONUP:
                # Stop the servo when the button is released
                pwm_buttons.ChangeDutyCycle(0)
        time.sleep(0.01)

except KeyboardInterrupt:
    pass

# Clean up GPIO
pwm_joystick.stop()
pwm_buttons.stop()
GPIO.cleanup()