
//----------------Variables globales-------------------//
const float Vcc= 5;                  //Tension aux bornes de l'arduino en Volt
const float R=47000;                      //Résistance de la 2eme résistance en Ohm
const float NBNum=1023.0;            //Valeur numérique la plus grande

//Capteur X1 (Capteur 4)
int X1 =0;
float X1_Res=0;
int angleX1=0;
const float flatX1=29800;                 //Résistance du flex sensor à plat
const float bentX1=44400;                   //Résistance du flex sensor à 90 degré

//Capteur X2 (Capteur 19)
int X2=0 ;
float X2_Res=0;
int angleX2=0;
const float flatX2=32300;                 //Résistance du flex sensor à plat
const float bentX2=40700;                   //Résistance du flex sensor à 90 degré

//Capteur Y2 (Capteur 1)
int Y2=0 ;
float Y2_Res=0;
int angleY2=0;
const float flatY2=33600;                 //Résistance du flex sensor à plat
const float bentY2=48200;                   //Résistance du flex sensor à 90 degré

//Capteur X3 ( Capteur 11)
int X3=0 ;
float X3_Res=0;
int angleX3=0;
const float flatX3=30500;                 //Résistance du flex sensor à plat
const float bentX3=35500;                   //Résistance du flex sensor à 90 degré

//Capteur Y3 ( Capteur 21)
int Y3=0;
float Y3_Res=0;
int angleY3=0;
const float flatY3=27600;                 //Résistance du flex sensor à plat
const float bentY3=45200;                   //Résistance du flex sensor à 90 degré

//Capteur X4 ( Capteur 34)
int X4=0 ;
float X4_Res=0;
int angleX4=0;
const float flatX4=27500;                 //Résistance du flex sensor à plat
const float bentX4=35300;                   //Résistance du flex sensor à 90 degré

//Capteur Y4 ( Capteur 24)
int Y4=0;
float Y4_Res=0;
int angleY4=0;
const float flatY4=30000;                 //Résistance du flex sensor à plat
const float bentY4=49000;                   //Résistance du flex sensor à 90 degré

//Capteur X5 ( Capteur 42)
int X5=0 ;
float X5_Res=0;
int angleX5=0;
const float flatX5=24300;                 //Résistance du flex sensor à plat
const float bentX5=37000;                   //Résistance du flex sensor à 90 degré

void setup()
{
/* Configuration hardware de l'arduino*/  
  //Débit de communication
  Serial.begin(9600);

  //Configuration des broches
  pinMode(A0,INPUT);        //capteur X1
  pinMode(A2,INPUT);        //capteur X2 A2
  pinMode(A4,INPUT);        //capteur Y2 A4
  pinMode(A6,INPUT);        //capteur X3 A6
  pinMode(A7,INPUT);        //capteur Y3 A8
  pinMode(A8,INPUT); //capteur X4 A7
  pinMode(A10,INPUT);        //capteur Y4 A10
  pinMode(A12,INPUT);        //capteur X5 A13
  //pinMode(A15,INPUT);        //capteur X5 A15
}


float Num_to_Analog(int Num)
{
/*Prends une valeur numérique entre 0 et 1023 et renvoie la tension correspondante */

  //Calcul de la tension en faisant une conversion Numérique-Analogique
  float Vflex=Num*(Vcc / NBNum);

  //Calcul de la résistance du Flex sensor en utilisant le pont diviseur
  float Rflex=R*(Vcc / Vflex -1.0);

  return Rflex;
}

void SerialReturn(int ID,int angle)
{
/*Renvoie l'ID du capteur et la valeur de l'angle au port de l'ordinateur*/
  Serial.println(ID);
  Serial.println(angle);
}



void loop() 
{
/* Renvoie la valeur de l'angle pour chaque capteur*/

  //Lectures des valeurs Numériques reçues via les ports Analogiques
  X1=analogRead(A0);
  X2=analogRead(A2);
  Y2=analogRead(A4);
  X3=analogRead(A6);
  Y3=analogRead(A8);
  X4=analogRead(A10);
  Y4=analogRead(A12);
  X5=analogRead(A14);

  //Calculs des résistances correspondantes
  X1_Res=Num_to_Analog(X1);
  X2_Res=Num_to_Analog(X2);
  Y2_Res=Num_to_Analog(Y2);
  X3_Res=Num_to_Analog(X3);
  Y3_Res=Num_to_Analog(Y3);
  X4_Res=Num_to_Analog(X4);
  Y4_Res=Num_to_Analog(Y4);
  X5_Res=Num_to_Analog(X5);

  //Calculs des valeurs des angles
  angleX1=(int)map(X1_Res,flatX1,bentX1,0,90.0);
  angleX2=(int)map(X2_Res,flatX2,bentX2,0,90.0);
  angleY2=(int)map(Y2_Res,flatY2,bentY2,0,90.0);
  angleX3=(int)map(X3_Res,flatX3,bentX3,0,90.0);
  angleY3=(int)map(Y3_Res,flatY3,bentY3,0,90.0);
  angleX4=(int)map(X4_Res,flatX4,bentX4,0,90.0);
  angleY4=(int)map(Y4_Res,flatY4,bentY4,0,90.0);
  angleX5=(int)map(X5_Res,flatX5,bentX5,0,90.0);

  //Renvoie des valeurs par l'Arduino au port correspondant
  Serial.println(9999);
  if(angleX1 < 150 && angleX1 > 0)
    SerialReturn(1100,angleX1);             //capteur X1
  else if(angleX1 >= 150)
    SerialReturn(1100,150);
  else if(angleX1 <= 0)
    SerialReturn(1100,0);

  if(angleX2 < 150 && angleX2 > -5) 
    SerialReturn(2100,angleX2);             //capteur X2
  else if(angleX2 >= 150) 
    SerialReturn(2100,150);
  else if(angleX2 <= -5) 
    SerialReturn(2100,-5);

  if(angleY2 < 150 && angleY2 > 0) 
    SerialReturn(2200,angleY2);             //capteur Y2
  else if(angleY2 >= 150) 
    SerialReturn(2200,150); 
  else if(angleY2 <= 0) 
    SerialReturn(2200,0); 

  if(angleX3 < 150 && angleX3 > -5) 
    SerialReturn(3100,angleX3);             //capteur X3
  else if(angleX3 >= 150) 
    SerialReturn(3100,150); 
  else if(angleX3 <= -5) 
    SerialReturn(3100,-5); 
  
  if(angleY3 < 150 && angleY3 > 0) 
    SerialReturn(3200,angleY3);             //capteur Y3
  else if(angleY3 >= 150) 
    SerialReturn(3200,150); 
  else if(angleY3 <= 0) 
    SerialReturn(3200,0); 

  if(angleX4 < 150 && angleX4 > -5) 
    SerialReturn(4100,angleX4);             //capteur X4
  else if(angleX4 >= 150) 
    SerialReturn(4100,150); 
  else if( angleX4 <= -5) 
    SerialReturn(4100,-5); 

  if(angleY4 < 150 && angleY4 > 0) 
    SerialReturn(4200,angleY4);             //capteur Y4
  else if(angleY4 >= 150) 
    SerialReturn(4200,150);
  else if(angleY4 <= 0) 
    SerialReturn(4200,0);

  if(angleX5 < 150 && angleX5 > -5) 
    SerialReturn(5100,angleX5);             //capteur X5
  else if(angleX5 >= 150) 
    SerialReturn(5100,150);   
  else if(angleX5 <= -5) 
    SerialReturn(5100,-5);   
  delay(2000);
}

 
