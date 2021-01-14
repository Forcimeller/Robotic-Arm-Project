import time    #Imports the time module
import serial  #Imports the Serial module, used to communicate with the arduino

def CondimentMenu(): #Shows a menu for the user to select from
    print "**********************************"
    print "*  Please select your condiment  *"
    print "*      Type 'k' for Ketchup      *"
    print "*    Type 's' for Sweet Chilli   *"
    print "*        Type 'b' for BBQ        *"
    print "**********************************"
    condiment = raw_input() #Collects the options ans stores it in the condiment variable
    return condiment #Returns the condiment to the place of the function call
    
def Dispense(): #Squeezes the condiment bottle
    cmd = "3" + "," + "100" + "\n" #Specifies the command to claw servo (Servo 3) and sets the degree 100
    ser.write(cmd) #Writes the command to the arduino
    time.sleep(1) #Delays the program in order to account for any latency
    print "\n\nCondiment Dispensed. Enjoy!\n\n\n" #Tells the user athat the condiment is dispensed so that they can remove their food


def GraspAndLift(): #Grabs the bottle and lifts it out of position

    cmd = "3" + "," + "84" + "\n" #Specifies the command to claw servo (Servo 3) and sets the degree 100
    ser.write(cmd) #Writes the command to the arduino
    time.sleep(1) #Delays the program in order to account for any latency

    cmd = "1" + "," + "170" + "\n" #Specifies the command to left servo (Servo 1) and sets the degree 170
    ser.write(cmd) #Writes the command to the arduino
    time.sleep(1) #Delays the program in order to account for any latency

    cmd = "2" + "," + "90" + "\n" #Specifies the command to right servo (Servo 2) and sets the degree 100
    ser.write(cmd) #Writes the command to the arduino
    time.sleep(1) #Delays the program in order to account for any latency
    

def MoveToCentre(): #Moves the arm to the centre position

    cmd = "2" + "," + "90" + "\n" #Specifies the command to right servo (Servo 2) and sets the degree 100
    ser.write(cmd) #Writes the command to the arduino
    time.sleep(1) #Delays the program in order to account for any latency

    cmd = "1" + "," + "180" + "\n" #Specifies the command to left servo (Servo 1) and sets the degree 180
    ser.write(cmd) #Writes the command to the arduino
    time.sleep(1) #Delays the program in order to account for any latency

    cmd = "0" + "," + "90" + "\n" #Specifies the command to right servo (Servo 0) and sets the degree 90
    ser.write(cmd) #Writes the command to the arduino
    time.sleep(1) #Delays the program in order to account for any latency
    
def Ketchup(): #Dispenses the ketchup condiment
    print "\n\nNow dispensing your ketchup...\n\n\n"

    cmd = "3" + "," + "10" + "\n" #Specifies the command to claw servo (Servo 3) and sets the degree 10
    ser.write(cmd) #Writes the command to the arduino
    time.sleep(1) #Delays the program in order to account for any latency

    cmd = "0" + "," + "51" + "\n" #Specifies the command to right servo (Servo 0) and sets the degree 51
    ser.write(cmd) #Writes the command to the arduino
    time.sleep(1) #Delays the program in order to account for any latency

    cmd = "1" + "," + "140" + "\n" #Specifies the command to left servo (Servo 1) and sets the degree 140
    ser.write(cmd) #Writes the command to the arduino
    time.sleep(1) #Delays the program in order to account for any latency

    cmd = "2" + "," + "123" + "\n" #Specifies the command to right servo (Servo 2) and sets the degree 123
    ser.write(cmd) #Writes the command to the arduino
    time.sleep(1) #Delays the program in order to account for any latency
    GraspAndLift() #Calls upon the 'GraspAndLift' subroutine to run
    MoveToCentre() #Calls upon the 'MoveToCentre' subroutine to run
    Dispense() #Calls upon the 'Dispense' subroutine to run

    cmd = "0" + "," + "51" + "\n" #Specifies the command to right servo (Servo 0) and sets the degree 51
    ser.write(cmd) #Writes the command to the arduino
    time.sleep(1) #Delays the program in order to account for any latency

    cmd = "2" + "," + "121" + "\n" #Specifies the command to right servo (Servo 2) and sets the degree 121
    ser.write(cmd) #Writes the command to the arduino
    time.sleep(1) #Delays the program in order to account for any latency

    cmd = "1" + "," + "140" + "\n" #Specifies the command to left servo (Servo 1) and sets the degree 140
    ser.write(cmd) #Writes the command to the arduino
    time.sleep(1) #Delays the program in order to account for any latency

    cmd = "3" + "," + "10" + "\n" #Specifies the command to claw servo (Servo 3) and sets the degree 10
    ser.write(cmd) #Writes the command to the arduino
    time.sleep(1) #Delays the program in order to account for any latency
    MoveToCentre() #Calls upon the 'MoveToCentre' subroutine to run

