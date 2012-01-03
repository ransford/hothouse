#include <OneWire.h>
#include <DallasTemperature.h>

// Data wire is plugged into port 2 on the Arduino
#define ONE_WIRE_BUS 2

/* Setup a oneWire instance to communicate with any OneWire devices (not just
   Maxim/Dallas temperature ICs) */
OneWire oneWire(ONE_WIRE_BUS);

// Pass our oneWire reference to Dallas Temperature.
DallasTemperature sensors(&oneWire);

void setup(void)
{
  // start serial port
  Serial.begin(9600);

  // Start up the library
  sensors.begin();
  sensors.setResolution(12);

  pinMode(13, OUTPUT); // LED on Uno pin 13
}

void loop(void)
{
  // call sensors.requestTemperatures() to issue a global temperature
  // request to all devices on the bus
  digitalWrite(13, HIGH);
  sensors.requestTemperatures(); // Send the command to get temperatures
  digitalWrite(13, LOW);

  Serial.println(sensors.getTempFByIndex(0));

  delay(5000);
}

