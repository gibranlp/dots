#!/usr/bin/env bash

CONFIG_DIR="$HOME/.config/sketchybar"
MAX_ITEMS=20

# Create menu items
for i in $(seq 1 $MAX_ITEMS); do
  sketchybar --add item "menu.$i" left \
             --set "menu.$i" \
                  padding_left=$PADDINGS \
                  padding_right=$PADDINGS \
                  drawing=off \
                  icon.drawing=off \
                  label.padding_left=6 \
                  label.padding_right=6 \
                  click_script="$CONFIG_DIR/helpers/menus/bin/menus -s $i"
done

# Bracket for menu items
sketchybar --add bracket menu_items '/menu\..*/' \
           --set menu_items background.color=$BG_COLOR

# Padding item
sketchybar --add item menu.padding left \
           --set menu.padding drawing=off width=5

# Create scripts folder if missing
mkdir -p "$CONFIG_DIR/scripts"

# Subscribe update_menus to front_app_switched
sketchybar --set menu.padding script="$CONFIG_DIR/scripts/update_menus.sh"
sketchybar --subscribe menu.padding front_app_switched

# Add and subscribe swap event
sketchybar --add item space_menu_swap left \
           --set space_menu_swap drawing=off script="$CONFIG_DIR/scripts/swap_menus_and_spaces.sh"
sketchybar --add event swap_menus_and_spaces
sketchybar --subscribe space_menu_swap swap_menus_and_spaces

# Initial load
"$CONFIG_DIR/scripts/update_menus.sh"
