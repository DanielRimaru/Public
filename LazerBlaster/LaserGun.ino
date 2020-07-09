#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
RF24 radio(41, 40); // CE, CSN
const byte address[6] = "00001";


#include "SevSeg.h"
SevSeg sevseg; 

//trigger
const int SW_pin = 22; // digital pin connected to switch output
const int X_pin = 0; // analog pin connected to X output
const int Y_pin = 1; // analog pin connected to Y output
const int laser=29;
int mode;
int score;
unsigned long stime;
unsigned long time;
void setup(){
  pinMode(SW_pin, INPUT);
  pinMode(laser, OUTPUT);

  //wifi
  Serial.begin(9600);
  radio.begin();
  radio.openReadingPipe(0, address);
  radio.setPALevel(RF24_PA_MIN);
  radio.startListening();

  //sevseg
  byte numDigits = 4;
  byte digitPins[] = {10, 11, 12, 13};
  byte segmentPins[] = {9, 2, 3, 5, 6, 8, 7, 4};
  bool resistorsOnSegments = true; 
  bool updateWithDelaysIn = true;
  byte hardwareConfig = COMMON_CATHODE; 
  sevseg.begin(hardwareConfig, numDigits, digitPins, segmentPins, resistorsOnSegments);
  sevseg.setBrightness(90);
  mode=0;
}
int rawconvert(char raw[12])
{
  int score=0;
  int k=1;
  for(int i=11;i>=0;i--)
  {
    if(raw[i]=='1')
      score+=k;
    k*=2;
  }
  return score;
}
int getscore(char scoreraw[12]){

  if (radio.available()) {
    char scoreraw[12]="";
    radio.read(&scoreraw, sizeof(scoreraw));
    Serial.write(scoreraw);
    int score = rawconvert(scoreraw);
    return score;
  }
  
}
void loop(){
    time = millis();
    if(time-stime>=10000 && mode==2)
    {
      stime=time;
      mode=0;
    }else
    if(time-stime>=60000 && mode==1)
    {
      stime=time;
      mode=2;
      char scoreraw[12]="";
      score = getscore(scoreraw[12]);
      
    }

  
    digitalWrite(laser, LOW);
    if(analogRead(X_pin)>=600 && (mode==1||mode==0))
    {
      digitalWrite(laser, HIGH);
      if(mode!=1)
        stime=time;
      mode=1;
    }
    if(mode==2)
    {
      sevseg.setNumber(int(score), 0);
      sevseg.refreshDisplay();
    }
    sevseg.blank();
}
