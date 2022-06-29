#! /bin/bash

for i in student11 student12 student13
do
	sudo useradd -c $i-g Students -m -s /bin/bash $i
	echo "Zalozen ucet s loginem $i"
	echo "Vypis ze souboru /etc/passwd:"
	echo 'getent passwd $i'
	sleep 3
done
