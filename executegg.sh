#!/bin/bash
if [ $# -eq 1 ] && [ $1 == "help" ]
then
    cat /Users/admin/Desktop/Workspaces/t1a3/docs/t1a3help.txt
else
    python3 /Users/admin/Desktop/Workspaces/t1a3/main.py
fi