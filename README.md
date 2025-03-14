# DHT11_RaspberryPi4

The code works with current version RaspiOs

1. Create a virtual environment in a directory using following commands
  sudo apt install python3-venv
  python3 -m venv TestProjects --system-site-packages

2.  You will need to activate the virtual environment every time the Pi is rebooted. To activate it, type:
  source env/bin/activate

3. To deactivate type:
   deactivate

4. Install any required packages using pip3
   pip3 install smbus

5. REBOOT the device

6. Run all the programs in CLI from inside the virtual environment 


Connections:

For DHT11:
GND - GND of Raspberry Pi 4
Data - 10K - 3.3 V  (Pull-up with 10K resistor)
Data - GPIO 4
VCC - 3.3V of Raspberry Pi 4 
