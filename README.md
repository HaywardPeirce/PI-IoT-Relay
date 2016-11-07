# PI-IoT-Relay

A Raspberry Pi-based relay that is connected up to Adafruit.io. The python script is run as a service using Upstart.

### Resources

The code for including Adafruit.io was found here: https://github.com/adafruit/io-client-python

Understanding how RPi.GPIO works was learned here: https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/

The inspiration for the base python script I wrote was found here: https://learn.adafruit.com/adafruits-raspberry-pi-lesson-13-power-control/overview

Details about how to wire up a relay were also found here: http://tech.iprock.com/wp-content/uploads/2013/08/Pi-Power-Controller-Wiring-Diagram-SainSmart.jpg

### Instilation

Install Upstart:
`sudo apt-get upstart`

Follow the adafruit.io installation instructions

Place the python script in the pi home directory

Place the Adafruit APIkey in a files in the pi user home directory called apikey.txt

Place the relayservice.conf file in /etc/init

Reboot the Pi
