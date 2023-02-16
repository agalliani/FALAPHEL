const int pinInRise = 2;
const int pinInFall = 3;


volatile int state = LOW;

int up = 0, down = 0;
void setup() {
  // put your setup code here, to run once:
  pinMode(pinInRise, INPUT);
  pinMode(pinInFall, INPUT);

  attachInterrupt(pinInRise, riseUp, RISING);
  attachInterrupt(pinInFall, fallDown, FALLING);

  Serial.begin(9600);
}

void loop() {
  //Serial.println(state);
}


void riseUp() {
  Serial.println("H");
  state = HIGH;
}

void fallDown() {
  Serial.println("L");

  state = LOW;
}