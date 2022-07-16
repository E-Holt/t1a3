#!/bin/bash
if [ $# -eq 1 ] && [ $1 == "help" ]
then
    cat docs/help.txt
else
    python3 src/main.py
fi