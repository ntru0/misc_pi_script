# misc_pi_script
Miscellaneous scripts I use for my raspberry pi.

# Motivations
 I have a Garmin Forerunner 55 which unfortunately doesn't track strength training on the default watch setting. 

If I want to keep track of my activities, I have to record my session under 'Others' and then manually changing my activities to strength training everytime in the app.
 
To make the task less tedious, I wrote this small script that a raspberry pi will run and will automatically update any recent 'Others' activities to strength training.

I referenced [this massive command line garmin python demo](https://github.com/cyberjunky/python-garminconnect) when referring to API calls. 

The Pi will run this script every 24 hours or so and change any 'Others' activities to strength training.

I will expand this project if I have more ideas. 

# Setting Up Raspberry Pi

So grab Imager from the Raspberry Pi OS and flash it into your microSD. 

Orignally, I wanted to go headless (not use any monitor attched to my Pi) but I ran into some SSH issue on my laptop and ended up hooking up the pi to my TV as a monitor and grabbed a spare keyboard.

Booted it up, enable SSH via
```
sudo systemctl enable ssh
sudo systemctl start ssh
```

on your Pi OS. 

SCP files from your laptop over to your pi.

```
scp garmin_others_to_str.py nhi@raspberrypi.local:~/

scp coordinator.py nhi@raspberrypi.local:~/
scp garmin_others_to_str.py nhi@raspberrypi.local:~/

scp garminapps.service nhi@raspberrypi.local:~/
```

ssh bash into the pi:

```
ssh nhi@raspberrypi.local
```
copy into

```
# Copy service file into place
sudo cp ~/garminapps.service /etc/systemd/system/garminapps.service

# Reload systemd, enable and start
sudo systemctl daemon-reload
sudo systemctl enable garminapps
sudo systemctl start garminapps

# Confirm it's running
sudo systemctl status garminapps
```


