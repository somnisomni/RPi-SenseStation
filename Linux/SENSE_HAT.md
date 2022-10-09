RPi-SenseStation Sense-HAT Addendum
===================================

Prevent Industrial I/O take over I2C sensors of Sense-HAT
---------------------------------------------------------
> Ref: [EnvTrackerNode README](https://github.com/J-Pai/EnvTrackerNode/blob/master/README.md#raspberry-pi-setup)

When Sense-HAT connected to Raspberry Pi and recognized(either reading EEPROM or `dtoverlay` specified in `config.txt`) by Ubuntu, the Ubuntu will load `rpisense_{js,fb,core}` kernel module which we needs.  
But eventually Ubuntu loads Industrial I/O(`iio`) modules for recognized I2C sensors, which takes over corresponding I2C addresses of sensors, makes the sensors not available for reading data on other applications. In that situation, `i2cdetect` will show output like this:
```sh
$ sudo i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:                         -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- UU -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- UU -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- UU -- -- UU
60: -- -- -- -- -- -- -- -- -- -- 6a -- -- -- -- --
70: -- -- -- -- -- -- -- --
```
`UU` means that the address is being used by an application *(= Industrial I/O kernel modules)*, thus not available for other applications. This problem can be solved by blocking Industrial I/O kernel modules to be loaded.

  - Create the file `/etc/modprobe.d/blacklist-industrialio.conf` with contents:
    ```
    blacklist st_pressure_spi
    blacklist st_magn_spi
    blacklist st_sensors_spi
    blacklist st_magn_i2c
    blacklist st_pressure_i2c
    blacklist st_magn
    blacklist st_pressure
    blacklist st_sensors_i2c
    blacklist st_sensors
    blacklist industrialio_triggered_buffer
    blacklist industrialio
    ```
  - Reboot, Industrial I/O modules won't be loaded.
