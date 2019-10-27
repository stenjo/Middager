# Middager
Lister opp en google-kalender på et 8x8 diode matrix display
Using the library to drive the dot matrix led display cascaded:
https://pypi.org/project/luma.led_matrix/


# Requirements:
```
pip3 install --upgrade luma.led_matrix
pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
pip3 install --upgrade python-dateutil
pip3 install backports-datetime-fromisoformat
```
In case of error message on installing the libraries, this might work:
```
sudo apt-get install libjpeg-dev zlib1g-dev
pip install Pillow

# Installation
Make sure the SPI is enabled.

Connect the display to the serial ports pins with Raspi IO pins
When powering up, have the led display disconnected from power as the load might make starting up the Pi a strain on the input voltage.
