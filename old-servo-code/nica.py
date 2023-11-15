import RPi.GPIO as GPIO
import time

#Suppress warnings about channel usage
GPIO.setwarnings(False)

#Setup
servo_pin = 14  # The GPIO pin connected to the servo

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
        time.sleep(0.5)  # Give the servo some time to move

    while True:
        # Move the servo from 0 to 180 degrees
        for angle in range(0, 181, 10):
            set_servo_angle(angle)

#Move the servo from 180 to 0 degrees
        for angle in range(180, -1, -10):
            set_servo_angle(angle)

except KeyboardInterrupt:
    # Clean up GPIO on Ctrl+C exit
    pwm.stop()
    GPIO.cleanup()