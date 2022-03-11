#!/bin/bash

while getopts p:f: option 
do
    case "${option}" in
        p) PORT=${OPTARG};;
        f) FILE=${OPTARG};;
    esac
done

if [ -z "$FILE" ]; then
    if [ -n "$1" ]; then 
        FILE=$1;
    else
        echo "Please supply a file";
        exit 0;
    fi
fi

if test -f "$FILE"; then
    cd presentation_runner;
    ln -s -f ../$FILE presentatie.md;

    npm start -- --port=$PORT;
else 
    echo $FILE + " does not exist";
fi