def SweetChilli(): #Dispenses the Sweet Chilli condiment
    print "\n\nNow dispensing your sweet chilli...\n\n\n"

    cmd = "3" + "," + "10" + "\n" #Specifies the command to claw servo (Servo 3) and sets the degree 10
    ser.write(cmd) #Writes the command to the arduino
    time.sleep(1) #Delays the program in order to account for any latency

    cmd = "0" + "," + "70" + "\n" #Specifies the command to right servo (Servo 0) and sets the degree 70
    ser.write(cmd) #Writes the command to the arduino
    time.sleep(1) #Delays the program in order to account for any latency

    cmd = "1" + "," + "140" + "\n" #Specifies the command to left servo (Servo 1) and sets the degree 140
    ser.write(cmd) #Writes the command to the arduino
    time.sleep(1) #Delays the program in order to account for any latency

    cmd = "2" + "," + "137" + "\n" #Specifies the command to right servo (Servo 2) and sets the degree 137
    ser.write(cmd) #Writes the command to the arduino
    time.sleep(1) #Delays the program in order to account for any latency
    GraspAndLift() #Calls upon the 'GraspAndLift' subroutine to run
    MoveToCentre() #Calls upon the 'MoveToCentre' subroutine to run
    Dispense() #Calls upon the 'Dispense' subroutine to run

    cmd = "0" + "," + "70" + "\n" #Specifies the command to right servo (Servo 0) and sets the degree 70
    ser.write(cmd) #Writes the command to the arduino
    time.sleep(1) #Delays the program in order to account for any latency

    cmd = "2" + "," + "136" + "\n" #Specifies the command to right servo (Servo 2) and sets the degree 136
    ser.write(cmd) #Writes the command to the arduino
    time.sleep(1) #Delays the program in order to account for any latency

    cmd = "1" + "," + "140" + "\n" #Specifies the command to left servo (Servo 1) and sets the degree 140
    ser.write(cmd) #Writes the command to the arduino
    time.sleep(1) #Delays the program in order to account for any latency

    cmd = "3" + "," + "10" + "\n" #Specifies the command to claw servo (Servo 3) and sets the degree 10
    ser.write(cmd) #Writes the command to the arduino
    time.sleep(1) #Delays the program in order to account for any latency
    MoveToCentre() #Calls upon the 'MoveToCentre' subroutine to run
def BBQ(): #Dispenses the BBQ condiment
    print "\n\nNow dispensing your BBQ...\n\n\n"

    cmd = "3" + "," + "10" + "\n" #Specifies the command to claw servo (Servo 3) and sets the degree 10
    ser.write(cmd) #Writes the command to the arduino
    time.sleep(1) #Delays the program in order to account for any latency

    cmd = "0" + "," + "32" + "\n" #Specifies the command to right servo (Servo 0) and sets the degree 32
    ser.write(cmd) #Writes the command to the arduino
    time.sleep(1) #Delays the program in order to account for any latency

    cmd = "1" + "," + "139" + "\n" #Specifies the command to left servo (Servo 1) and sets the degree 139
    ser.write(cmd) #Writes the command to the arduino
    time.sleep(1) #Delays the program in order to account for any latency

    cmd = "2" + "," + "121" + "\n" #Specifies the command to right servo (Servo 2) and sets the degree 121
    ser.write(cmd) #Writes the command to the arduino
    time.sleep(1) #Delays the program in order to account for any latency
    GraspAndLift() #Calls upon the 'GraspAndLift' subroutine to run
    MoveToCentre() #Calls upon the 'MoveToCentre' subroutine to run
    Dispense() #Calls upon the 'Dispense' subroutine to run

    cmd = "0" + "," + "32" + "\n" #Specifies the command to right servo (Servo 0) and sets the degree 32
    ser.write(cmd) #Writes the command to the arduino
    time.sleep(1) #Delays the program in order to account for any latency

    cmd = "2" + "," + "121" + "\n" #Specifies the command to right servo (Servo 2) and sets the degree 121
    ser.write(cmd) #Writes the command to the arduino
    time.sleep(1) #Delays the program in order to account for any latency

    cmd = "1" + "," + "139" + "\n" #Specifies the command to left servo (Servo 1) and sets the degree 139
    ser.write(cmd) #Writes the command to the arduino
    time.sleep(1) #Delays the program in order to account for any latency

    cmd = "3" + "," + "10" + "\n" #Specifies the command to claw servo (Servo 3) and sets the degree 10
    ser.write(cmd) #Writes the command to the arduino
    time.sleep(1) #Delays the program in order to account for any latency
    MoveToCentre() #Calls upon the 'MoveToCentre' subroutine to run

try: #Excetion Handling block made to ensure that the device is connected before running the program
    usbport = 'COM3' #Sets the USB port as 'COM3'
    ser = serial.Serial(usbport, 9600, timeout=1) #Establishes a connection with the arduino uno
    try:#Excetion Handling block made to ensure that the servos are connected before running the program
        MoveToCentre() #Calls upon the 'MoveToCentre' subroutine to run

        cmd = "3" + "," + "10" + "\n" #Specifies the command to claw servo (Servo 3) and sets the degree 10
        ser.write(cmd) #Writes the command to the arduino
        time.sleep(1) #Delays the program in order to account for any latency
        while True: #Establishes an INFINITE Loop
            condimentSelection = CondimentMenu() #Calls the value returning function 'CondimentMenu' and stores the value in the 'condimentSelection' variable

            if condimentSelection == 'k' or condimentSelection == 'K':
                Ketchup() #Calls upon the 'Ketchup' subroutine to run if the user enters an upper or lower case 'k'
            elif condimentSelection == 's' or condimentSelection == 'S':
                SweetChilli() #Calls upon the 'SweetChilli' subroutine to run if the user enters an upper or lower case 's'
            elif condimentSelection == 'b' or condimentSelection == 'B':
                BBQ() #Calls upon the 'BBQ' subroutine to run if the user enters an upper or lower case 'b'
            else:
                print "You have selected an invalid condiment choice.\n \n" #Tells the user that there selection is invalid if they do not type in one of the options made available to them
    
    except:
        print "Callibration Error" #States that the robotic arm was unable to calibrate, meaning, potentially, that one or more of the servos are not connected - This only occurs if the second exception handling block fails.

except:
    print "Connection Error. Please Restart The Program." #States that the program failed to connect robotic arm - This only occurs if the first exception handling block fails.



