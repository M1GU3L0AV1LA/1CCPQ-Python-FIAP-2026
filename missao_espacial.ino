#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 4, 5, 6, 7);

#define PIN_NTC A0
#define PIN_LDR A1
#define PIN_LED 8
#define PIN_BUZZER 9

float temperatura;
int luminosidade;
bool alerta;

void setup() {
  Serial.begin(9600);
  pinMode(PIN_LED, OUTPUT);
  pinMode(PIN_BUZZER, OUTPUT);
  lcd.begin(16, 2);
  lcd.print("MISSION CONTROL");
  delay(2000);
  lcd.clear();
}

void loop() {
  // Leitura NTC
  int valorNTC = analogRead(PIN_NTC);
  float tensao = valorNTC * 5.0 / 1023.0;
  temperatura = (tensao - 0.5) * 100.0;

  // Leitura LDR
  luminosidade = analogRead(PIN_LDR);

  // Verifica alertas
  alerta = false;
  if (temperatura > 40 || temperatura < 10) alerta = true;
  if (luminosidade < 100) alerta = true;

  // LCD linha 1
  lcd.setCursor(0, 0);
  lcd.print("T:");
  lcd.print(temperatura, 1);
  lcd.print("C L:");
  lcd.print(luminosidade);

  // LCD linha 2
  lcd.setCursor(0, 1);
  if (alerta) {
    lcd.print("*** ALERTA ***  ");
    digitalWrite(PIN_LED, HIGH);
    tone(PIN_BUZZER, 1000, 200);
  } else {
    lcd.print("Status: NORMAL  ");
    digitalWrite(PIN_LED, LOW);
    noTone(PIN_BUZZER);
  }

  // Monitor Serial
  Serial.print(temperatura);
  Serial.print(" C | Luz: ");
  Serial.print(luminosidade);
  Serial.println(alerta ? " | *** ALERTA ***" : " | NORMAL");

  delay(1000);
}