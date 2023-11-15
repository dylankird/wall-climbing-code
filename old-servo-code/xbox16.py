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

# cInitialize the servo position and joystick pressed flag
current_angle = 90  # Start in the center (90 degrees)
joystick_pressed = False

try:
    # Set up GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servo_pin, GPIO.OUT)

    # PWM setup
    pwm = GPIO.PWM(servo_pin, 50)  # 50 Hz (standard for most servos)
    pwm.start(0)

    def set_servo_angle(angle):
        duty_cycle = (angle / 14) + 2  # Updated duty cycle calculation
        pwm.ChangeDutyCycle(duty_cycle)

    print("Press CTRL+C to exit.")

    while True:
        joystick_pressed = False  # Reset the flag at the beginning of each loop

        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                if event.axis == 0:  # Left stick horizontal axis
                    if abs(event.value) > 0.1:  # Check if the joystick is significantly tilted
                        joystick_pressed = True
                        # Map axis value to servo angle
                        current_angle += event.value * 10  # Adjust angle by 10 degrees
                        current_angle = max(0, min(180, current_angle))  # Limit angle to 0-180 degrees

        # Stop the servo movement when the joystick is not pressed
        if not joystick_pressed:
            set_servo_angle(current_angle)  # Hold the current angle

        # Update the servo angle if the joystick is pressed
        set_servo_angle(current_angle)

except KeyboardInterrupt:
    # Clean up GPIO on Ctrl+C exit
    pwm.stop()
    GPIO.cleanup()