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
# Array of icons per space (adjust as needed)
#icons=("" "󰺻" "󱥁" "" "󰈙" "󰢔" "󰊖" "󰎅" "" "")
icons=("" "󰺻" "󱥁" "" "󰈙" "󰢔")

for i in "${!icons[@]}"; do
  sid=$((i+1))
  icon="${icons[$i]}"

  sketchybar --add item space.$sid left \
    --subscribe space.$sid aerospace_workspace_change \
    --set space.$sid \
      icon="$icon" \
      icon.font="Hack Nerd Font:Bold:17.0" \
      icon.color="0xdd${color0:1}" \
      icon.highlight_color="0xdd${color1:1}" \
      icon.padding_left=4 \
      icon.padding_right=2 \
      background.corner_radius=3 \
      background.height=20 \
      background.drawing=off \
      click_script="aerospace workspace $sid" \
      script="$CONFIG_DIR/plugins/aerospace.sh $sid"
done

