#!/bin/bash
a=$(qtile cmd-obj -o group -f info | grep "name" | tail -1 | awk '{print $2}' | sed "s/[',]//g")
xdotool key super+$((a-1))
