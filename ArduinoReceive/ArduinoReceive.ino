#include <Servo.h>

Servo myservo;  // create servo object to control a servo

void setup() {
  Serial.begin(9600);       // initialize serial communication
  myservo.attach(37);       // attaches the servo on pin 32 to the servo object
  pinMode(13,OUTPUT);
}

void loop() {
  if (Serial.available()) {
    String received = Serial.readStringUntil('\n');
   
    if (received == "Class 1") {
      digitalWrite(13,HIGH);
      myservo.write(180);   // turn servo to 180 degrees
      delay(500);
    } else if (received == "Class 2") {
      myservo.write(0);     // turn servo to 0 degrees
      delay(500);
      digitalWrite(13,HIGH);
    } else {
      myservo.write(90);    // for any other input, turn servo to 90 degrees
    digitalWrite(13,LOW);
    delay(500);
    }
  }
  
}
