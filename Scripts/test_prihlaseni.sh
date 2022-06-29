#! /bin/bash

echo "Zadejte login, ktery chcete sledovat:"
read login

while who | grep $login > /dev/null #výpis se nedává na obrazovku, ale do cerne diry
do
	sleep 20
done

echo "Uzivatel $login se prave odhlasil"
