
# _____             _                 _____ _____ 
#|   __|___ ___ ___| |_ ___ _ _ _____|     |   __|
#|__   | . | -_|  _|  _|  _| | |     |  |  |__   |
#|_____|  _|___|___|_| |_| |___|_|_|_|_____|_____|
#      |_|   
# SpectrumOS - Embrace the Chromatic Symphony!
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence 
#
## 
import json
import os
from libqtile.lazy import lazy

#Home Path
home = os.path.expanduser('~') # Path for use in folders

#Color Variables
## Import Colors from Pywal
with open(home + '/.cache/wal/colors.json') as wal_import:
  data = json.load(wal_import)
  wallpaper = data['wallpaper']
  colors = data['colors']
  val_colors = list(colors.values())
  def getList(val_colors):
    return [*val_colors]
    
  def init_colors():
    return [*val_colors]

color = init_colors()

def hex_to_rgb(hex_color):
    # Remove the '#' if it exists in the input
    hex_color = hex_color.lstrip('#')
    # Convert the hex color to RGB
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return r, g, b

def rgb_to_hex(rgb_color):
    # Convert RGB values to a hex color code
    hex_color = "#{:02X}{:02X}{:02X}".format(*rgb_color)
    return hex_color

def darken_color(hex_color, factor=0.3):
    # Convert hex color to RGB
    r, g, b = hex_to_rgb(hex_color)
    
    # Darken the color by reducing each RGB component
    r = int(r * factor)
    g = int(g * factor)
    b = int(b * factor)
    
    # Ensure values are within the valid RGB range (0-255)
    r = max(0, r)
    g = max(0, g)
    b = max(0, b)
    
    # Convert the darkened RGB color back to hex
    darkened_hex_color = rgb_to_hex((r, g, b))
    
    return darkened_hex_color

def lighten_color(hex_color, factor=1.2):
    # Convert hex color to RGB
    r, g, b = hex_to_rgb(hex_color)
    
    # Lighten the color by increasing each RGB component
    r = min(255, int(r * factor))
    g = min(255, int(g * factor))
    b = min(255, int(b * factor))
    
    # Convert the lightened RGB color back to hex
    lightened_hex_color = rgb_to_hex((r, g, b))
    
    return lightened_hex_color

def generate_palettes(hex_color_list):
    # Darken and lighten the colors in the input list
    darkened_colors = [darken_color(color) for color in hex_color_list]
    brighter_colors = [lighten_color(color) for color in hex_color_list]
    
    return brighter_colors, darkened_colors

secondary_color, third_color = generate_palettes(color)

#### Import Configuuration File ####
## Import config
file = open(home + '/.config/qtile/variables', 'r')
variables=file.readlines()

## Read picom.conf for blur in the bar
file = open(home + '/.config/picom/picom.conf', 'r')
bar_blur=file.readlines()
current_blur = bar_blur[279].strip()

if current_blur == '"QTILE_INTERNAL:32c = 0"':
  new_blur = '"QTILE_INTERNAL:32c = 1"' + "\n"
  bar_blur[279] = new_blur
  blur_icon=''
else:
  new_blur = '"QTILE_INTERNAL:32c = 0"' + "\n"
  bar_blur[279] = new_blur
  blur_icon=''

## Get Terminal Fontsize
file = open(home + '/.config/alacritty/alacritty.toml', 'r')
term_size=file.readlines()
terminal_font_size = term_size[21].strip()

## Sticky Windows

sticky_windows=[]

## Move Window to current Group
@lazy.function
def toggle_sticky_windows(qtile, window=None):
    if window is None:
        window = qtile.current_screen.group.current_window
    if window in sticky_windows:
        sticky_windows.remove(window)
    else:
        sticky_windows.append(window)
    return window