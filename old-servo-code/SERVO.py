import RPi.GPIO as GPIO
import time

#Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

#Define the GPIO pin connected to the servo signal line
servo_pin = 14

#Set up the GPIO pin as an output
GPIO.setup(servo_pin, GPIO.OUT)

#Create a PWM object with a frequency of 50 Hz
pwm = GPIO.PWM(servo_pin, 50)

#Function to set the servo angle
def set_servo_angle(angle):
    duty_cycle = (angle / 14) + 2
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.05)  # Give the servo some time to move
    pwm.ChangeDutyCycle(0)  # Turn off the PWM signal to hold the position

try:
    # Start the PWM
    pwm.start(0)

    while True:
        # Move the servo to 0 degrees
        set_servo_angle(0)
        time.sleep(2)

        # Move the servo to 90 degrees
        set_servo_angle(90)
        time.sleep(2)

        # Move the servo to 180 degrees
        set_servo_angle(180)
        time.sleep(2)

except KeyboardInterrupt:
    # Clean up GPIO on Ctrl+C exit
    pwm.stop()
    GPIO.cleanup()