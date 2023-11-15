import RPi.GPIO as GPIO
import pygame
import time

#Suppress GPIO warnings
GPIO.setwarnings(False)

#Set up GPIO for servo control
servo_pin1 = 14
servo_pin2 = 2
servo_pin3 = 3

#Define the servo pins for the new servos
servo_pin4 = 20  # Change to the desired GPIO pin for the 4th servo
servo_pin5 = 21  # Change to the desired GPIO pin for the 5th servo

#Set up GPIO for the new servos
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

#Start with 0% duty cycle for all servos
pwm1.start(0)
pwm2.start(0)
pwm3.start(0)
pwm4.start(0)
pwm5.start(0)

#Define the angle limits and duty cycle limits for the new servos
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

try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                # Handle button events
                if event.button == 0:
                    pwm1.ChangeDutyCycle(5)
                elif event.button == 3:
                    pwm1.ChangeDutyCycle(10)
                elif event.button == 1:
                    # Add your custom functionality for button B here
                    pass

            elif event.type == pygame.JOYBUTTONUP:
                pwm1.ChangeDutyCycle(0)

            if event.type == pygame.JOYHATMOTION:
                # Handle D-Pad events
                x, y = event.value
                if x == 1:
                    pwm3.ChangeDutyCycle(10)
                elif x == -1:
                    pwm3.ChangeDutyCycle(5)
                else:
                    pwm3.ChangeDutyCycle(0)

                if y == 1:
                    pwm2.ChangeDutyCycle(10)
                elif y == -1:
                    pwm2.ChangeDutyCycle(5)
                else:
                    pwm2.ChangeDutyCycle(0)

            if event.axis == 0:
                                # Handle the left stick's horizontal axis (event.axis 0)
                                angle4 = (event.value + 1) * 0.5 * (max_angle4 - min_angle4) + min_angle4
                                duty_cycle4 = (angle4 - min_angle4) / (max_angle4 - min_angle4) * (max_duty_cycle4 - min_duty_cycle4) + min_duty_cycle4
                                pwm4.ChangeDutyCycle(duty_cycle4)
            elif event.axis == 2:
                                # Handle the right stick's horizontal axis (event.axis 2)
                                angle5 = (event.value + 1) * 0.5 * (max_angle5 - min_angle5) + min_angle5
                                duty_cycle5 = (angle5 - min_angle5) / (max_angle5 - min_angle5) * (max_duty_cycle5 - min_duty_cycle5) + min_duty_cycle5
                                pwm5.ChangeDutyCycle(duty_cycle5)

        time.sleep(0.01)

except KeyboardInterrupt:
    pass
#Clean up GPIO
pwm1.stop()
pwm2.stop()
pwm3.stop()
pwm4.stop()
pwm5.stop()
GPIO.cleanup()