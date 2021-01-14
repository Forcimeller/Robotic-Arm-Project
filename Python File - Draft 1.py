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
    #Claw Servo
    cmd = "3" + "," + "100" + "\n"

    time.sleep(1)
    print "\n\nCondiment Dispensed. Enjoy!\n\n\n"

def GraspAndLift():
    #Claw Servo
    cmd = "3" + "," + "84" + "\n"

    time.sleep(1)

    #Left Servo
    cmd = "1" + "," + "170" + "\n"

    time.sleep(1)

    #Right Servo
    cmd = "2" + "," + "90" + "\n"

    time.sleep(1)
    

def MoveToCentre():
    #Right Servo
    cmd = "2" + "," + "90" + "\n"

    time.sleep(1)
    #Left Servo
    cmd = "1" + "," + "180" + "\n"

    time.sleep(1)
    #Middle Servo
    cmd = "0" + "," + "90" + "\n"

    time.sleep(1)
    
def Ketchup():
    print "\n\nNow dispensing your ketchup...\n\n\n"
    #Claw Servo
    cmd = "3" + "," + "10" + "\n"

    time.sleep(1)
    #Middle Servo
    cmd = "0" + "," + "51" + "\n"
 
    time.sleep(1)
    #Left Servo
    cmd = "1" + "," + "140" + "\n"

    time.sleep(1)
    #Right Servo
    cmd = "2" + "," + "123" + "\n"

    time.sleep(1)
    GraspAndLift()
    MoveToCentre()
    Dispense()
    #Middle Servo
    cmd = "0" + "," + "51" + "\n"

    time.sleep(1)
    #Right Servo
    cmd = "2" + "," + "121" + "\n"

    time.sleep(1)
    #Left Servo
    cmd = "1" + "," + "140" + "\n"

    time.sleep(1)
    #Claw Servo
    cmd = "3" + "," + "10" + "\n"

    time.sleep(1)
    MoveToCentre()

def SweetChilli():
    print "\n\nNow dispensing your sweet chilli...\n\n\n"
    #Insert SweetChilli Fetch code here
    #Claw Servo
    cmd = "3" + "," + "10" + "\n"

    time.sleep(1)
    #Middle Servo
    cmd = "0" + "," + "70" + "\n"

    time.sleep(1)
    #Left Servo
    cmd = "1" + "," + "140" + "\n"

    time.sleep(1)
    #Right Servo
    cmd = "2" + "," + "137" + "\n"

    time.sleep(1)
    GraspAndLift()
    MoveToCentre()
    Dispense()
    #Middle Servo
    cmd = "0" + "," + "70" + "\n"

    time.sleep(1)
    #Right Servo
    cmd = "2" + "," + "136" + "\n"

    time.sleep(1)
    #Left Servo
    cmd = "1" + "," + "140" + "\n"

    time.sleep(1)
    #Claw Servo
    cmd = "3" + "," + "10" + "\n"

    time.sleep(1)
    MoveToCentre()
def BBQ():
    print "\n\nNow dispensing your BBQ...\n\n\n"
    #Claw Servo
    cmd = "3" + "," + "10" + "\n"

    time.sleep(1)
    #Middle Servo
    cmd = "0" + "," + "32" + "\n"

    time.sleep(1)
    #Left Servo
    cmd = "1" + "," + "139" + "\n"

    time.sleep(1)
    #Right Servo
    cmd = "2" + "," + "121" + "\n"

    time.sleep(1)
    GraspAndLift()
    MoveToCentre()
    Dispense()
    #Middle Servo
    cmd = "0" + "," + "32" + "\n"

    time.sleep(1)
    #Right Servo
    cmd = "2" + "," + "121" + "\n"

    time.sleep(1)
    #Left Servo
    cmd = "1" + "," + "139" + "\n"

    time.sleep(1)
    #Claw Servo
    cmd = "3" + "," + "10" + "\n"

    time.sleep(1)
    MoveToCentre()


MoveToCentre()
#Claw Servo
cmd = "3" + "," + "10" + "\n"

time.sleep(1)
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
