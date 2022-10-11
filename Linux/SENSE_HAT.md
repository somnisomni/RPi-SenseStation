RPi-SenseStation Sense-HAT Addendum
===================================

Don't change I2C baudrate
-------------------------
Changing I2C baudrate with `dtparam=i2c_baudrate=<NNNNNN>` in `config.txt` can result the Sense-HAT kernel module fail to read I2C data.

No console shows on HDMI monitor
--------------------------------
This is because Sense-HAT framebuffer has been set on `/dev/fb0`. In this case, normal VC4 framebuffer will set on `/dev/fb1` and Sense-HAT LED matrix keep cleared even set pixels or something on it.

~~I can't find how Nth framebuffer to be set as default, or change ordering for now.~~ **SEE "Workaround" BELOW**

This seems to happen sometimes, so it's worth trying to reboot`(ctrl+alt+del)` Pi again and again until you see console TTY on your monitor, if you have to.

### Workaround
A workaround for this problem is to set `framebuffer_priority` in `config.txt`. In `config.txt`, add lines below:
  ```
  # `framebuffer_priority` config does not work with KMS driver, so the driver should be disabled to apply this workaround
  # Just comment out existing dtoverlay line
  #dtoverlay=vc4-kms-v3d

  framebuffer_priority=2
  display_default_lcd=0
  ```
Since we are going to use Pi as headless/CLI-only, so it's not very big deal not to use VC4 KMS driver. But on my system disabling `vc4-kms-v3d` will make screen keep flickering/flashing, and I can't figure out why this happens. ~~At least it's far better than nothing shown on monitor~~

You can check out official references of [`framebuffer_priority`](https://www.raspberrypi.com/documentation/computers/config_txt.html#framebuffer_priority) and [`display_default_lcd`](https://www.raspberrypi.com/documentation/computers/config_txt.html#display_default_lcd).

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

Additionally, if you keep seeing `UU` in `i2cdetect` after do this, it looks like kernel modules of individual sensor are loaded. Execute `lsmod` and find some modules including sensor model names, and block it.  
Some known modules: `hts221_spi`, `hts221_i2c`, `hts221`

