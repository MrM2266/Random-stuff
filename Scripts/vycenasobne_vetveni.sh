#!/bin/bash

read -p "Zadejte znak: " znak
echo -n "Znak je: "


case $znak in
	[0-9]) echo cislo;;
	[A-Z]) echo velke pismeno;;
	[a-z]) echo male pismeno;;
	*) echo jiny znak;;

esac
