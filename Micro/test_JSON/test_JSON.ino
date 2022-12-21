#include <ArduinoJson.h>

uint16_t configArray[32] = { 895, 0, 0, 0, 0, 895, 0, 895, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 };



void setup() {


  // Initialize the "link" serial port
  // Use a low data rate to reduce the error ratio
  Serial.begin(9600);
}

void loop() {
  // Values we want to transmit
  /*long timestamp = millis();
  int value = analogRead(1);
*/
  // Print the values on the "debug" serial port
  /*Serial.print("timestamp = ");
  Serial.println(timestamp);
  Serial.print("value = ");
  Serial.println(value);
  Serial.println("---");
  */

  // Create the JSON document
  StaticJsonDocument<600> doc;

  JsonObject object = doc.to<JsonObject>();
  object["operation"] = "CONFIG";

  JsonArray array = doc["data"].to<JsonArray>();

  for (int i = 0; i < 32; i++) {
    array.add(configArray[i]);
  }









  //doc["value"] = value;

  /*
  StaticJsonDocument<800> doc;
  DeserializationError err = deserializeJson(doc, Serial);

*/

  // Send the JSON document over the "link" serial port
  /*if (err == DeserializationError::Ok) {
    
    serializeJson(doc, Serial);
    Serial.println("");
  } */
  serializeJson(doc, Serial);
  Serial.println("");

  // Wait
  delay(5000);
}