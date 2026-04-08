#!/bin/bash

battery=$((RANDOM % 101))             #generates a random number from 0-100(both inclusive)
echo "Battery level: $battery%"

if [ $battery -lt 20 ]; then          #checks its battery percentage
    echo "Battery low! Return to base!"
    exit 1
fi

ping -c 1 google.com > /dev/null 2>&1 #to check netwrok connection

if [ $? -ne 0 ]; then
    echo "Communication failure!"    #-ne 0 is not eual to 0, then comminication had failed
    exit 1
fi

echo "All systems operational!"      #prints when everything is fine
