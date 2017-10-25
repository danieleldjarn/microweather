/*****************************************************************
  MicroWeather station

  A little weather app for my MicroView.
  Gets weather information form internet and displays on screen.
*****************************************************************/
#include <MicroView.h>



void setup() {
  // put your setup code here, to run once:
  uView.begin();
  uView.clear(PAGE);
}

void loop() {
  // put your main code here, to run repeatedly:
  uView.setCursor(10, 10);
  uView.print("Temp [C]");
  uView.display();
}
