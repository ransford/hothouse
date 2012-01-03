# Hothouse

Tools to measure, plot, and emit complaints based on temperature.

# Prerequisites

For the Arduino end, these Arduino libraries:
* [OneWire](http://www.pjrc.com/teensy/td_libs_OneWire.html)
* [Dallas Temperature Control](http://milesburton.com/Dallas_Temperature_Control_Library)

For the computer end,
* The [pyserial](http://pyserial.sourceforge.net/) Python module for
  serial-port access

# "Schematic"

Connect Pin 1 of DS18B20 to ground;
Connect Pin 2 to +5V with a 4.7kΩ resistor and to Arduino Pin 2 with a wire.
Connect Pin 3 to ground.
