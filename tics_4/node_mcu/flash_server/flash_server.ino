#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <ESP8266mDNS.h>
#include <FS.h>

#ifndef STASSID
#define STASSID "" 
#define STAPSK  ""
#endif

const char* ssid = STASSID;
const char* password = STAPSK;
String file_name = "/data/acc.csv";
ESP8266WebServer server(80);
const int led = 2;

void sendFile(){ // send the right file to the client (if it exists)
  if(SPIFFS.exists(file_name)){                            // If the file exists
    Serial.println("arquivo existe");
    File file = SPIFFS.open(file_name, "r");                 // Open it
    size_t sent = server.streamFile(file, "text/plain"); // And send it to the client
    file.close();                                       // Then close the file again
  }
  else{
    Serial.println("\tFile Not Found");
    server.send(200, "text/plain", "Arquivo nao existe");
  }
}

void handleRoot() {
  digitalWrite(led, 0);
  delay(1000);
  server.send(200, "text/plain", "hello from esp8266!");
  digitalWrite(led, 1);
}

void handleNotFound(){
  digitalWrite(led, 0);
  String message = "File Not Found\n\n";
  message += "URI: ";
  message += server.uri();
  message += "\nMethod: ";
  message += (server.method() == HTTP_GET) ? "GET" : "POST";
  message += "\nArguments: ";
  message += server.args();
  message += "\n";
  for (uint8_t i = 0; i < server.args(); i++) {
    message += " " + server.argName(i) + ": " + server.arg(i) + "\n";
  }
  server.send(404, "text/plain", message);
  delay(1000);
  digitalWrite(led, 1);
}

void setup(void){
  pinMode(led, OUTPUT);
  digitalWrite(led, 1);
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  Serial.println("");
  // Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
  if(MDNS.begin("esp8266")){
    Serial.println("MDNS responder started");
  }
  server.on("/", handleRoot);
  server.on("/acc", sendFile);
  server.onNotFound(handleNotFound);
  server.begin();
  Serial.println("HTTP server started");
  if(SPIFFS.begin()){
      Serial.println("Sistema de arquivos aberto com sucesso!");
  }
  else{
    Serial.println("Erro ao abrir o sistema de arquivos");
  }
}

void loop(void) {
  server.handleClient();
  MDNS.update();
}
