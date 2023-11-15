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
        pygame.event.pump()  # Pump the Pygame event queue to get the latest joystick events
        axis_value = controller.get_axis(0)  # Get the X-axis value (-1 to 1)

        # Map axis value to servo angle
        current_angle = int((axis_value + 1) * 45)  # Scale to servo angle (0 to 180 degrees)

        # Set the servo angle
        set_servo_angle(current_angle)

except KeyboardInterrupt:
    # Clean up GPIO on Ctrl+C exit
    pwm.stop()
    GPIO.cleanup()