RPi-SenseStation Sense-HAT Status Display Service
=================================================
This directory contains some Systemd service files and Python script files for Sense-HAT LED control.

## ... what?
With this, Sense-HAT's LED matrix will react on OS boot completed, during OS shutdown, and keep blinking one pixel while OS running.  
I made this to check boot status and just for fun.

  - [`sensehat-startup.py`](opt/sensehat-startup.py): Python script for startup swirl animation. This will be executed first by `startup.sh`.  
    ![Sense-HAT startup animation](/DocsResources/SenseHatStatusService-Startup.gif)
  - [`sensehat-persist.py`](opt/sensehat-persist.py): Python script for persist blinking animation. This will be executed after `sensehat-startup.py` by `startup.sh`.  
    ![Sense-HAT persist animation](/DocsResources/SenseHatStatusService-Persist.gif)
  - [`sensehat-shutdown.py`](opt/sensehat-shutdown.py): Python script for shutdown starry animation. This will be executed by `shutdown.sh`, and for nearly 10 seconds.  
    ![Sense-HAT shutdown animation](/DocsResources/SenseHatStatusService-Shutdown.gif)
  - [`startup.sh`](opt/startup.sh): Shell script to execute `sensehat-startup.py` and `sensehat-persist.py`. This is an entrypoint of `somni-startup.service`.
  - [`shutdown.sh`](opt/shutdown.sh): Shell script to execute `sensehat-shutdown.py`. This is an entrypoint of `somni-shutdown.service`.
  - [`somni-startup.service`](somni-startup.service): Systemd service file for startup, started after `multi-user.target`(boot completed).
  - [`somni-shutdown.service`](somni-shutdown.service): Systemd service file for shutdown/halt/reboot.
  - [`install.sh`](install.sh): Copy contents of [`opt/`](opt/) directory to `/opt/somni/sensehat-status`, and register Systemd service files.
  - [`uninstall.sh`](uninstall.sh): Delete contents of `/opt/somni/sensehat-status`, and unregister Systemd service files and delete them.

## Install and uninstall
To install, try `$ sudo bash install.sh`. To uninstall, try `$ sudo bash uninstall.sh`. Simple and will just work in most cases.
