#include <NTPClient.h>
#include <WiFiUdp.h>
#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include "I2Cdev.h"
#include "MPU6050_6Axis_MotionApps20.h"
#if I2CDEV_IMPLEMENTATION == I2CDEV_ARDUINO_WIRE
#include "Wire.h"
#endif

const char* ssid = "...";
const char* password = "!123?QWE...";
//const char* mqtt_server = "demo.thingsboard.io";
//const char* device_token = "XM5DQeXupU6OzvF06sDP"; // THINGSBOARD DEMO
const char* mqtt_server = "10.0.0.103";
const char* device_token = "7SWvR7FGz8Rf77jG5l52"; // THINGSBOARD LOCAL
WiFiClient wifi_client;
PubSubClient mqtt_client(wifi_client);
double _time;
double  _time_plus;
double  last_time;
double  _time_mili;
WiFiUDP ntpUDP;
NTPClient timeClient(ntpUDP, "pool.ntp.org", 0); //set uct-0
MPU6050 mpu;
bool blinkState = false;
// MPU control/status vars
bool dmpReady = false;  // set true if DMP init was successful
uint8_t mpuIntStatus;   // holds actual interrupt status byte from MPU
uint8_t devStatus;      // return status after each device operation (0 = success, !0 = error)
uint16_t packetSize;    // expected DMP packet size (default is 42 bytes)
uint16_t fifoCount;     // count of all bytes currently in FIFO
uint8_t fifoBuffer[64]; // FIFO storage buffer
// orientation/motion vars
Quaternion q;           // [w, x, y, z]         quaternion container
VectorInt16 aa;         // [x, y, z]            accel sensor measurements
VectorInt16 aaReal;     // [x, y, z]            gravity-free accel sensor measurements
VectorInt16 aaWorld;    // [x, y, z]            world-frame accel sensor measurements
VectorFloat gravity;    // [x, y, z]            gravity vector
float euler[3];         // [psi, theta, phi]    Euler angle container
float ypr[3];           // [yaw, pitch, roll]   yaw/pitch/roll container and gravity vector
// packet structure for InvenSense teapot demo
uint8_t teapotPacket[14] = { '$', 0x02, 0,0, 0,0, 0,0, 0,0, 0x00, 0x00, '\r', '\n' };
String file_name = "/data/acc.csv";
volatile bool mpuInterrupt = false;     // indicates whether MPU interrupt pin has gone high

void dmpDataReady(){
  mpuInterrupt = true;
}

void conectar_wifi() {
  delay(10);
  Serial.println();
  Serial.print("conectando a ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while(WiFi.status()!=WL_CONNECTED){
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("conectado ao AP");
  Serial.println("endereco IP: ");
  Serial.println(WiFi.localIP());
}

void reconectar(){
  while(!mqtt_client.connected()){
    if (WiFi.status() != WL_CONNECTED) {
      conectar_wifi();
    }
    Serial.print("tentando conexao com o ThingsBoard via MQTT...");
    if (mqtt_client.connect("wemos", device_token, NULL)) {
      Serial.println("conectado");
    } 
    else{
      Serial.print("falhou, rc=");
      Serial.print(mqtt_client.state());
      Serial.println(" tentando novamente em 5s");
      delay(5000);
    }
  }
}

void setup(){
  Serial.begin(115200);
  conectar_wifi();
  mqtt_client.setServer(mqtt_server, 1883);
  #if I2CDEV_IMPLEMENTATION == I2CDEV_ARDUINO_WIRE
      Wire.begin(D5, D6);
      Wire.setClock(400000); // 400kHz I2C clock. Comment this line if having compilation difficulties
  #elif I2CDEV_IMPLEMENTATION == I2CDEV_BUILTIN_FASTWIRE
      Fastwire::setup(400, true);
  #endif
  while (!Serial);
  mpu.initialize();
  //pinMode(INTERRUPT_PIN, INPUT);
  // verify connection
  Serial.println(F("Initializing DMP..."));
  devStatus = mpu.dmpInitialize();
  // supply your own gyro offsets here, scaled for min sensitivity
  mpu.setXGyroOffset(220);
  mpu.setYGyroOffset(76);
  mpu.setZGyroOffset(-85);
  mpu.setZAccelOffset(1788); // 1688 factory default for my test chip
  // make sure it worked (returns 0 if so)
  if(devStatus == 0){
      // Calibration Time: generate offsets and calibrate our MPU6050
      mpu.CalibrateAccel(6);
      mpu.CalibrateGyro(6);
      mpu.PrintActiveOffsets();
      // turn on the DMP, now that it's ready
      Serial.println(F("Enabling DMP..."));
      mpu.setDMPEnabled(true);
      Serial.println(F("DMP ready!"));
      dmpReady = true;
      // get expected DMP packet size for later comparison
      packetSize = mpu.dmpGetFIFOPacketSize();
  }
  else{
      // ERROR!
      // 1 = initial memory load failed
      // 2 = DMP configuration updates failed
      // (if it's going to break, usually the code will be 1)
      Serial.print(F("DMP Initialization failed (code "));
      Serial.print(devStatus);
      Serial.println(F(")"));
  }
  timeClient.begin();
  timeClient.setTimeOffset(0);
  timeClient.update();
  //Serial.println(timeClient.getEpochTime());
  //  Serial.println(_time*1000);
  _time = timeClient.getEpochTime();
  //Serial.println(_time, 0);
  _time = _time*1000;
  //Serial.println(_time);
  last_time = millis();
}

void loop(){
  if(!dmpReady) return;
  if(mpu.dmpGetCurrentFIFOPacket(fifoBuffer)){ // Get the Latest packet 
    //Serial.println(_time);
    //Serial.println(_time*1000);
    //Serial.println(last_time, 0);
    _time_mili = millis();
    //Serial.println(_time_mili, 0);
    _time_plus = _time_mili-last_time;
    last_time = _time_mili;
    //Serial.println(_time_plus, 0);
    _time = _time + _time_plus;
    //Serial.println(_time, 0);
    // display initial world-frame acceleration, adjusted to remove gravity
    // and rotated based on known orientation from quaternion
    mpu.dmpGetQuaternion(&q, fifoBuffer);
    mpu.dmpGetAccel(&aa, fifoBuffer);
    mpu.dmpGetGravity(&gravity, &q);
    mpu.dmpGetLinearAccel(&aaReal, &aa, &gravity);
    mpu.dmpGetLinearAccelInWorld(&aaWorld, &aaReal, &q);
    // Serial.println(_time1*1000);
    String payload ="{\"ts\":"+String(_time, 0)+",\"values\":{\"x\":"+String(aaWorld.x)+",\"y\":"+String(aaWorld.y)+",\"z\":"+String(aaWorld.z)+"}}";
    Serial.println(payload);
    char dados_json[100];
    payload.toCharArray(dados_json, 100);
    mqtt_client.publish("v1/devices/me/telemetry", dados_json);
  }
  if(!mqtt_client.connected()){
    reconectar();
  }
  mqtt_client.loop();
}
