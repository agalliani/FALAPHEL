const int pinOut = 13;
const int pinInRise = 2;
const int pinInFall = 3;

volatile int state = LOW;
long int count = 0, flag = 0;

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

  if (count > 10000) {
    Serial.print(flag);
    Serial.println(" - Up charge");
    flag +=1;
    count = 0;
  }
}

void riseUp() {
  state = HIGH;

}

void fallDown() {
  state = LOW;
  count = count + 1;
}
