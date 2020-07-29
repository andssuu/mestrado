#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <TimeAlarms.h>

/* ssid e password do AP ao qual se deseja conectar */
const char* ssid = "";
const char* password = "";
/* endereco do servidor onde está instalado o ThingsBoard
// const char* mqtt_server = "192.168.X.XXX";
/* ou para o ThingsBoard live demo */
const char* mqtt_server = "demo.thingsboard.io";
/* credenciais para o device que se deseja conectar */
//const char* device_token = "3KD8jT0vc2qrCB16jm07";
//const char* device_token = "qc53IaxGMtoFYpEHdPuf";
const char* device_token = "4wrqbDY22AVUqBvZRnd0"; //ACC
/* instancia o cliente Wi-Fi */
WiFiClient wifi_client;
/* instancia o cliente MQTT */
PubSubClient mqtt_client(wifi_client);

// --------------- ACC BEGBIN --------------- 
#include "I2Cdev.h"
#include <FS.h>
#include "MPU6050_6Axis_MotionApps20.h"
#if I2CDEV_IMPLEMENTATION == I2CDEV_ARDUINO_WIRE
    #include "Wire.h"
#endif
MPU6050 mpu;
// uncomment "OUTPUT_READABLE_QUATERNION" if you want to see the actual
// quaternion components in a [w, x, y, z] format (not best for parsing
// on a remote host such as Processing or something though)
//#define OUTPUT_READABLE_QUATERNION

// uncomment "OUTPUT_READABLE_EULER" if you want to see Euler angles
// (in degrees) calculated from the quaternions coming from the FIFO.
// Note that Euler angles suffer from gimbal lock (for more info, see
// http://en.wikipedia.org/wiki/Gimbal_lock)
// #define OUTPUT_READABLE_EULER

// uncomment "OUTPUT_READABLE_YAWPITCHROLL" if you want to see the yaw/
// pitch/roll angles (in degrees) calculated from the quaternions coming
// from the FIFO. Note this also requires gravity vector calculations.
// Also note that yaw/pitch/roll angles suffer from gimbal lock (for
// more info, see: http://en.wikipedia.org/wiki/Gimbal_lock)
// #define OUTPUT_READABLE_YAWPITCHROLL

// uncomment "OUTPUT_READABLE_REALACCEL" if you want to see acceleration
// components with gravity removed. This acceleration reference frame is
// not compensated for orientation, so +X is always +X according to the
// sensor, just without the effects of gravity. If you want acceleration
// compensated for orientation, us OUTPUT_READABLE_WORLDACCEL instead.
// #define OUTPUT_READABLE_REALACCEL

// uncomment "OUTPUT_READABLE_WORLDACCEL" if you want to see acceleration
// components with gravity removed and adjusted for the world frame of
// reference (yaw is relative to initial orientation, since no magnetometer
// is present in this case). Could be quite handy in some cases.
#define OUTPUT_READABLE_WORLDACCEL

// uncomment "OUTPUT_TEAPOT" if you want output that matches the
// format used for the InvenSense teapot demo
//#define OUTPUT_TEAPOT

#define INTERRUPT_PIN 2  // use pin 2 on Arduino Uno & most boards
#define LED_PIN 13 // (Arduino is 13, Teensy is 11, Teensy++ is 6)
bool blinkState = false;
// MPU control/status vars
bool dmpReady = false;  // set true if DMP init was successful
uint8_t mpuIntStatus;   // holds actual interrupt status byte from MPU
uint8_t devStatus;      // return status after each device operation (0 = success, !0 = error)
uint16_t packetSize;    // expected DMP packet size (default is 42 bytes)
uint16_t fifoCount;     // count of all bytes currently in FIFO
uint8_t fifoBuffer[64]; // FIFO storage buffer
VectorInt16 fifoBufferAcc[15];

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

void writeFile(VectorInt16 acc, String path){
  //Adiciona conteúdo ao arquivo
  File rFile = SPIFFS.open(path, "a"); 
  if(!rFile){
    Serial.println("Erro ao abrir arquivo!");
  } else {
    rFile.println(String(acc.x)+";"+String(acc.y)+";"+String(acc.z));
    //Serial.print("gravou estado: ");
    //Serial.println(String(acc.x)+";"+String(acc.y)+";"+String(acc.z));
  }
  rFile.close();
}
// --------------- ACC END --------------- 

void conectar_wifi() {
  delay(10);
  Serial.println();
  Serial.print("conectando a ");
  Serial.println(ssid);
  /* tenta iniciar a conexao com a rede Wi-Fi */
  WiFi.begin(ssid, password);
  /* verifica o status e aguarda a conexao */
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  /* imprime na serial IP da conexao Wi-Fi */
  Serial.println("");
  Serial.println("conectado ao AP");
  Serial.println("endereco IP: ");
  Serial.println(WiFi.localIP());
}

