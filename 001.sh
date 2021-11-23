#!/bin/bash
USER=`whoami`
DATE="2021-11-23"

echo "$USER | $DATE"
ls -lS /home/dsc/data/opentraveldata/ | head -2 | tail -1
