# Middager
Displaying a google-kalender on a 8x8 diode matrix display
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
```

# Installation
Make sure the SPI is enabled.
- Go to https://developers.google.com/calendar/quickstart/python
- run the "Enable the Google Calendar API". 
- Give the project a name and hit "Next"
- Select "Desktop app" and hit "Create"
- Press `Download Client Configuration` and save in root directory (/home/pi/) as ".creds.json". Full pat should be `/home/pi/.creds.json`

Connect the display to the serial ports pins with Raspi IO pins

Run the program using command:
```
python3 Middager/middag.py
```
When powering up, have the led display disconnected from power as the load might make starting up the Pi a strain on the input voltage.

In case of error message from the dot-matrix driver, try chaning line 69 of middag.py to
```
        serial = spi(port=0, device=0, cs_high=True, gpio=noop())
```

# Setting up continuous running from boot
## CRON run
To run the display continuously, enter a crontab line like this:
```
*/10 * * * * python3 /home/pi/Middager/middag.py
```
## Service
Alternatively, install as service by copying the service file `/etc/systemd/system` using root.:
```
$ sudo cp  middager-sync.service /etc/systemd/system/middager-sync.service
```