
//Pin connected to ST_CP of 74HC595
int latchPin = 8;
//Pin connected to SH_CP of 74HC595
int clockPin = 14;  //12;
////Pin connected to DS of 74HC595
int dataPin = 11;

//MSB 10 bit
uint16_t configArray[32] = { 0x37F, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0 };



void setup() {
  //set pins to output so you can control the shift register
  pinMode(latchPin, OUTPUT);
  pinMode(clockPin, OUTPUT);
  pinMode(dataPin, OUTPUT);
}


void loop() {

  digitalWrite(latchPin, LOW);
  // shift out the bits:
  for (int i = 0; i < 32; i++) {
    shiftOut10(dataPin, clockPin, configArray[i]);
  }

  //take the latch pin high so the LEDs will light up:
  digitalWrite(latchPin, HIGH);
}


/**
Positive edge SR driver MSBFIRST working at 9 kHz.
ulDataPin: output pin 
ulClockPin: clock pin
ulVal: uint16_t number to shift out to the SR
*/
void shiftOut10(pin_size_t ulDataPin, pin_size_t ulClockPin, uint16_t ulVal) {
  uint16_t i;

  for (i = 0; i < 10; i++) {
    digitalWrite(ulDataPin, !!(ulVal & (1 << (9 - i))));
    digitalWrite(ulClockPin, LOW);
    delayMicroseconds(50);
    digitalWrite(ulClockPin, HIGH);
    delayMicroseconds(50);
  }
}