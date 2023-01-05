const float Vcc= 5;                  //Tension aux bornes de l'arduino en Volt
const float R=47000;                      //Résistance de la 2eme résistance en Ohm
const float NBNum=1023.0;            //Valeur numérique la plus grande

//Capteur X1
int X1 ;
float X1_Res;
int angleX1=90;
const float flatX1 = 27700 // resitance fablab
;                 //Résistance du flex sensor à plat
const float bentX1 = 49000;                   //Résistance du flex sensor à 90 degré

//Capteur X2
int X2 ;
float X2_Res;
int angleX2;
const float flatX2=24300 // resitance fablab
;                 //Résistance du flex sensor à plat
const float bentX2=58000;                   //Résistance du flex sensor à 90 degré

//Capteur Y2
int Y2 ;
float Y2_Res;
int angleY2;
const float flatY2= 54000 // resitance fablab
;                 //Résistance du flex sensor à plat
const float bentY2=126000;                   //Résistance du flex sensor à 90 degré

//Capteur X3
int X3 ;
float X3_Res;
int angleX3=90;
const float flatX3 // resitance fablab
;                 //Résistance du flex sensor à plat
const float bentX3;                   //Résistance du flex sensor à 90 degré

//Capteur Y3
int Y3 ;
float Y3_Res;
int angleY3=90;
const float flatY3// resitance fablab
;                 //Résistance du flex sensor à plat
const float bentY3;                   //Résistance du flex sensor à 90 degré

//Capteur X4
int X4;
float X4_Res;
int angleX4=90;
const float flatX4 // resitance fablab
;                 //Résistance du flex sensor à plat
const float bentX4;                   //Résistance du flex sensor à 90 degré

//Capteur Y4
int Y4 ;
float Y4_Res;
int angleY4=90;
const float flatY4 // resitance fablab
;                 //Résistance du flex sensor à plat
const float bentY4;                   //Résistance du flex sensor à 90 degré

//Capteur X5
int X5 ;
float X5_Res;
int angleX5=90;
const float flatX5 // resitance fablab
;                 //Résistance du flex sensor à plat
const float bentX5;                   //Résistance du flex sensor à 90 degré

void setup()
{
/* Configuration hardware de l'arduino*/  
  //Débit de communication
  Serial.begin(9600);

  //Configuration des broches
  pinMode(A6,INPUT);        //capteur X1
  pinMode(A5,INPUT);
 
}


float Num_to_Analog(int Num)
{
/*Prends une valeur numérique entre 0 et 1023 et renvoie la tension correspondante*/

  //Calcul de la tension en volt en faisant une conversion Numérique-Analogique
  float Vflex=Num*(Vcc / 1023.0);

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
  X1=analogRead(A6);
 

  //Calculs des résistances correspondantes
  X1_Res=Num_to_Analog(X1); // resistance du capteur flex en ohm
  Y2_Res=Num_to_Analog(Y2);
 

  //Calculs des valeurs des angles
  //Renvoie des valeurs par l'Arduino au port correspondant
            //capteur X1
            //Serial.println("valeur resistance capteur vaut en ohms");
            Serial.println(X1_Res);
            //Serial.println("angle vaut ");
            //  Serial.println(angleX1);
            //Serial.println(9999);
            //SerialReturn(1100,angleX1);
            /*SerialReturn(2100,angleX2);
            SerialReturn(2200,angleY2);
            SerialReturn(3100,angleX3);
            SerialReturn(3200,angleY3);
            SerialReturn(4100,angleX4);
            SerialReturn(4200,angleY4);
            SerialReturn(5100,angleX5);*/
            
  
  delay(100);
}
