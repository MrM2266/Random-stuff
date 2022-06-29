#! /bin/bash

while read login jmeno prijmeni uid primgroup groups
do
	echo "Zalozeni uzivatele"
	echo "====================="
	echo "Login: $login"
	echo "Jmeno: $jmeno"
	echo "Prijmeni $prijmeni"
	echo "uid: $uid"
	echo "Primarni skupina: $primgroup"
	echo "Skupiny: $groups"
	echo
	echo
	#sudo useradd -c "$jmeno $prijmeni" -u $uid -g $primgroup -G groups -m -s /bin/bash $login

done < uzivatele01.txt

