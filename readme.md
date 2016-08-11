# CHIP Binary clock
This code is used in combinations with the CHIP computer by NTC and some extra hardware to create a physical binary clock. It takes current time, turn it into three binary arrays for hours,  minutes and seconds, and activates diferent CHIP LCD outputs.

Feel free to recommend and extend this project. Created and mantained by Gonzalo Cao Cabeza de Vaca. Please send any feedback or comments to gonzalo.cao(at)gmail.com

### Version
0.2

### Video demo
[![CHIP Binary clock demo](https://img.youtube.com/vi/jDt31H7_JK8/0.jpg)](https://www.youtube.com/watch?v=jDt31H7_JK8)

### Tech
In order to construct this project you'll need some extras
* [CHIP](https://www.getchip.com/pages/chip) computer by NTC
* [CHIP_IO python library](https://github.com/xtacocorex/CHIP_IO)
* 17 x 3.3v leds
* 17 x 100ohm resistances
* 18 x male-male arduino cables
* You'll probably need also some kind of 

### Instructions
* Install [CHIP_IO python library](https://github.com/xtacocorex/CHIP_IO)
* Build the scheme
* run "sudo python binary-clock.py"

### Construction scheme

Time bit      CHIP Output   Rest of the circuit              CHIP GND line

Hour bit 4:   LCD-D3      -> 100 Ohm resistor -> LED 3.3V    -> GND  
Hour bit 3:   LCD-D4      -> 100 Ohm resistor -> LED 3.3V    -> GND  
Hour bit 2:   LCD-D5      -> 100 Ohm resistor -> LED 3.3V    -> GND  
Hour bit 1:   LCD-D6      -> 100 Ohm resistor -> LED 3.3V    -> GND  
Hour bit 0:   LCD-D7      -> 100 Ohm resistor -> LED 3.3V    -> GND  


Minute bit 5: LCD-10      -> 100 Ohm resistor -> LED 3.3V    -> GND  
Minute bit 4: LCD-11      -> 100 Ohm resistor -> LED 3.3V    -> GND  
Minute bit 3: LCD-12      -> 100 Ohm resistor -> LED 3.3V    -> GND  
Minute bit 2: LCD-13      -> 100 Ohm resistor -> LED 3.3V    -> GND  
Minute bit 1: LCD-14      -> 100 Ohm resistor -> LED 3.3V    -> GND  
Minute bit 0: LCD-15      -> 100 Ohm resistor -> LED 3.3V    -> GND  


Second bit 5: LCD-18      -> 100 Ohm resistor -> LED 3.3V    -> GND  
Second bit 4: LCD-19      -> 100 Ohm resistor -> LED 3.3V    -> GND  
Second bit 3: LCD-20      -> 100 Ohm resistor -> LED 3.3V    -> GND  
Second bit 2: LCD-21      -> 100 Ohm resistor -> LED 3.3V    -> GND  
Second bit 1: LCD-22      -> 100 Ohm resistor -> LED 3.3V    -> GND  
Second bit 0: LCD-23      -> 100 Ohm resistor -> LED 3.3V    -> GND  


