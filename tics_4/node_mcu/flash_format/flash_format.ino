#include <FS.h>

void setup(){
  Serial.begin(115200);
  //Iniciando sistema de arquivos
  if(SPIFFS.begin()){
    Serial.println("\nSistema de arquivos aberto com sucesso!");
  }
  else{
    Serial.println("\nErro ao abrir o sistema de arquivos");
  }
  Serial.println("Formatando Flash...");
  //Formatacao da flash
  if(SPIFFS.format()){
    Serial.println("Flash formatada!");
  }
  else{
   Serial.println("Erro!");
  }
}
void loop(){}
