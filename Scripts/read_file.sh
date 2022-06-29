#! /bin/bash

if [ $# -gt 0 ]
then 
	file=$1

	while read -r line
	do
		echo $line
		sleep 0.5
	done < "$file"

else
	echo "Chybi nazev souboru"

fi
