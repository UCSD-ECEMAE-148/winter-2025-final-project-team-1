void setup() {
  Serial.begin(9600);
  pinMode(PD7, OUTPUT);
}

void loop() {
  if (Serial.available() > 0){
    String msg = Serial.readString();

    if (msg == "ON"){
      digitalWrite(PD7, HIGH);
      Serial.print("ON");
    }
    else if (msg == "OFF"){
      digitalWrite(PD7, LOW);
      Serial.print("OFF");
    }
    else {
      for (int i = 0; i < 5; i++){
        digitalWrite(PD7, HIGH);
        delay(100);
        digitalWrite(PD7, LOW);
        delay(100);
      }
    }
  }
}