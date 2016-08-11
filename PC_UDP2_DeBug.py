#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

import socket
try:
   import cPickle as pickle
except:
   import pickle

# Setup Variables & Socket
IP = '192.168.0.122'
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((IP, 5000))
print ("Ready")
servoMin = 150  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096

#Error Variables
Error_1 = "Servo 0 Problem"
Error_2 = "Servo 1 Problem"
Error_3 = "Servo 2 Problem"
Error_4 = "Servo 3 Problem"
Error_5 = "Servo 4 Problem"
Error_6 = "Recv Problem"

# Initialise the PWM device using the default address
pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)
pwm.setPWMFreq(60) # Set the Frequency to 60hz

while True:
   try:
      raw_message,data = s.recvfrom(1024)
   except:
      print(Error_6)
   (data_x, data_y, data_s, data_z, JoyButton_0, JoyButton_1, JoyButton_2) = pickle.loads(raw_message)
   if JoyButton_0 == 1:
      print("heelo")
   if JoyButton_1 == 1:
      print("Potato")
   if JoyButton_2 == 1:
      print("Dog")

   Aileron_Servo = (2.25*data_x)+375
   Elevator_Servo = (2.25*data_y)+375
   Throttle_Servo = (4.5*data_s)+150
   Rudder_Servo = (2.25*data_z)+375
   

   if 150 <= Aileron_Servo <= 600:
      Servo0 = Alieron_Servo
      try:
         pwm.setPWM(0, 0, Servo0)
      except:
         print(Error_1)
   if 150 <= Elevator_Servo <= 600:
      Servo1 = Elevator_Servo
      try:
         pwm.setPWM(1, 0, Elevator_Servo)
      except:
         print(Error_2)
   if 150 <= Throttle_Servo <= 600:
      Servo2 = Throttle_Servo
      try:
         pwm.setPWM(2, 0, Throttle_Servo)
      except:
         print(Error_4)
   if 150 <= Rudder_Servo <= 600:
      Servo3 = Rudder_Servo
      try:
         pwm.setPWM(3, 0, Rudder_Servo)
      except:
         print(Error_5)
      




