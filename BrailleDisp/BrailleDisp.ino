#include "LedControl.h"
#include "binary.h"

/*
 DIN connects to pin 12
 CLK connects to pin 11
 CS connects to pin 10 
*/
String data;
LedControl lc=LedControl(12,11,10,1);

// delay time between faces
unsigned long delaytime=500;

void setup() 
{ 
  Serial.begin(9600); 
  pinMode(LED_BUILTIN, OUTPUT); 
  digitalWrite (LED_BUILTIN, LOW); //initially set to low
  Serial.println("This is my First Example.");
  lc.shutdown(0,false);
  // Set brightness to a medium value
  lc.setIntensity(0,8);
  // Clear the display
  lc.clearDisplay(0);  
}

void cleardisp()
{
  lc.setRow(0,0,B00000000);
  lc.setRow(0,1,B00000000);
  lc.setRow(0,2,B00000000);
  lc.setRow(0,3,B00000000);
  lc.setRow(0,4,B00000000);
  lc.setRow(0,5,B00000000);
  lc.setRow(0,6,B00000000);
  lc.setRow(0,7,B00000000);
}
void alpha(char x)
{
  if(x==' ')
  {
    lc.setRow(0,0,B00000000);
    lc.setRow(0,1,B00000000);
    lc.setRow(0,2,B00000000);
    delay(delaytime);
    cleardisp();
  }
  if(x=='a')
  {
    lc.setRow(0,0,B10000000);
    delay(delaytime);
    cleardisp();
  }
  if(x=='b')
  {
    lc.setRow(0,0,B10000000);
    lc.setRow(0,1,B10000000);
    delay(delaytime);
    cleardisp();
  }
  if(x=='c')
  {
    lc.setRow(0,0,B11000000);
    delay(delaytime);
    cleardisp();
  }
  if(x=='d')
  {
    lc.setRow(0,0,B11000000);
    lc.setRow(0,1,B01000000);
    delay(delaytime);
    cleardisp();
  }
  if(x=='e')
  {
    lc.setRow(0,0,B10000000);
    lc.setRow(0,1,B01000000);
    delay(delaytime);
    cleardisp();
  }
  if(x=='f')
  {
    lc.setRow(0,0,B11000000);
    lc.setRow(0,1,B10000000);
    delay(delaytime);
    cleardisp();
  }
  if(x=='g')
  {
    lc.setRow(0,0,B11000000);
    lc.setRow(0,1,B11000000);
    delay(delaytime);
    cleardisp();
  }
  if(x=='h')
  {
    lc.setRow(0,0,B10000000);
    lc.setRow(0,1,B11000000);
    delay(delaytime);
    cleardisp();
  }
  if(x=='i')
  {
    lc.setRow(0,0,B01000000);
    lc.setRow(0,1,B10000000);
    delay(delaytime);
    cleardisp();
  }
  if(x=='j')
  {
    lc.setRow(0,0,B01000000);
    lc.setRow(0,1,B11000000);
    delay(delaytime);
    cleardisp();
  }
  if(x=='k')
  {
    lc.setRow(0,0,B10000000);
    lc.setRow(0,2,B10000000);
    delay(delaytime);
    cleardisp();
  }
  if(x=='l')
  {
    lc.setRow(0,0,B10000000);
    lc.setRow(0,1,B10000000);
    lc.setRow(0,2,B10000000);
    delay(delaytime);
    cleardisp();
  }
  if(x=='m')
  {
    lc.setRow(0,0,B11000000);
    lc.setRow(0,2,B10000000);
    delay(delaytime);
    cleardisp();
  }
  if(x=='n')
  {
    lc.setRow(0,0,B11000000);
    lc.setRow(0,1,B01000000);
    lc.setRow(0,2,B10000000);
    delay(delaytime);
    cleardisp();
  }
  if(x=='o')
  {
    lc.setRow(0,0,B10000000);
    lc.setRow(0,1,B01000000);
    lc.setRow(0,2,B10000000);
    delay(delaytime);
    cleardisp();
  }
  if(x=='p')
  {
    lc.setRow(0,0,B11000000);
    lc.setRow(0,1,B10000000);
    lc.setRow(0,2,B10000000);
    delay(delaytime);
    cleardisp();
  }
  if(x=='q')
  {
    lc.setRow(0,0,B11000000);
    lc.setRow(0,1,B11000000);
    lc.setRow(0,2,B10000000);
    delay(delaytime);
    cleardisp();
  }
  if(x=='r')
  {
    lc.setRow(0,0,B10000000);
    lc.setRow(0,1,B11000000);
    lc.setRow(0,2,B10000000);
    delay(delaytime);
    cleardisp();
  }
  if(x=='s')
  {
    lc.setRow(0,0,B01000000);
    lc.setRow(0,1,B10000000);
    lc.setRow(0,2,B10000000);
    delay(delaytime);
    cleardisp();
  }
  if(x=='t')
  {
    lc.setRow(0,0,B01000000);
    lc.setRow(0,1,B11000000);
    lc.setRow(0,2,B10000000);
    delay(delaytime);
    cleardisp();
  }
  if(x=='u')
  {
    lc.setRow(0,0,B10000000);
    lc.setRow(0,1,B00000000);
    lc.setRow(0,2,B11000000);
    delay(delaytime);
    cleardisp();
  }
  if(x=='v')
  {
    lc.setRow(0,0,B10000000);
    lc.setRow(0,1,B10000000);
    lc.setRow(0,2,B11000000);
    delay(delaytime);
    cleardisp();
  }
  if(x=='w')
  {
    lc.setRow(0,0,B01000000);
    lc.setRow(0,1,B11000000);
    lc.setRow(0,2,B01000000);
    delay(delaytime);
    cleardisp();
  }
  if(x=='x')
  {
    lc.setRow(0,0,B11000000);
    lc.setRow(0,1,B00000000);
    lc.setRow(0,2,B11000000);
    delay(delaytime);
    cleardisp();
  }
  if(x=='y')
  {
    lc.setRow(0,0,B11000000);
    lc.setRow(0,1,B01000000);
    lc.setRow(0,2,B11000000);
    delay(delaytime);
    cleardisp();
  }
  if(x=='z')
  {
    lc.setRow(0,0,B10000000);
    lc.setRow(0,1,B01000000);
    lc.setRow(0,2,B11000000);
    delay(delaytime);
    cleardisp();
  }
}
 
void loop() 
{
  while (Serial.available())
  {
    data = Serial.readString();
    //Serial.print(data);
  }
  for(int i=0;i<data.length();++i)
  alpha(data.charAt(i));

}
