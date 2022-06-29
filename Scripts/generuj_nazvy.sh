#! /bin/bash

echo "Zadejte pocatecni cislo zakladanych uzivatelskych uctu:"
read x

echo "Zadejte koncove cislo zakladanych uzivatelskych uctu:"
read y

for (( a=$x; $a-($y+1); a=$a+1 ))
do
	if (($a < 10))
	then
		echo 0$a
	else
		echo $a
	fi

done
