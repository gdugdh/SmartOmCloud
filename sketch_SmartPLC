#include <HTTPClient.h>
#include "DHT.h"

String URL = "http://localhost:8000";

#define DHTTYPE DHT11   // DHT 11
const char ssid[] = "YAKSE";  // Enter SSID here
const char password[] = "Qwezxc123";  //Enter Password here

uint8_t DHTPin = 5; 

DHT dht(DHTPin, DHTTYPE);
float Temperature;
float Humidity;

void setup() {
  Serial.begin(115200);
  delay(5000);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Соединяемся с Wi-Fi..");
  }
  Serial.println("Соединение с Wi-Fi установлено");
}

String getURL(String serverName) {
  String serverPath = serverName + "?temperature=";
  serverPath += dht.readTemperature();
  serverPath += "&humidity=";
  serverPath += dht.readHumidity();
  return serverPath;
}

void loop() {
  if ((WiFi.status() == WL_CONNECTED)) {
    HTTPClient http;
    http.begin(getURL(URL).c_str());
    int httpCode = http.GET();
    if (httpCode > 0) {
      String payload = http.getString();
      Serial.println(httpCode);
      Serial.println(payload);
    }
    else {
      Serial.println("Ошибка HTTP-запроса");
    }
    http.end();
  }
  delay(10000);
}
