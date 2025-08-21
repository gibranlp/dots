#!/usr/bin/env bash

CONFIG_DIR="$HOME/.config/sketchybar"

first_state=$(sketchybar --query menu.1 | jq -r '.geometry.drawing')

if [ "$first_state" = "on" ]; then
  # Menus are visible → switch to spaces
  sketchybar --set '/menu\..*/' drawing=off
  sketchybar --set '/space\..*/' drawing=on
  sketchybar --set front_app drawing=on
else
  # Menus are hidden → show menus
  sketchybar --set '/space\..*/' drawing=off
  sketchybar --set front_app drawing=off
  "$CONFIG_DIR/scripts/update_menus.sh"
fi
