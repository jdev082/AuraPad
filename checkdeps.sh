#!/bin/bash
#checks for dependencies

if ! which python3
then
	echo "Python3 is not installed, AuraPad won't run!"
	exit 1
fi


