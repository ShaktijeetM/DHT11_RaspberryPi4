#! /usr/bin/env python



# Import necessary libraries for communication and display use
import I2C_LCD
import DHT
import time


dht = DHT.DHT11(4)
display = I2C_LCD.Lcd()

# Main body of code
try:
	while True:
		ec,temp,hum=dht.read()
		display.lcd_clear()
		if(dht.is_valid):
			display.lcd_display_string("Temp: "+str(temp)+" C",1)
			display.lcd_display_string("Rel Hum: "+str(hum)+" %",2)
			print('Temp:{} C'.format(temp))
			print('Hum:{} %'.format(hum))
		time.sleep(4)
except KeyboardInterrupt:
    # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    gpio.cleanup()
    display.lcd_clear()
