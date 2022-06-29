#! /bin/bash

input="student02"

if grep -q $input /etc/passwd;
then
	echo "Uzivatel $input nalezen"
else
	echo "Uzivatel $input nenalezen"

fi


if [ -f /etc/group ];
then
	echo "soubor existuje"

fi


if [ -d /home/uzivatel/Scripts/test/Adresare ]
then
	echo "Soubor Adresare nalezen"
else
	echo "Soubor Adresare nenalezen - bude vytvoren"
	mkdir /home/uzivatel/Scripts/test/Adresare

fi


getent passwd | while IFS=: read -r name password uid gid gecos home shell; do
if [ -d /home/uzivatel/Scripts/test/Adresare/$name ]
then
	echo "$name		ok"
else
	mkdir /home/uzivatel/Scripts/test/Adresare/$name
	echo "$name		created"
fi
	
done
