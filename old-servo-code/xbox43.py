import RPi.GPIO as GPIO
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

button0_pressed = False
button3_pressed = False
button4_pressed = False
button5_pressed = False
try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:
                    # Button 0 is pressed
                    button0_pressed = True
                elif event.button == 3:
                    # Button 3 is pressed
                    button3_pressed = True
                elif event.button == 4:
                    # Button 4 is pressed
                    button4_pressed = True
                elif event.button == 5:
                    # Button 5 is pressed
                    button5_pressed = True

            elif event.type == pygame.JOYBUTTONUP:
                if event.button == 0:
                    # Button 0 is released
                    button0_pressed = False
                elif event.button == 3:
                    # Button 3 is released
                    button3_pressed = False 
                elif event.button == 4:
                    # Button 4 is released
                    button4_pressed = False
                elif event.button == 5:
                    # Button 5 is released
                    button5_pressed = False
        # Rotate servo 1  when button 0 is pressed
        if button0_pressed:
            pwm1.ChangeDutyCycle(5)
       # Rotate servo 1  when button 3 is pressed
    if button3_pressed:
            pwm1.ChangeDutyCycle(10)


# Rotate servo 4 by 30 degrees when button 4 is pressed
        if button4_pressed:
            angle4 = min(max_angle4, min_angle4 + 30)
            duty_cycle4 = (angle4 - min_angle4) / (max_angle4 - min_angle4) * (max_duty_cycle4 - min_duty_cycle4) + min_duty_cycle4
            pwm4.ChangeDutyCycle(duty_cycle4)

        # Rotate servo 5 by 30 degrees when button 5 is pressed
        if button5_pressed:
            angle5 = min(max_angle5, min_angle5 + 30)
            duty_cycle5 = (angle5 - min_angle5) / (max_angle5 - min_angle5) * (max_duty_cycle5 - min_duty_cycle5) + min_duty_cycle5
            pwm5.ChangeDutyCycle(duty_cycle5)
    
        if event.type == pygame.JOYHATMOTION:
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