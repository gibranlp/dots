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

# Pywal Colors
source "$HOME/.cache/wal/colors.sh"

# Padding item before apple icon
sketchybar --add item spacer.left padding=5

# Add the Apple icon item
sketchybar --add item apple left \
  --set apple \
    icon="" \
    icon.font="Hack Nerd Font:Bold:20.0" \
    icon.padding_left=0 \
    icon.padding_right=5 \
    label.drawing=off \
    icon.color="0xff${color7:1}" \
    background.color="0x00${color0:1}" \
    padding_left=1 \
    padding_right=1 \
    click_script="$CONFIG_DIR/helpers/menus/bin/menus -s 0"

# Padding item after apple icon
sketchybar --add item spacer.right padding=7
