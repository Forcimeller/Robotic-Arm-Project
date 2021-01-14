import time
import serial
import random

def CondimentMenu():
    print "**********************************"
    print "*  Please select your condiment  *"
    print "*      Type 'k' for Ketchup      *"
    print "*    Type 's' for Sweet Chilli   *"
    print "*        Type 'b' for BBQ        *"
    print "**********************************"
    condiment = raw_input()
    return condiment
    
def Dispense():
    #Insert Dispensation Code Here
    print "Condiment Dispensed. Enjoy!\n\n\n\n

def GraspAndLift():
    #Insert...

def MoveToCentre():
    #Middle Servo
    cmd = 0 + "," + 90 + "\n"
    ser.write(cmd)
    #Left Servo
    cmd = 1 + "," + 180 + "\n"
    ser.write(cmd)
    #Right Servo
    cmd = 2 + "," + 90 + "\n"
    ser.write(cmd)
    #Claw Servo
    cmd = 3 + "," + 82 + "\n"
    ser.write(cmd)
    
def Ketchup():
    print "Now dispensing your ketchup...\n\n"
    #Claw Servo
    cmd = 3 + "," + 45 + "\n"
    ser.write(cmd)
    #Middle Servo
    cmd = 0 + "," + 55 + "\n"
    ser.write(cmd)
    #Left Servo
    cmd = 1 + "," + 158 + "\n"
    ser.write(cmd)
    #Right Servo
    cmd = 2 + "," + 128 + "\n"
    ser.write(cmd)
    GraspAndLift()
    MoveToCentre()
    Dispense()
    #Middle Servo
    cmd = 0 + "," + 55 + "\n"
    ser.write(cmd)
    #Left Servo
    cmd = 1 + "," + 158 + "\n"
    ser.write(cmd)
    #Right Servo
    cmd = 2 + "," + 128 + "\n"
    #Claw Servo
    cmd = 3 + "," + 0 + "\n"
    ser.write(cmd)
    MoveToCentre()

def SweetChilli():
    print "Now dispensing your sweet chilli...\n\n"
    #Insert SweetChilli Fetch code here

def BBQ():
    print "Now dispensing your BBQ...\n\n"
    #Insert BBQ Fetch code here


try:
    try:
        usbport = COM3
        ser = serial.Serial(usbport, 9600, timeout=1)
    except:
        print "Connection Error. Please Restart The Program."            
    #Middle Servo
    cmd = 0 + "," + 90 + "\n"
    ser.write(cmd)
    #Left Servo
    cmd = 1 + "," + 180 + "\n"
    ser.write(cmd)
    #Right Servo
    cmd = 2 + "," + 90 + "\n"
    ser.write(cmd)
    #Claw Servo
    cmd = 3 + "," + 82 + "\n"
    ser.write(cmd)
except:
    print "Callibration Error"
    
while True:
    condimentSelection = CondimentMenu()

    if condimentSelection == 'k' or condimentSelection == 'K':
        Ketchup()
    elif condimentSelection == 's' or condimentSelection == 'S':
        SweetChilli()
    elif condimentSelection == 'b' or condimentSelection == 'B':
        BBQ()
    else:
        print "You have selected an invalid condiment choice.\n \n"
