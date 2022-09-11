#!/usr/bin/env bash
echo -e "MAKE SURE GPS AND FSH ARE CONNECTED?"
echo -e "PRESS ANY KEY FOR NEXT ... ..."
read tipka2
#su -c ./testports.sh
#echo -e "AKO JE SVE UREDU, PRITISNITE d ZA NASTAVAK. "
#read tipka2
#if [ $tipka2!="d" ]; then
#exit()
#fi
su -c "chmod 777 /dev/ttyUSB0; chmod 777 /dev/ttyUSB1"
python roadscan-cli.py -g off -p /dev/ttyUSB0 -d data/muxa_36 -c conf/muxa_36.ini -t 10 -s 3 -a on
echo -e "PRESS ANY KEY FOR NEXT ... OR Ctrl+C TO STOP."
read tipka3
echo -e "MEASUREMENT DURATION IN secs:"
read timesec
echo -e "GPS PORT (ie. /dev/ttyUSB1 or off to disable GPS read out):"
read gpsport
echo -e "MEASUREMENT IS STARTING..."
python roadscan-cli.py -g $gpsport -p /dev/ttyUSB0 -d data/muxa_36 -c conf/muxa_36.ini -t $timesec -s 2 -a on
