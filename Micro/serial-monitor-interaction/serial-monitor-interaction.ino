#include <ArduinoJson.h>

int number = 0;
enum fstState
{
  STOP,
  CONFIG_CUSTOM,
  CHARGE_SCAN,
  CHARGE_SCAN_FULL_MATRIX
} state = STOP;

// int clockPin = 14;  //12;
// int dataPin = 11;

// MSB 10 bit
static uint16_t configArray[32]; // = {895,0,0,0,0,895,0,895,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
static uint16_t configSetup;

String selectedOperation;
StaticJsonDocument<600> doc;
DeserializationError err;

/*
{"operation":"STOP","data":[895,0,0,0,0,895,0,895,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"isFullMatrix": true}
*/

void setup()
{
  // pinMode(clockPin, OUTPUT);
  // pinMode(dataPin, OUTPUT);
  Serial.begin(9600);
}

void loop()
{

  // Check to see if anything is available in the serial receive buffer
  while (Serial.available() > 0)
  {
    // wait and elaborate communications from the PC
    err = deserializeJson(doc, Serial);

    if (err == DeserializationError::Ok)
    {

      Serial.print("Received: ");
      selectedOperation = doc["operation"].as<String>();
      Serial.println(selectedOperation);

      if (selectedOperation.equals("STOP"))
      {

        FiniteStateMachine(0);
      }
      else if (selectedOperation.equals("CONFIG_CUSTOM"))
      {

        for (int i = 0; i < 32; i++)
        {
          configArray[i] = doc["data"][i];
          Serial.print(configArray[i]);
        }
        Serial.println("\nCustom charge scan configuration");
        FiniteStateMachine(1);
      }
      else if (selectedOperation.equals("CHARGE_SCAN"))
      {

        FiniteStateMachine(2);
      }
      The above code is checking if the selected operation is equal to "CHARGE_SCAN_FULL_MATRIX". If it is, then it will print "Full matrix charge scan configuration" to the serial monitor. It will then set the configSetup variable to the value of the "setup" key in the JSON document. It will then print the value of configSetup to the serial monitor. It will then call the FiniteStateMachine function with the value 3.
      else if (selectedOperation.equals("CHARGE_SCAN_FULL_MATRIX"))
      {

        Serial.println("Full matrix charge scan configuration");
        configSetup = doc["setup"].as<uint16_t>();
        Serial.println(configSetup);
        FiniteStateMachine(3);
      }
      else
      {
        Serial.println("Unknown operation request");
      }
    }
    else
    {

      if (err.c_str() != "EmptyInput")
      {
        Serial.println(err.c_str());
      }
    }
  }
}

void FiniteStateMachine(int number)
{
  Serial.println("Entering Finite State machine");

  switch (number)
  {
  case (0):
    state = STOP;
    Serial.println("STOP");
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

    uint16_t fullMatrixConfig[32] = {configSetup, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

    // config the matrix enabling only the first pixel with the configuration data
    for (int i = 0; i < 32; i++)
    {
      Serial.println(fullMatrixConfig[i]);
      // shiftOut10(dataPin, clockPin, fullMatrixConfig[i]);
    }

    // charge scan every pixel
    for (int i = 0; i < 32; i++)
    {
      chargeScan();
      // then shift to the next pixel
      // shiftOut10(dataPin, clockPin, 0);
    }

    Serial.println("CHARGE_SCAN_FULL_MATRIX: Finished");
    break;
  }

  default:
  {
    Serial.println("default");
    break;
  }
  }
}

void shiftOut10(pin_size_t ulDataPin, pin_size_t ulClockPin, uint16_t ulVal)
{
  uint16_t i;

  for (i = 0; i < 10; i++)
  {
    digitalWrite(ulDataPin, !!(ulVal & (1 << (9 - i))));
    digitalWrite(ulClockPin, LOW);
    delay(50);
    digitalWrite(ulClockPin, HIGH);
    delay(50);
  }
}

void chargeScan()
{
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
