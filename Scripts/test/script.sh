#! /bin/bash

pr1="obsah"
moravec="gay"

echo "test string"

echo $pr1


for i in moravec je gay
do
	echo $i
done

if [ "$moravec"="gay" ];
then
	echo "ano"
fi


cislo1=20
cislo2=20

if [  $cislo1 -eq  $cislo2 ];
then
	echo "cisla se rovnaji"
else
	echo "cisla se nerovnaji"
fi


