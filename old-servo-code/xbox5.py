import RPi.GPIO as GPIO
import time
import pygame

# Suppress warnings about channel usage
GPIO.setwarnings(False)

# Setup
servo_pin = 14  # The GPIO pin connected to the servo

# Initialize pygame
pygame.init()
pygame.joystick.init()

try:
    # Set up GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servo_pin, GPIO.OUT)

    # PWM setup
    pwm = GPIO.PWM(servo_pin, 50)  # 50 Hz (standard for most servos)
    pwm.start(0)

    def set_servo_angle(angle):
        # Convert angle to duty cycle (duty cycle range: 2% to 12% for most servos)
        duty_cycle = (angle / 14) + 2
        pwm.ChangeDutyCycle(duty_cycle)
        time.sleep(0.5)  # Give the servo some time to move

    while True:
        # Handle events and get joystick input
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                # The left joystick on an Xbox controller ranges from -1.0 to 1.0
                # Map this to servo angles from 0 to 180 degrees
                angle = int((event.value + 1) * 90)
                set_servo_angle(angle)

except KeyboardInterrupt:
    # Clean up GPIO on Ctrl+C exit
    pwm.stop()
    GPIO.cleanup()
    pygame.quit()