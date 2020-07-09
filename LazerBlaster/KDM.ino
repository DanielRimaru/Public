const int sensor[3]={22,23,24};
int seq[]={1,2,1,0,2,1,2,0,1,2,0,1,2,0,1,0,2,1,0,2,1,2,1,0,2,1,1,2,1,2,0,1,2,0,1,0,2,0,1,2,0,2,0,1,2,1,2,1,0,1,0,2,0,2,1,2,1,0,2,1,0,2,1,0,2,1,0,2,0,1,2,0,2,1,2,0,1};
#include <Servo.h>
int k;
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
Servo myservo[4];
int pos=0;
RF24 radio(41, 40); // CE, CSN
const byte address[6] = "00001";
bool hit;
int mode=0;
unsigned long cd;
unsigned long stime;
unsigned long time;
int points;
void setup() {

  for (int i=0;i<=2;i++)
  {
    pinMode(sensor[i],INPUT);
    pinMode(sensor[i]+8,OUTPUT);
  }
  Serial.begin(9600);
  cd=0;
  mode=0;
  radio.begin();
  radio.openWritingPipe(address);
  radio.setPALevel(RF24_PA_MIN);
  radio.stopListening();
  hit=false;
  points;
}

void loop() {
  time=millis();
  if(mode==0)
  {
    points=0;
    if(digitalRead(sensor[0]) || digitalRead(sensor[1]) || digitalRead(sensor[2]))
    {
     Serial.write("Start \n");
     for (int i=0;i<=3;i++)
        myservo[i].attach(9+i);
     k=0;
     if(seq[k]==0)
        Serial.write("Blue!!\n");
     else
     if(seq[k]==1)
        Serial.write("Green!!\n");
     if(seq[k]==2)
        Serial.write("Yellow!!\n");
     digitalWrite(sensor[seq[k]]+8,HIGH);
     mode=1;
     stime=time;
    }
  }
  else
  
  if(mode==1)
  {
     if(seq[k]==0)
        Serial.write("Blue!!\n");
     if(seq[k]==1)
        Serial.write("Green!!\n");
     if(seq[k]==2)
        Serial.write("Yellow!!\n");
  if(digitalRead(sensor[0]) && seq[k]==0)
  {
    Serial.write("Blue!!\n");
    points+=25;
    k++;
    digitalWrite(sensor[0]+8,LOW);
    digitalWrite(sensor[seq[k]]+8,HIGH);
  }
  if (digitalRead(sensor[1]) && seq[k]==1)
    {
    Serial.write("Green!!\n");
    points+=25;
    k++;
    digitalWrite(sensor[1]+8,LOW);
    digitalWrite(sensor[seq[k]]+8,HIGH);
  }
  if (digitalRead(sensor[2])&& seq[k]==2)
    {
    Serial.write("Yellow!!\n");
    points+=25;
    k++;
    digitalWrite(sensor[2]+8,LOW);
    digitalWrite(sensor[seq[k]]+8,HIGH);
    }
  }
  if(mode==1)
  {
    if(pos==360)
      pos=180; 
    for (int i=0;i<=3;i++)
      if(i<=1)
        myservo[i].write(pos);
      else
        myservo[i].write(-pos);
       
    pos+=90;
  }
  if(mode==1&&time-stime>=58000)
  {
    mode=2;
    stime=time;
  }
  if(mode==2)
  {
    char text[11]="000000000000";
    int a=0;
    while(points>0)
    {
      if(points%2==1)
        text[11-a]='1';
      else
        text[11-a]='0';
      points=points/2;
      a++;
    }

    Serial.write(text);
    Serial.write(strlen(text));
    radio.write(&text,12);
    
    
    for (int i=0;i<=3;i++)
    {    
      digitalWrite(sensor[i]+8,LOW);
      myservo[i].detach();
    }
    
  }
  if(mode==2&&time-stime>=10000)
    mode=0;
  k=k%70;
}
