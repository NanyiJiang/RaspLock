from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor

import time
import atexit

mh = Adafruit_MotorHAT(addr = 0x60)

def turn_off_motor():
  mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
  mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
  mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
  mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

myStepper = mh.getStepper(200, 1)
myStepper.setSpeed(30)
def step(n):
  if n > 0:
    dir = Adafruit_MotorHAT.BACKWARD
  else:
    dir = Adafruit_MotorHAT.FORWARD
  myStepper.step(abs(n), dir, Adafruit_MotorHAT.DOUBLE)
  turn_off_motor()

def lock():
  step(150)

def unlock():
  step(-150)