import RPi.GPIO as GPIO
import time
import pygame

# Suppress warnings about channel usage
GPIO.setwarnings(False)

# Setup
servo_pin = 14  # The GPIO pin connected to the servo

# Xbox controller setup
pygame.init()
controller = pygame.joystick.Joystick(0)
controller.init()

# Initialize the servo position
current_angle = 90  # Start in the center (90 degrees)

# Flags to track button states
button_right_pressed = False
button_left_pressed = False

try:
    # Set up GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servo_pin, GPIO.OUT)

    # PWM setup
    pwm = GPIO.PWM(servo_pin, 50)  # 50 Hz (standard for most servos)
    pwm.start(0)

    def set_servo_angle(angle):
        duty_cycle = (angle / 14) + 2
        pwm.ChangeDutyCycle(duty_cycle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 1:  # Button B (right button)
                    button_right_pressed = True
                elif event.button == 0:  # Button A (left button)
                    button_left_pressed = True
            elif event.type == pygame.JOYBUTTONUP:
                if event.button == 1:
                    button_right_pressed = False
                elif event.button == 0:
                    button_left_pressed = False

        if button_right_pressed:
            # Move to the right
            current_angle = min(180, current_angle + 10)
            set_servo_angle(current_angle)
        elif button_left_pressed:
            # Move to the left
            current_angle = max(0, current_angle - 10)
            set_servo_angle(current_angle)
        else:
            # Stop the servo when no buttons are pressed
            set_servo_angle(current_angle)

except KeyboardInterrupt:
    # Clean up GPIO on Ctrl+C exit
    pwm.stop()
    GPIO.cleanup()