import RPi.GPIO as GPIO
import time

#Disable GPIO warnings
GPIO.setwarnings(False)

#Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

#Define the GPIO pin connected to the servo signal line
servo_pin = 14

try:
    # Set up the GPIO pin as an output
    GPIO.setup(servo_pin, GPIO.OUT)

    # Create a PWM object with a frequency of 50 Hz
    pwm = GPIO.PWM(servo_pin, 50)

    # Function to set the servo angle
    def set_servo_angle(angle):
        duty_cycle = (angle / 14) + 2
        pwm.ChangeDutyCycle(duty_cycle)
        time.sleep(0.5)  # Give the servo some time to move

    # Start the PWM
    pwm.start(0)

    # Move the servo to 90 degrees
    set_servo_angle(90)
    time.sleep(2)

except KeyboardInterrupt:
    # Clean up GPIO on Ctrl+C exit
    pwm.stop()
finally:
    GPIO.cleanup()  # Always make sure to clean up GPIO resources