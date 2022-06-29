#!/bin/bash
#skript pro zobrazení stavu pc

#datum + cas

echo BASIC SYSTEM INFO:
uname -nvr
echo
echo uptime
uptime
echo
echo LAST BOOT:
who -b
echo
echo NETWORK ADAPTERS:
ip link
echo

echo TEST PING google.com:
ping -c 3 www.google.com
