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
    pwm.start(7.5)  # Initialize at the middle position

    while True:
        # Rotate the servo in one direction (clockwise)
        pwm.ChangeDutyCycle(10)  # Increase to speed up clockwise rotation
        time.sleep(2)

 #Rotate the servo in the other direction (counterclockwise)
        pwm.ChangeDutyCycle(5)  # Decrease to speed up counterclockwise rotation
        time.sleep(2)

except KeyboardInterrupt:
    # Clean up GPIO on Ctrl+C exit
    pwm.stop()
    GPIO.cleanup()