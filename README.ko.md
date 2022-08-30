RPi-SenseStation
================
[🇺🇸 English](README.md)

[Raspberry Pi 3](https://www.raspberrypi.com/products/raspberry-pi-3-model-b/) + [Home Assistant](https://www.home-assistant.io/) 조합으로 IoT 디바이스 및 연결된 센서 등을 **컨트롤하고 모니터할 수 있도록 만드는** DIY 프로젝트입니다.

<s>방 안에 굴러다니는 라즈베리 파이 3를 드디어 활용해보네요! 아이 좋아라!</s>

이런걸 왜 해요? 이미 만들어진 프로젝트 없어요?
=============================================
 - 재미있잖아요!
 - 완제품은 비싸잖아요!
 - 실용적인 기기 하나 직접 만들어서 쓰면 왠지 뿌듯하잖아요! 그렇지 않아요?
 - 경험 하나 쌓아보는거죠~
 - *죠그마하지만* 하드웨어/전자기기 관련 실력도 유지하려구요~
 - <s>아니 **그냥** 만들어보고 싶어서 만드는데 왜그래요 냅둬요 ㅠㅠ</s>

BOM
===
### 방에 굴러다니던 부품들
 - Raspberry Pi 3 Model B
   - 정보 : https://www.raspberrypi.com/products/raspberry-pi-3-model-b/
 - Raspberry Pi Sense HAT
   - 정보 : https://www.raspberrypi.com/products/sense-hat/
 - Mean Well RS-15-5
   - 정보 : https://www.meanwell.com/Upload/PDF/RS-15/RS-15-SPEC.PDF
 - USB A타입 to micro-B타입 고속충전 케이블
 - 브레드보드
 - (만능기판)
 - M-F/M-M 와이어 여러개
 - (납땜인두기 및 납땜 관련 도구들)
   - (사실 이 프로젝트를 진행하면서 인두기를 새로 샀습니다. 기존에 쓰던 알리익스프레스에서 구매한 메이드-인-차이나 인두기가 정말... 못써먹을 정도라...)

### 특화 쇼핑몰([디바이스마트](https://www.devicemart.co.kr/))에서 구매
 - RF-180 전원 소켓
   - 정보 : https://www.devicemart.co.kr/goods/view?no=21446
 - 8자 AC 케이블
   - 정보 : https://www.devicemart.co.kr/goods/view?no=16542
 - VCTF 전원 코드 (0.75SQ x 3C, 1M)
   - 정보 : https://www.devicemart.co.kr/goods/view?no=10886536
 - (SZH-AT002) Raspberry Pi 쿨링 팬
   - 정보 : https://www.devicemart.co.kr/goods/view?no=1361327
 - (ONE011) DHT11 온·습도 센서 모듈
   - 정보 : https://www.devicemart.co.kr/goods/view?no=10916343
 - (ONE023) 진동 센서 모듈
   - 정보 : https://www.devicemart.co.kr/goods/view?no=10916350
 - (ONE026) CdS 조도 센서 모듈
   - 정보 : https://www.devicemart.co.kr/goods/view?no=10916353
 - (ONE013) 읍압 센서 모듈
   - 정보 : https://www.devicemart.co.kr/goods/view?no=10916345
 - (ONE007) MQ-2 인화성 가스 센서 모듈
   - 정보 : https://www.devicemart.co.kr/goods/view?no=10916339
 - (ONE009) IR 포토트랜지스터 적외선 수신 모듈
   - 정보 : https://www.devicemart.co.kr/goods/view?no=10916341
 - (ELB030103) IR 더블헤드 적외선 송신 모듈
   - 정보 : https://www.devicemart.co.kr/goods/view?no=1310703
 - Microchip Technology MCP3008-I/P ADC 컨버터
   - 제품 정보 : https://www.microchip.com/en-us/product/MCP3008
   - 정보 : https://www.devicemart.co.kr/goods/view?no=1322885
 - (추가 예정)

### 아무데서나 구매
 - TP-Link Tapo P110 스마트 플러그 (2-Pack)
   - 제품 정보 : https://www.tp-link.com/kr/home-networking/smart-plug/tapo-p110/

제어·모니터링할 기기
====================
### 센서
 - DHT11 온도 & 습도
 - MQ-2 인화성 가스 감지
 - 진동 감지
 - CdS 조도 레벨 감지
 - 음압 레벨 감지
 - Sense HAT 내장 센서
   - 자이로스코프
   - 가속도계
   - 자기계
   - 기압계
   - 온도
   - 습도

### IoT 기기
 - Xiaomi Mijia Smart Standing Fan 2 (BPLDS02DM)
 - Xiaomi Mi Air 2S

### 상태 체크
 - 개인 PC (`ping` 사용)

### IR 제어 기기
 - 삼성 하우젠 에어컨 (HS-B67PR)
