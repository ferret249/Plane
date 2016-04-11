#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

import socket
try:
   import cPickle as pickle
except:
   import pickle

# Setup Variables & Socket
IP = '192.168.0.100'
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((IP, 5000))
print ("Ready")
servoMin = 150  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096

# Initialise the PWM device using the default address
pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)

# Define Servo Function
def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

while True:
   raw_message,data = s.recvfrom(1024)
   (data_x, data_y, data_s, data_z, JoyButton_0, JoyButton_1, JoyButton_2) = pickle.loads(raw_message)
   if JoyButton_0 == 1:
      print("heelo")
   if JoyButton_1 == 1:
      print("Potato")
   if JoyButton_2 == 1:
      print("Dog")


   if -100 <= data_x <= 100:
      Aileron_Servo = (data_x/200)+1.5
      setServoPulse(1, Aileron_Servo)
   if -100 <= data_y <= 100:
      Elevator_Servo = (data_y/200)+1.5
      setServoPulse(2, Elevator_Servo)
   if 0 <= data_s <= 100:
      Throttle_Servo = (data_s/100)+1
      setServoPulse(4, Throttle_Servo)
   if -100 <= data_z <= 100:
      Rudder_Servo = (data_y/200)+1.5
      setServoPulse(3, Rudder_Servo)
      