void reconectar() {
  /* loop ate que esteja reconectado com o broker MQTT */
  while (!mqtt_client.connected()) {
    /* verifica a conexao Wi-Fi */
    if (WiFi.status() != WL_CONNECTED) {
      /* reconecta com o Wi-Fi */
      conectar_wifi();
    }
    Serial.print("tentando conexao com o ThingsBoard via MQTT...");
    /* tentativa de conexao */
    if (mqtt_client.connect("wemos", device_token, NULL)) {
      Serial.println("conectado");
    } 
    else {
      Serial.print("falhou, rc=");
      Serial.print(mqtt_client.state());
      Serial.println(" tentando novamente em 5s");
      /* tenta novamente daqui a 5s */
      delay(5000);
    }
  }
}

void coletar_e_enviar_dados(){
  Serial.print("\n Coletando dados da acc: ");
  // if programming failed, don't try to do anything
  //Serial.print(mpu.dmpGetCurrentFIFOPacket(fifoBuffer));
    /* converte os dados lidos para String */
    String acc_x = String(aaWorld.x);
    String acc_y = String(aaWorld.y);
    String acc_z = String(aaWorld.z);
    /* cria o payload da mensagem MQTT no formato JSON */
    String payload = "{";
    payload += "\"acc_x\":"; payload += acc_x; payload += ",";
    payload += "\"acc_y\":"; payload += acc_y; payload += ",";
    payload += "\"acc_z\":"; payload += acc_z;
    payload += "}";
    /* converte os dados em formato JSON de String para char[] */
    char dados_json[100];
    payload.toCharArray(dados_json, 100);
    /* envia o pacote MQTT com os dados dos sensores */
    mqtt_client.publish( "v1/devices/me/telemetry", dados_json);
}

// ================================================================
// ===                      INITIAL SETUP                       ===
// ================================================================

void setup(){
  /* configura a interface serial */
  Serial.begin(115200);
  /* conectar a rede Wi-Fi */
  conectar_wifi();
  /* conectar ao broker MQTT */
  mqtt_client.setServer(mqtt_server, 1883);
  /* programa um evento de tempo a cada 10s para enviar os dados dos sensores */
  //Alarm.timerRepeat(5, coletar_e_enviar_dados);
  // join I2C bus (I2Cdev library doesn't do this automatically)
  #if I2CDEV_IMPLEMENTATION == I2CDEV_ARDUINO_WIRE
      Wire.begin(D5, D6);
      Wire.setClock(400000); // 400kHz I2C clock. Comment this line if having compilation difficulties
  #elif I2CDEV_IMPLEMENTATION == I2CDEV_BUILTIN_FASTWIRE
      Fastwire::setup(400, true);
  #endif
  while (!Serial);
  Serial.println(F("Initializing I2C devices..."));
  mpu.initialize();
  pinMode(INTERRUPT_PIN, INPUT);
  // verify connection
  Serial.println(F("Testing device connections..."));
  Serial.println(mpu.testConnection() ? F("MPU6050 connection successful") : F("MPU6050 connection failed"));
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
      Serial.println(F("DMP ready! Waiting for first interrupt..."));
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
  //Tratamento de Arquivos
  //Iniciando sistema de arquivos
  if(SPIFFS.begin()){
    Serial.println("\nSistema de arquivos aberto com sucesso!");
  }
  else{
    Serial.println("\nErro ao abrir o sistema de arquivos");
  }  
}

// ================================================================
// ===                    MAIN PROGRAM LOOP                     ===
// ================================================================

void loop(){
  if(!dmpReady) return;
  // read a packet from FIFO
  if(mpu.dmpGetCurrentFIFOPacket(fifoBuffer)){ // Get the Latest packet 
    #ifdef OUTPUT_READABLE_WORLDACCEL
      // display initial world-frame acceleration, adjusted to remove gravity
      // and rotated based on known orientation from quaternion
      mpu.dmpGetQuaternion(&q, fifoBuffer);
      mpu.dmpGetAccel(&aa, fifoBuffer);
      mpu.dmpGetGravity(&gravity, &q);
      mpu.dmpGetLinearAccel(&aaReal, &aa, &gravity);
      mpu.dmpGetLinearAccelInWorld(&aaWorld, &aaReal, &q);
      Serial.print("aworld x:\t");
      Serial.print(aaWorld.x);
      Serial.print("\t y: ");
      Serial.print(aaWorld.y);
      Serial.print("\t z: ");
      Serial.println(aaWorld.z);
      //writeFile(aaWorld, file_name);
      String acc_x = String(aaWorld.x);
      String acc_y = String(aaWorld.y);
      String acc_z = String(aaWorld.z);
      /* cria o payload da mensagem MQTT no formato JSON */
      String payload = "{";
      payload += "\"acc_x\":"; payload += acc_x; payload += ",";
      payload += "\"acc_y\":"; payload += acc_y; payload += ",";
      payload += "\"acc_z\":"; payload += acc_z;
      payload += "}";
      /* converte os dados em formato JSON de String para char[] */
      char dados_json[100];
      payload.toCharArray(dados_json, 100);
      /* envia o pacote MQTT com os dados dos sensores */
      mqtt_client.publish( "v1/devices/me/telemetry", dados_json);
    #endif
  }
  /* verifica status da conexao */
  if(!mqtt_client.connected()){
    reconectar();
  }
  /* executa a funcao de loop da biblioteca TimeAlarm */
  Alarm.delay(100);
  /* executa a funcao de loop do cliente MQTT */
  mqtt_client.loop();
}
