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

# Flag to track whether the joystick button is pressed
button_pressed = False

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
                if event.button == 0:  # Change the button number if needed
                    button_pressed = True
            elif event.type == pygame.JOYBUTTONUP:
                if event.button == 0:
                    button_pressed = False

            if button_pressed:
                if event.type == pygame.JOYAXISMOTION:
                    if event.axis == 0:  # Left stick horizontal axis
                        # Map axis value to servo angle
                        current_angle += event.value * 10  # Adjust angle by 10 degrees
                        current_angle = max(0, min(180, current_angle))  # Limit angle to 0-180 degrees
                        set_servo_angle(current_angle)
            else:
                # Stop the servo when the button is not pressed
                set_servo_angle(90)

except KeyboardInterrupt:
    # Clean up GPIO on Ctrl+C exit
    pwm.stop()
    GPIO.cleanup()