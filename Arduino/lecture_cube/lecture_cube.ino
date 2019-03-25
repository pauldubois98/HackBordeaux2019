float a0 = 0;
float a1 = 0;
float a2 = 0;
float a3 = 0;
float a4 = 0;
float a5 = 0;
float a6 = 0;
float a7 = 0;

float r0 = 0;
float r1 = 0;
float r2 = 0;
float r3 = 0;
float r4 = 0;
float r5 = 0;
float r6 = 0;
float r7 = 0;

float rref0 = 22000 ;
float rref1 = 22000 ;
float rref2 = 33000 ;
float rref3 = 33000 ;



void setup() {
  Serial.begin(9600);
  Serial.println("");
}

void loop() {

  
  
  a0 = analogRead(A0);
  a0 = a0*5/1024;
  r0 = (rref0*a0)/(5-a0);
  
 
  a1 = analogRead(A1);
  a1 = a1*5/1024;
  r1 = (rref0*a1)/(5-a1);
  
  a2 = analogRead(A2);
  a2 = a2*5/1024;
  r2 = (rref1*a2)/(5-a2);
  
  a3 = analogRead(A3);
  a3 = a3*5/1024;
  r3 = (rref1*a3)/(5-a3);
  
  a4 = analogRead(A4);
  a4 = a4*5/1024;
  r4 = (rref2*a4)/(5-a4);
  
  a5 = analogRead(A5);
  a5 = a5*5/1024;
  r5 = (rref2*a5)/(5-a5);
  
  a6 = analogRead(A6);
  a6 = a6*5/1024;
  r6 = (rref3*a6)/(5-a6);
  
  a7 = analogRead(A7);
  a7 = a7*5/1024;
  r7 = (rref3*a7)/(5-a7);

if ((Serial.available()>1)){
  
  if (Serial.read() == 'r') {
    
  Serial.print("[");
  Serial.print(r0);
  Serial.print(",");
  Serial.print(r1);
  Serial.print(",");
  Serial.print(r2);
  Serial.print(",");
  Serial.print(r3);
  Serial.print(",");
  Serial.print(r4);
  Serial.print(",");
  Serial.print(r5);
  Serial.print(",");
  Serial.print(r6);
  Serial.print(",");
  Serial.print(r7);
  Serial.println("]"); 
  }

  }

  

}

 
    


