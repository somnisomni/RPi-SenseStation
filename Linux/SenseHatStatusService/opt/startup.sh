#!/bin/sh

PYTHON3=$(/usr/bin/which python3)

cd $(dirname $0)
$PYTHON3 sensehat-startup.py
$PYTHON3 sensehat-persist.py
