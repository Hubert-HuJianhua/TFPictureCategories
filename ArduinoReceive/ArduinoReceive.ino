#include <SoftwareSerial.h>

// 定义软件串口的RX和TX引脚
int RX_PIN = 10;  // 将RX_PIN连接到模块的TX
int TX_PIN = 11;  // 将TX_PIN连接到模块的RX

// 初始化软件串口，将其命名为softSerial
SoftwareSerial softSerial(RX_PIN, TX_PIN);

void setup() {
  // 打开硬件串口和软件串口
  Serial.begin(9600);       // 硬件串口
  softSerial.begin(9600);   // 软件串口

  // 打印消息到硬件串口
  Serial.println("软件串口已启动");
}

void loop() {
   if (softSerial.available()) {
    String received = softSerial.readStringUntil('\n');
    Serial.println(received); // Echo the received data
    if(received=="Class 1"){
      Serial.println("OK");
    }
    else if (received=="Class 2")
    {
      Serial.println("No");
    }
    else{
      Serial.println("STOP");
    }
    
  }
}
