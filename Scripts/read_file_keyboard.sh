#! /bin/bash

echo "Zadejte nazev souboru:"
read filename

if [ -f $filename ]
then
	while read -r line
	do
		echo $line
		sleep 0.4
	done < "$file"

else
	echo "Zadany soubor neexistuje"

fi

