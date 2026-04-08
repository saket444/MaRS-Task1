#!/bin/bash

mkdir -p rover_mission       #creating the directery(-p is added to not give the error of file already exists)
cd rover_mission          #going into the directory

touch log1.txt log2.txt log3.txt      #creating log files

mv log1.txt mission_log.txt           #renaming the log1 file

echo "ERROR" > mission_log.txt        #not given in question, done to test the search command only

find . -name "*.log"                  #finding .log files

cat mission_log.txt                   #displays file content

grep "ERROR" mission_log.txt          #searches for ERROR

wc -l mission_log.txt                 #counts lines in mission_log

date                                  #shows the date

top                                   #shows system performance
