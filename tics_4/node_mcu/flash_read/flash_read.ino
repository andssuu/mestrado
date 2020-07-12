#include <FS.h>

String file_name = "/data/acc.txt";

void readFile(String path){
  // Leitura do arquivo 
  File file_acc = SPIFFS.open(path, "r");
  if (!file_acc){
    Serial.println("Failed to open file for reading");
  }
  Serial.println("File Content:");
  while (file_acc.available()){
    Serial.write(file_acc.read());
  }
  file_acc.close();
}

void setup(){
    Serial.begin(115200);
    // initialize device
    //Iniciando sistema de arquivos
    if(SPIFFS.begin()){
      Serial.println("\nSistema de arquivos aberto com sucesso!");
    }
    else{
      Serial.println("\nErro ao abrir o sistema de arquivos");
    }
    //Listagem de arquivos no diretorio /data
//    Dir dir = SPIFFS.openDir("/data");
//    while (dir.next()){
//        Serial.print(dir.fileName());
//        File f = dir.openFile("r");
//        Serial.println(f.size());
//    }
    // Leitura do arquivo
    if(SPIFFS.exists(file_name)){
      Serial.println("Arquivo existe");
      readFile(file_name);
    }
    else{
      Serial.println("Arquivo não existe");
    }
}
void loop(){}
