import RPi.GPIO as GPIO
import time
import math
import evdev
import board
import busio
import pygame
import time

#Suppress GPIO warnings
GPIO.setwarnings(False)

#Set up GPIO for servo control
servo_pin1 = 14
servo_pin2 = 2
servo_pin3 = 3

#Set up GPIO for servo control
servo_pin4 = 20  # Change to the desired GPIO pin for servo 4
servo_pin5 = 21  # Change to the desired GPIO pin for servo 5

#Set up GPIO for the servos
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin1, GPIO.OUT)
GPIO.setup(servo_pin2, GPIO.OUT)
GPIO.setup(servo_pin3, GPIO.OUT)
GPIO.setup(servo_pin4, GPIO.OUT)
GPIO.setup(servo_pin5, GPIO.OUT)

#Initialize the servo motors
pwm1 = GPIO.PWM(servo_pin1, 50)
pwm2 = GPIO.PWM(servo_pin2, 50)
pwm3 = GPIO.PWM(servo_pin3, 50)
pwm4 = GPIO.PWM(servo_pin4, 50)
pwm5 = GPIO.PWM(servo_pin5, 50)

#Start with 0% duty cycle for both servos
pwm1.start(0)
pwm2.start(0)
pwm3.start(0)
pwm4.start(0)
pwm5.start(0)

#Define the angle and duty cycle limits for both servos
min_angle4 = 0
max_angle4 = 180
min_duty_cycle4 = 2.5
max_duty_cycle4 = 12.5

min_angle5 = 0
max_angle5 = 180
min_duty_cycle5 = 2.5
max_duty_cycle5 = 12.5

#Initialize the pygame module
pygame.init()

#Initialize the Xbox controller
controller = pygame.joystick.Joystick(0)
controller.init()


#Initialize the Xbox controller
devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
controller = None

for device in devices:
    if "Pro Controller" in device.name:
        controller = evdev.InputDevice(device.path)

if not controller:
    print("Xbox controller not found. Make sure it's connected.")
    exit()

print("Xbox controller found and connected.")

try:
    while True:

        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:  # A button (button index may vary)
                    # Rotate servo 1 to the left (counterclockwise)
                    pwm1.ChangeDutyCycle(5)  # Adjust this value as needed
                elif event.button == 3:  # Y button (button index may vary)
                    # Rotate servo 1 to the right (clockwise)
                    pwm1.ChangeDutyCycle(10)  # Adjust this value as needed
                if event.button == 4:  # Button 4
                    # Rotate servo 4 to the left (counterclockwise) by 30 degrees when button 4 is pressed
                    angle4 = max(min_angle4, min_angle4 + 30)
                    angle5 = max(max_angle5, max_angle5 - 30)
                    duty_cycle4 = (angle4 - min_angle4) / (max_angle4 - min_angle4) * (max_duty_cycle4 - min_duty_cycle4) + min_duty_cycle4
                    duty_cycle5 = (angle5 - min_angle5) / (max_angle5 - min_angle5) * (max_duty_cycle5 - min_duty_cycle5) + min_duty_cycle5
                    pwm4.ChangeDutyCycle(duty_cycle4)
                    pwm5.ChangeDutyCycle(duty_cycle5)

                elif event.button == 5:  # Button 5
                    # Rotate servo 4 to the right (clockwise) by 30 degrees when button 5 is pressed
                    angle4 = min(max_angle4, max_angle4 - 30)
                    angle5 = min(min_angle5, min_angle5 + 30)
                    duty_cycle4 = (angle4 - min_angle4) / (max_angle4 - min_angle4) * (max_duty_cycle4 - min_duty_cycle4) + min_duty_cycle4
                    duty_cycle5 = (angle5 - min_angle5) / (max_angle5 - min_angle5) * (max_duty_cycle5 - min_duty_cycle5) + min_duty_cycle5
                    pwm4.ChangeDutyCycle(duty_cycle4)
                    pwm5.ChangeDutyCycle(duty_cycle5)

            elif event.type == pygame.JOYBUTTONUP:
                # Stop servo 1 when the button is released
                pwm1.ChangeDutyCycle(0)
                # Stop servo 4 when the button is released
                pwm4.ChangeDutyCycle(0)
                # Stop servo 5 when the button is released
                pwm5.ChangeDutyCycle(0)
                
            if event.type == pygame.JOYHATMOTION:
                            # Handle D-Pad events
                            x, y = event.value
                            if x == 1:
                                # Move servo 3 to the right (clockwise)
                                pwm3.ChangeDutyCycle(10)  # Adjust this value as needed
                            elif x == -1:
                                # Move servo 3 to the left (counterclockwise)
                                pwm3.ChangeDutyCycle(5)  # Adjust this value as needed
                            else:
                                pwm3.ChangeDutyCycle(0)  # Stop servo 3

                            if y == 1:
                                # Move servo 2 up
                                pwm2.ChangeDutyCycle(10)  # Adjust this value as needed
                            elif y == -1:
                                # Move servo 2 down
                                pwm2.ChangeDutyCycle(5)  # Adjust this value as needed
                            else:
                                pwm2.ChangeDutyCycle(0)  # Stop servo 2

        time.sleep(0.01)

except KeyboardInterrupt:
    pass

# Clean up GPIO
pwm1.stop()
pwm2.stop()
pwm3.stop()
pwm4.stop()
pwm5.stop()
GPIO.cleanup()