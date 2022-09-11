RPi-SenseStation
================
[🇰🇷 한국어](README.ko.md)

Some dumb DIY work with my [Raspberry Pi 3](https://www.raspberrypi.com/products/raspberry-pi-3-model-b/) + [Home Assistant](https://www.home-assistant.io/), making RPi a **total control and monitor tower** of my IoT devices and attached sensors.

<s>YAY such a money-wasting DIY project! but at least I gave my rolling-on-the-floor Raspberry Pi 3 a usage ;)</s>

Why are you doing this? Aren't you reinventing the wheels?
==========================================================
 - Just for fun!
 - Buying a finished product is very costly!
 - Building my own useful device is very accomplishing! isn't it?
 - Make a good experience and keep my *smol* hardware/electrician skill!
 - <s>Hey, what's the problem? I **just** wanted to build this from scratch, so don't bother me</s>

BOM
===
### Picked up in my room
 - Raspberry Pi 3 Model B
   - Info : https://www.raspberrypi.com/products/raspberry-pi-3-model-b/
 - Raspberry Pi Sense HAT
   - Info : https://www.raspberrypi.com/products/sense-hat/
 - Mean Well RS-15-5
   - Info : https://www.meanwell.com/Upload/PDF/RS-15/RS-15-SPEC.PDF
 - ~~microSD memory card~~
   - ~~SanDisk one~~ **corrupted and physically broken**
   - ~~SK Networks MOCAT one~~ **became write-protected or cause data loss in couple of days but normal after reformat, but I decided not to use microSD cards**
 - An *old* 2.5-inch HDD, which was from *old* Lenovo laptop
 - USB Type-A to USB Micro Type-B fast-charging cable
 - A breadboard
   - or a perfboard, if you decided to solder these *smol* things
 - A bunch of M-F/M-M wires
 - (An soldering iron and its friends)
   - (Actually I bought a new soldering iron, because the made-in-China cheap one which I was bought from AliExpress is ...*a trash*)

### Bought from specialized store ([디바이스마트](https://www.devicemart.co.kr/))
 - RF-180 power socket
   - Info : https://www.devicemart.co.kr/goods/view?no=21446
 - 8-shaped AC cable
   - Damn I don't know how to call it in English
   - Info : https://www.devicemart.co.kr/goods/view?no=16542
 - VCTF power cord (0.75SQ x 3C, 1M)
   - Info : https://www.devicemart.co.kr/goods/view?no=10886536
 - (SZH-AT002) Raspberry Pi cooling fan
   - Info : https://www.devicemart.co.kr/goods/view?no=1361327
 - (ONE011) DHT11 temperature/humidity module
   - Info : https://www.devicemart.co.kr/goods/view?no=10916343
 - (ONE023) Vibration sensor module
   - Info : https://www.devicemart.co.kr/goods/view?no=10916350
 - (ONE026) CdS light sensor module
   - Info : https://www.devicemart.co.kr/goods/view?no=10916353
 - (ONE013) Sound pressure sensor module
   - Info : https://www.devicemart.co.kr/goods/view?no=10916345
 - (ONE007) MQ-2 flammable gas sensor module
   - Info : https://www.devicemart.co.kr/goods/view?no=10916339
 - (ONE009) IR phototransistor infrared receiver module
   - Info : https://www.devicemart.co.kr/goods/view?no=10916341
 - (ELB030103) IR double-headed infrared transmitter module
   - Info : https://www.devicemart.co.kr/goods/view?no=1310703
 - Microchip Technology MCP3008-I/P ADC converter
   - Product info : https://www.microchip.com/en-us/product/MCP3008
   - Info : https://www.devicemart.co.kr/goods/view?no=1322885
 - (To be added)

### Bought from some random stores
 - TP-Link Tapo P110 smart plug (2-Pack)
   - Product info : https://www.tp-link.com/kr/home-networking/smart-plug/tapo-p110/
 - MBF U3SATA-BK SATA to USB 3.0 (Type A) Converter
   - Product info : https://mybestfriend.co.kr/product/detail.html?product_no=3873&cate_no=332&display_group=3

Target devices to be controlled/monitored
=========================================
| Name of sensor or device          | Type         | Monitor/Control Target                                                        | Home Assistant Integration |
| --------------------------------- | ------------ | ----------------------------------------------------------------------------- | -------------------------- |
| DHT11                             | Sensor       | Temperature, Humidity                                                         | (GPIO →) MQTT              |
| MQ-2                              | Sensor       | Flammable gas concentration level                                             | (GPIO →) MQTT              |
| SW-420                            | Sensor       | Vibration detection                                                           | (GPIO →) MQTT              |
| CdS                               | Sensor       | Light level                                                                   | (GPIO →) MQTT              |
| Sound pressure sensor             | Sensor       | Sound pressure level                                                          | (GPIO →) MQTT              |
| Sense HAT                         | Sensor       | Gyroscope, Accelerometer, Magnetometer, Barometer, Temperature, Humidity      | (GPIO →) MQTT              |
| Xiaomi Mijia Smart Standing Fan 2 | IoT Device   | Device control                                                                | Xiaomi Miio                |
| Xiaomi Mi Air 2S                  | IoT Device   | Device control, Temperature, Humidity, PM2.5 particulates concentration level | Xiaomi Miio                |
| Tapo P110                         | IoT Device   | Device control, Electric power usage | HACS → Tapo Controller                 |
| Personal PC                       | Health Check | Power status using `ping`                                                     | MQTT                       |
| Samsung Hauzen A/C HS-B67PR       | IR Control   | Device control                                                                | MQTT (→ GPIO)              |
