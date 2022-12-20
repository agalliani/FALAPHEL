const unsigned int MAX_MESSAGE_LENGTH = 12;

static char message[MAX_MESSAGE_LENGTH];  //Create a place to hold the incoming message
static unsigned int message_pos = 0;
char inByte;
int number = 0;

enum fstState { CONFIG,
                CHARGE_SCAN,
                STOP } state = STOP;



int clockPin = 14;  //12;
int dataPin = 11;

//MSB 10 bit
uint16_t configArray[32] = { 0x37F, 0x0, 0x0, 0x0, 0x0, 0x37F, 0x0, 0x37F, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0 };

String inputString;


void setup() {
  pinMode(clockPin, OUTPUT);
  pinMode(dataPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  //Check to see if anything is available in the serial receive buffer
  while (Serial.available() > 0) {
    //Read the next available byte in the serial receive buffer
    inputString = Serial.readString();

    Serial.print("Your selection: ");
    Serial.println(inputString);
    inputString.trim();
    if (inputString.equals("CONFIG")) {
      FiniteStateMachine(2);
    }
    else{
      Serial.println("NO");
    }
  }
}

void FiniteStateMachine(int number) {

  switch (number) {
    case (1):
      state = STOP;
      Serial.println("STOP");
      break;

    case (2):
      state = CONFIG;
      Serial.println("CONFIG");

      // shift out the bits:
      for (int i = 0; i < 32; i++) {
        shiftOut10(dataPin, clockPin, configArray[i]);
      }
      digitalWrite(clockPin, LOW);

      Serial.println("END CONFIG");


      break;

    case (3):
      state = CHARGE_SCAN;
      Serial.println("CHARGE_SCAN");
      break;

    default:
      Serial.println("default");
      break;
  }
}

void shiftOut10(pin_size_t ulDataPin, pin_size_t ulClockPin, uint16_t ulVal) {
  uint16_t i;

  for (i = 0; i < 10; i++) {
    digitalWrite(ulDataPin, !!(ulVal & (1 << (9 - i))));
    digitalWrite(ulClockPin, LOW);
    delay(50);
    digitalWrite(ulClockPin, HIGH);
    delay(50);
  }
}
