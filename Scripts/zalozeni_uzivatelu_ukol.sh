#! /bin/bash

while IFS=";" read login jmeno prijmeni uid primgroup groups pokoj
do
	if grep -q $login: /etc/passwd
	then
		echo "Login jiz zalozen"
		continue
	else
		if grep -q $uid: /etc/passwd
		then
			echo "Login s uid $uid jiz existuje"
			continue
		else

			echo "Zalozeni uzivatele"
			echo "====================="
			echo "Login: $login"
			echo "Jmeno: $jmeno"
			echo "Prijmeni: $prijmeni"
			echo "uid: $uid"
			echo "Primarni skupina: $primgroup"
			echo "Skupiny: $groups"
			echo "Pokoj: $pokoj"
			echo
			echo
			continue
		fi
	fi

	#sudo useradd -c "$jmeno $prijmeni" -u $uid -g $primgroup -G groups -m -s /bin/bash $login

done < ceta.txt

