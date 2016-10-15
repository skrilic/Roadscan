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
python gpspectrum.py -g off -p /dev/ttyUSB0 -d /home/slaven/Documents/rfid -c rfid -t 10 -s 3
echo -e "AKO JE PROBNO MJERENJE PROSLO UREDU PRITISNITE BILO KOJU TIPKU ZA NASTAVAK:"
read tipka3
echo "KOLIKO DUGO CE TRAJATI MJERENJE U SEKUNDAMA (40min=2400sec):"
read timesec
echo -e "MJERENJE POCINJE..."
python gpspectrum.py -g /dev/ttyUSB1 -p /dev/ttyUSB0 -d /home/slaven/Documents/rfid -c rfid -t $timesec -s 3

