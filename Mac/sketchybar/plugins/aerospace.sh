#!/usr/bin/env bash
#####################################################
#  _____             _                 _____ _____  #
# |   __|___ ___ ___| |_ ___ _ _ _____|     |   __| #
# |__   | . | -_|  _|  _|  _| | |     |  |  |__   | #
# |_____|  _|___|___|_| |_| |___|_|_|_|_____|_____| #
#       |_|                                         #
# SpectrumOS - Embrace the Chromatic Symphony!      #
# By: gibranlp <thisdoesnotwork@gibranlp.dev>.      #
# MIT licence                                       #
#                                                   #
#####################################################

source "$HOME/.cache/wal/colors.sh"

if [ "$1" = "$FOCUSED_WORKSPACE" ]; then
  sketchybar --set "$NAME" \
    icon.color="0xff${color0:1}" \
    background.color="0xff${color1:1}"
else
  sketchybar --set "$NAME" \
    icon.color="0xff${color1:1}" \
    background.color="0x00${color0:1}"
fi

