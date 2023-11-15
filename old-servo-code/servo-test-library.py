from piservo import Servo
import time

myservo = Servo(19, min_value=0, max_value=180, min_pulse=0.5, max_pulse=2.4, frequency=333)

myservo.write(180)
time.sleep(1)
myservo.write(0)
time.sleep(1)
myservo.write(90)
time.sleep(1)
myservo.stop()