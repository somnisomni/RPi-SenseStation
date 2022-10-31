#!/bin/sh
# Please run as root

OPT_DIR=/opt/somni/sensehat-status

systemctl stop somni-startup.service
systemctl disable somni-startup.service

systemctl stop somni-shutdown.service
systemctl disable somni-shutdown.service

rm -rf $OPT_DIR
rm -f /etc/systemd/system/somni-startup.service
rm -f /etc/systemd/system/somni-shutdown.service

systemctl daemon-reload
