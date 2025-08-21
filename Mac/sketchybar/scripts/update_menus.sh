#!/usr/bin/env bash

CONFIG_DIR="$HOME/.config/sketchybar"
MAX_ITEMS=15

# Hide all menu items first
sketchybar --set '/menu\..*/' drawing=off
sketchybar --set menu.padding drawing=on

id=1
"$CONFIG_DIR/helpers/menus/bin/menus" -l | while IFS= read -r menu; do
  if [ $id -le $MAX_ITEMS ]; then
    sketchybar --set "menu.$id" label="$menu" drawing=on
  else
    break
  fi
  id=$((id+1))
done
