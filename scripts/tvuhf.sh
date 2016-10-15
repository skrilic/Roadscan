#!/bin/bash
echo -e "PROVJERITE DA LI SU SPOJENI GPS I FSH NA NOTEBOOK?"
echo -e "PRITISNITE BILO STO ZA NASTAVAK ..."
read tipka2
#su -c ./testports.sh
#echo -e "AKO JE SVE UREDU, PRITISNITE d ZA NASTAVAK. "
#read tipka2
#if [ $tipka2!="d" ]; then
#exit()
#fi
su -c "chmod 777 /dev/ttyUSB0; chmod 777 /dev/ttyUSB1"
python gpspectrum.py -g off -p /dev/ttyUSB0 -d /home/slaven/Documents/tvuhf -c tvuhf -t 10 -s 3
echo -e "AKO JE PROBNO MJERENJE PROSLO UREDU PRITISNITE BILO KOJU TIPKU ZA NASTAVAK:"
read tipka3
echo -e "KOLIKO DUGO CE TRAJATI MJERENJE U SEKUNDAMA (40min=2400sec):"
read timesec
echo -e "GPS PORT (npr. /dev/ttyUSB1 ili off za iskljuceno):"
read gpsport
echo -e "MJERENJE POCINJE..."
python gpspectrum.py -g $gpsport -p /dev/ttyUSB0 -d /home/slaven/Documents/tvuhf -c tvuhf -t $timesec -s 2

