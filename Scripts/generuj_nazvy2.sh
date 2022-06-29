#! /bin/bash

for i in {1..15}
do
	if ($i < 10)
	then
		jmeno ="Zak c. 0"$i
		uid = 600$i
	else
		jmeno = "Zak c."$i
		uid = 60$i
	fi

	echo jmeno
	echo guid
	echo
	

done
