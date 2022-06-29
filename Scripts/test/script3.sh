#! /bin/bash

echo "Zadejte vstup:"
read input

while IFS=: read clen1 clen2
do
	if [ "$input" = "$clen1" ]
	then
		echo "Protiklad k $input je $clen2"
	fi

	if [ "$input" = "$clen2" ]
	then
		echo "Protiklad k $input je $clen1"
	fi

done < protiklady.txt
