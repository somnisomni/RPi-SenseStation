#!/bin/sh
# Please run as root

pushd $(dirname $0)

OPT_DIR=/opt/somni/sensehat-status
FILES_DIR=./opt

mkdir -p $OPT_DIR
cp $FILES_DIR/* $OPT_DIR/

cp somni-startup.service /etc/systemd/system/somni-startup.service
chmod 644 /etc/systemd/system/somni-startup.service

cp somni-shutdown.service /etc/systemd/system/somni-shutdown.service
chmod 644 /etc/systemd/system/somni-shutdown.service

systemctl daemon-reload
systemctl enable somni-startup.service
systemctl enable somni-shutdown.service

popd
