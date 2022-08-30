RPi-SenseStation Mosquitto setup
================================

## Setup
### Install via APT
```sh
$ sudo apt install mosquitto
```

### Create password file
```sh
$ sudo mosquitto_passwd /etc/mosquitto/passwd somni
  # password input will be prompted
```
 - You can change `somni` with any name you want.
 - Password information will be used while setting up MQTT integration in Home Assistant, so remember the username and password!

### Copy RPi-SenseStation specific configuration file
```sh
$ sudo cp <PATH_TO_conf.d/sensestation.conf> /etc/mosquitto/conf.d/
```

### Restart Mosquitto broker
```sh
$ sudo service mosquitto restart
```

### Add MQTT integration in Home Assistant
 - **Broker**: `localhost`
 - **Port**: `8889`
 - **Username**: `somni` or any username you created with `mosquitto_passwd` command
 - **Password**: The password you entered in `mosquitto_passwd` command
