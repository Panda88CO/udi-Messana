## Configuration and setup

 >Multiple Temperature Sensors DS18B20 can be placed placed on the same 2 wire bus on RPi - Vcc Pin1, GND Pin6, Data Pin7 - 4.7K Ohm resistor from pin7 to pin 1 - only one resistor is needed if multiple sensors are used 
(Only tested with 2 sensors this far)

> shortPoll updates temperature
> longPoll logs values for 24Hour Min/Max

>Use custom config parameters to name sensors in node server/ISY.  
1) Look for log entry temppoly:discover: rpitemp1 Sensor<n> 00000xxxxxxx
2) Copy 00000xxxxxxx to custom parameter
3) Specify the desired name as value
4) Erase nodes (Sensor<n>)
5) Restart node Server
I have been trying to use a files for this config but no luck so far 

> Uses W1ThemSensor library - more info can be found there 


#### For more information:
- <https://www.raspberrypi.org/documentation/usage/gpio/>
- <https://pinout.xyz/pinout/wiringpi>
- <https://github.com/timofurrer/w1thermsensor>
