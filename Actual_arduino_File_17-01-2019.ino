/* SerialServo */

#include <Servo.h>

const int nbrServos = 4;
Servo myservo[nbrServos];  // create servo objects to control servos

void setup() {
  Serial.begin(9600);
  myservo[0].attach(11);  // attaches the Middle servo at pin 11 
  myservo[1].attach(10);  // attaches the Left servo at pin 10
  myservo[2].attach(9);  // attaches the Right servo to pin 9
  myservo[3].attach(6);  // attaches the Claw servo to pin 6

  
  myservo[0].write(90); //0 - 180
  delay(15);
  myservo[1].write(180-90); //180 - 90
  delay(15);
  myservo[2].write(90+30); //90 - 180
  delay(15);
  myservo[3].write(0); //35- 0
  delay(15);

}

void loop() {
  if (Serial.available() > 0) {
    int selectedServo = Serial.parseInt();
    if (selectedServo >= 0 && selectedServo < nbrServos) {
      int pos = Serial.parseInt();
      if (pos >= 10 && pos <= 170) {
        myservo[selectedServo].write(pos);
      }
    }
  }
}
