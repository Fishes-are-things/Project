# Import libraries


#Numbers 2 = 0°, 12 = 180°
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50) # pin 11 for servo1

print("Wave maker starting")
 # Start PWM running on both servos, value of 0 (pulse off)
servo1.start(0)
servo2.start(0)

import keyboard

while True:
    if keyboard.is_pressed("some key"):
        break

   time.sleep(0.5)
  servo1.ChangeDutyCycle(2)

  # Wait for 2 seconds
  time.sleep(2)


  servo1.ChangeDutyCycle(12)
  time.sleep(0.5)

  servo1.ChangeDutyCycle(2)

  # Wait again for 2 seconds! :)
  time.sleep(2)

  servo1.ChangeDutyCycle(12)
  time.sleep(0.5)

  servo1.ChangeDutyCycle(2)

  # Wait again for 2 seconds! :)
  time.sleep(0.5)

  servo1.ChangeDutyCycle(12)
  time.sleep(0.5)

  servo1.ChangeDutyCycle(2)

  # Wait again for 2 seconds! :)
  time.sleep(0.5)

  servo1.ChangeDutyCycle(12)
  time.sleep(0.5)

  servo1.ChangeDutyCycle(2)

  # Wait again for 2 seconds! :)
  time.sleep(0.5)

  servo1.ChangeDutyCycle(12)
  time.sleep(0.5)

  servo1.ChangeDutyCycle(2)

  # Wait again for 2 seconds! :)
  time.sleep(0.5)

  servo1.ChangeDutyCycle(12)
  time.sleep(0.5)

  servo1.ChangeDutyCycle(2)

  # Wait again for 2 seconds! :)
  time.sleep(0.5)

  servo1.ChangeDutyCycle(12)
  time.sleep(0.5)

  servo1.ChangeDutyCycle(2)

  # Wait again for 2 seconds! :)
  time.sleep(0.5)

  servo1.ChangeDutyCycle(12)
  time.sleep(0.5)

  servo1.ChangeDutyCycle(2)

  # Wait again for 2 seconds! :)
  time.sleep(0.5)

  servo1.ChangeDutyCycle(12)
  time.sleep(0.5)

  servo1.ChangeDutyCycle(2)

  # Wait again for 2 seconds! :)
  time.sleep(0.5)

  servo1.ChangeDutyCycle(12)
  time.sleep(0.5)

  servo1.ChangeDutyCycle(2)

  # Wait again for 2 seconds! :)
  time.sleep(0.5)

  servo1.ChangeDutyCycle(12)
  time.sleep(0.5)

  servo1.ChangeDutyCycle(2)

  # Wait again for 2 seconds! :)
  time.sleep(0.5)

  servo1.ChangeDutyCycle(12)
  time.sleep(0.5)
  servo1.ChangeDutyCycle(2)

  # Wait again for 2 seconds! :)
  time.sleep(2)

  #reset


  servo1.ChangeDutyCycle(7)
  time.sleep(2)
 
  servo1.ChangeDutyCycle(7)
  


  time.sleep(5)
  if keyboard.is_pressed("some key"):
        break
###############################################

  servo1.ChangeDutyCycle(7)
  time.sleep(2)
 
  servo1.ChangeDutyCycle(7)
  

#Clean things up at the end
servo1.stop()
servo2.stop()
GPIO.cleanup()
print ("wave maker finished")
