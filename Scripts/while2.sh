#! /bin/bash

x=1

while [ $x -le 10 ]
do
	if [ $x == 6 ]
	then
		echo "preruseno - break"
		break
	fi
	echo "Opakuji $x krat"

	((x++))
done
