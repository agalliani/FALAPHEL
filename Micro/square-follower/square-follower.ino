const int pinOut = 4;    
const int pinInRise = 2;  
const int pinInFall = 3;

volatile int state = LOW;

void setup() {
  // put your setup code here, to run once:
  pinMode(pinInRise, INPUT);
  pinMode(pinInFall, INPUT);

  pinMode(pinOut, OUTPUT);

  attachInterrupt(pinInRise, riseUp, RISING);
  attachInterrupt(pinInFall, fallDown, FALLING);

  Serial.begin(9600);
}

void loop() {
  digitalWrite(pinOut, state);
}

void riseUp() {
  state = HIGH;
}

void fallDown() {
  state = LOW;
}
