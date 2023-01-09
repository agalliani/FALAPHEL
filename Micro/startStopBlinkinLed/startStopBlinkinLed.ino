int i = 0;

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);

  Serial.begin(9600);  // opens serial port, sets data rate to 9600 bps
}

void loop() {

  if (Serial.available() > 0) {
    // read the incoming string:
    String incomingString = Serial.readString();
    incomingString.trim();
    if (incomingString.equals("START")) {
      digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on (HIGH is the voltage level)
    }
    if (incomingString.equals("STOP")) {
      // wait for a second
      digitalWrite(LED_BUILTIN, LOW);
    }

    // prints the received data
    Serial.print("I received: ");
    Serial.println(incomingString);
  }
  delay(1000);
}