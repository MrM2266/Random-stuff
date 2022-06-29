#! /bin/bash


if grep "/bin/bash$" /etc/passwd >/dev/null
then
	echo "Bash je nastaven u techto uzivatelu:"
	awk -F ":" '$7 == "/bin/bash" {print $1}' /etc/passwd
else
echo "Bash nema nikdo nastaven"

fi


echo
echo "================================================="
echo

if grep "/nologin$" /etc/passwd > /dev/null
then
	echo "Prihlasit se nemuze uzivatel s loginem:"
	awk -F ":" '$7 == "/usr/sbin/nologin" {print $1}' /etc/passwd

else
	echo "Vsichni uzivatele se mohou prihlasit"
fi

