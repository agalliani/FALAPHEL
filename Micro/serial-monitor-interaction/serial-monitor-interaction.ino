#include <ArduinoJson.h>

const int pinOut = 4;
const int pinInRise = 2;
const int pinInFall = 3;

volatile int clonedSignal = LOW;

volatile bool isChargeScanActive = true;
volatile long int count = 0, flag = 0;



int number = 0;
enum fstState {
  STOP,
  CONFIG_CUSTOM,
  CHARGE_SCAN,
  CHARGE_SCAN_FULL_MATRIX,
  START
} state = STOP;

// int clockPin = 14;  //12;
// int dataPin = 11;

// MSB 10 bit
static uint16_t configArray[32];  // = {895,0,0,0,0,895,0,895,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
static uint16_t configSetup;




String selectedOperation;
StaticJsonDocument<600> doc;
DeserializationError err;

/*
{"operation":"STOP","data":[895,0,0,0,0,895,0,895,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"isFullMatrix": true}
*/

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);

  pinMode(pinInRise, INPUT);
  pinMode(pinInFall, INPUT);

  pinMode(pinOut, OUTPUT);


  // pinMode(clockPin, OUTPUT);
  // pinMode(dataPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {





  // Check to see if anything is available in the serial receive buffer
  while (Serial.available() > 0) {
    // wait and elaborate communications from the PC
    err = deserializeJson(doc, Serial);

    if (err == DeserializationError::Ok) {

      Serial.print("Received: ");
      selectedOperation = doc["operation"].as<String>();
      Serial.println(selectedOperation);

      if (selectedOperation.equals("STOP")) {

        FiniteStateMachine(0);
      } else if (selectedOperation.equals("CONFIG_CUSTOM")) {

        for (int i = 0; i < 32; i++) {
          configArray[i] = doc["data"][i];
          Serial.print(configArray[i]);
        }
        Serial.println("\nCustom charge scan configuration");
        FiniteStateMachine(1);
      } else if (selectedOperation.equals("CHARGE_SCAN")) {

        FiniteStateMachine(2);
      }
      //The above code is checking if the selected operation is equal to "CHARGE_SCAN_FULL_MATRIX". If it is, then it will print "Full matrix charge scan configuration" to the serial monitor. It will then set the configSetup variable to the value of the "setup" key in the JSON document. It will then print the value of configSetup to the serial monitor. It will then call the FiniteStateMachine function with the value 3.
      else if (selectedOperation.equals("CHARGE_SCAN_FULL_MATRIX")) {

        String s = doc["setup"].as<String>();
        //Serial.println(s);

        int value = 0;
        for (int i = 0; i < s.length(); i++)  // for every character in the string  strlen(s) returns the length of a char array
        {
          value *= 2;                // double the result so far
          if (s[i] == '1') value++;  //add 1 if needed
        }
        configSetup = value;


        // prepare matrix configuration data
        uint16_t fullMatrixConfig[32] = { configSetup, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

        // config the matrix enabling only the first pixel with the configuration data
        for (int i = 0; i < 32; i++) {
          Serial.print(fullMatrixConfig[i]);
          Serial.print(" ");
          // shiftOut10(dataPin, clockPin, fullMatrixConfig[i]);
        }

        // config number of injection and its amplitude
        int numInj = doc["numInj"].as<String>().toInt();

        int numStep = doc["numStep"].as<String>().toInt();
        int Qmin = doc["Qmin"].as<String>().toInt();
        int Qmax = doc["Qmax"].as<String>().toInt();

        int deltaAmplitude = (Qmax - Qmin)/numStep;
        int cumulatedAmplitude = Qmax;




        
        Serial.println("");

        Serial.print("FCS1-");
        Serial.print(Qmax);
        Serial.print("-");
        Serial.print("PRIMA CONFIGURAZIONE MATRICE IMPOSTATA");
        Serial.println("");

        isChargeScanActive = true;
        flag = 0;


        delay(6000); //await for instrument to trigger signal generation


        attachInterrupt(pinInRise, riseUp, RISING);
        attachInterrupt(pinInFall, fallDown, FALLING);
        Serial.println("ATTACHED interrupts");
        while (isChargeScanActive) {
          digitalWrite(pinOut, clonedSignal);


          if (count >= numInj) {
            
            count = 0;

            Serial.print("UPAMP-");
            Serial.print(flag);
            Serial.print("-");
            Serial.print(cumulatedAmplitude); 
            Serial.println("");
            cumulatedAmplitude -= deltaAmplitude;
            flag++;

          }

          if(flag > numStep){
            isChargeScanActive = false;

          }
        }

        detachInterrupt(pinInRise);
        detachInterrupt(pinInFall);
        Serial.println("DETATCHED Interrupts");

        Serial.println("EOC");



        //FiniteStateMachine(3);
      } else if (selectedOperation.equals("START")) {

        Serial.println("LED ON");
        FiniteStateMachine(4);
      } else {
        Serial.println("Unknown operation request");
      }
    } else {

      if (err.c_str() != "EmptyInput") {
        Serial.println(err.c_str());
      }
    }
  }
}

void FiniteStateMachine(int number) {
  Serial.println("Entering Finite State machine");

  switch (number) {
    case (0):
      state = STOP;
      Serial.println("STOP");
      digitalWrite(LED_BUILTIN, LOW);

      break;

    case (1):
      {

        state = CONFIG_CUSTOM;
        Serial.println("CONFIG_CUSTOM: Started");
        delay(5000);
        /*
  // shift out the bits:
  for (int i = 0; i < 32; i++) {
    shiftOut10(dataPin, clockPin, configArray[i]);
  }
  digitalWrite(clockPin, LOW);
  */
        Serial.println("CONFIG_CUSTOM: Finished");
        break;
      }
    case (2):
      {
        state = CHARGE_SCAN;
        Serial.println("CHARGE_SCAN: Started");
        chargeScan();
        Serial.println("CHARGE_SCAN: Finished");

        break;
      }
    case (3):
      {
        state = CHARGE_SCAN_FULL_MATRIX;
        Serial.println("CHARGE_SCAN_FULL_MATRIX: Started");
        // prepare matrix configuration data

        uint16_t fullMatrixConfig[32] = { configSetup, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

        // config the matrix enabling only the first pixel with the configuration data
        for (int i = 0; i < 32; i++) {
          Serial.println(fullMatrixConfig[i]);
          // shiftOut10(dataPin, clockPin, fullMatrixConfig[i]);
        }

        // charge scan every pixel
        for (int i = 0; i < 32; i++) {
          chargeScan();
          // then shift to the next pixel
          // shiftOut10(dataPin, clockPin, 0);
        }

        Serial.println("CHARGE_SCAN_FULL_MATRIX: Finished");
        break;
      }
    case (4):
      {
        state = START;
        digitalWrite(LED_BUILTIN, HIGH);
      }

    default:
      {
        Serial.println("default");
        break;
      }
  }

  Serial.println("EOC");
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

void chargeScan() {
  /*
  int count = 0;
  while (count < 100) {
    // read TTL
    // reset outputs on rising edges
    // read outputs on falling edges
    // Serial print formatted read results
  }
  */
  Serial.println("Charge scan");
}


void riseUp() {
  clonedSignal = HIGH;
}

void fallDown() {
  clonedSignal = LOW;
  count = count + 1;
}
