# _____             _                 _____ _____ 
#|   __|___ ___ ___| |_ ___ _ _ _____|     |   __|
#|__   | . | -_|  _|  _|  _| | |     |  |  |__   |
#|_____|  _|___|___|_| |_| |___|_|_|_|_____|_____|
#      |_|   
# SpectrumOS - Embrace the Chromatic Symphony!
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence
#
#
import random
import socket
import subprocess
from os.path import expanduser
from pathlib import Path
import requests
from libqtile import bar, hook, layout, qtile, widget
from qtile_bonsai import Bonsai
from libqtile.config import ScratchPad, DropDown, Click, Drag, Group, Key, KeyChord, Match, Screen
from qtile_extras import widget
from qtile_extras.popup.toolkit import (PopupRelativeLayout, PopupWidget)
from qtile_extras.widget.decorations import (BorderDecoration,PowerLineDecoration,RectDecoration)
from rofi import Rofi
from colors import *

#### Variables ####
# Modifiers
mod = "mod4"
alt = "mod1"

#### Import Configuration File ####

## Import config
file = open(home + '/.config/qtile/variables', 'r')
variables=file.readlines()

## Read picom.conf for blur in the bar
file = open(home + '/.config/picom/picom.conf', 'r')
bar_blur=file.readlines()
current_blur = bar_blur[284].strip()

if current_blur == '"QTILE_INTERNAL:32c = 0"':
  new_blur = '"QTILE_INTERNAL:32c = 1"' + "\n"
  bar_blur[284] = new_blur
  blur_icon=''
else:
  new_blur = '"QTILE_INTERNAL:32c = 0"' + "\n"
  bar_blur[284] = new_blur
  blur_icon=''

## Get Terminal Fontsize
file = open(home + '/.config/alacritty/alacritty.toml', 'r')
term_size=file.readlines()
terminal_font_size:(term_size[21].strip())

# Wallpaper Options
light=str(variables[4].strip()) # Option for light themes

# Terminal 
terminal = "alacritty"

# Fonts
main_font = str(variables[11].strip())
symbols_font = "Symbols Nerd Font"
font_size=int(variables[12].strip())

# Bar size
bar_size=30

# Format of the prompt
prompt = "$".format(os.environ["USER"], socket.gethostname()) 

#Initialize Groups
groups = []
group_names = ["Escape","1","2","3","4","5","6","7","8","9"]
hide_unused_groups=bool(str(variables[8].strip()))

# Themes
current_theme=str(variables[1].strip())
themes_dir = os.path.expanduser("~/.config/qtile/themes")
theme_files = [f for f in os.listdir(themes_dir) if os.path.isfile(os.path.join(themes_dir, f))]
theme = [os.path.splitext(f)[0] for f in theme_files]
theme_dest = (home + "/.config/qtile/theme.py")
theme_file = themes_dir + "/" + current_theme

# Pywal Backends Options: Wal, Colorz, Colorthief, Haishoku
def_backend=str(variables[2].strip())
backend=['wal','colorz','colorthief','haishoku']

## Margins
layout_margin=10 # Layout margins
single_layout_margin=10 # Single window margin 
## Borders
layout_border_width=3 # Layout border width
single_border_width=3 # Single border width

# Bar Position
bar_position=str(variables[6].strip())

#Widgets
widget_width=200 #Width of widgets varies depending the resolution

# Get current screen resolution
resolution = os.popen('xdpyinfo | awk "/dimensions/{print $2}"').read()
xres = resolution[17:21]
yres = resolution[22:26]

# Set Bar and font sizes for different resolutions

# Common Settings
layout_margin=5
single_layout_margin=5 
layout_border_width=5
single_border_width=5

if xres == "4920" and yres == "2560" or xres == "3840" and yres == "2160": #4k
  bar_size=30
  widget_width=450
  terminal_font_size=10
  if bar_position == "bottom":
    bar_margin=[0,10,5,10]
  else:
    bar_margin=[5,10,0,10]
elif xres == "3840" and yres == "1080" or xres == "3834" and yres == "1080" or xres == "1920" and yres == "2160" or xres == "1920" and yres == "1080": #FullHD
  bar_size=25
  widget_width=100
  font_size=17
  terminal_font_size=9
  if bar_position == "bottom":
    bar_margin=[0,10,5,10]
  else:
    bar_margin=[5,10,0,10]
else: # 1366 x 768 Macbook air 11"
  layout_margin=2
  single_layout_margin=2  
  layout_border_width=2
  single_border_width=2
  font_size=14
  bar_size=20
  widget_width=100
  terminal_font_size=8
  bar_margin=[0,0,0,0]

# Set the right Terminal Font size
term_size[21] = "  size= " + str(terminal_font_size) + "\n"
with open(home + '/.config/alacritty/alacritty.toml', 'w') as file:
    file.writelines(term_size)

# Make font smaller for cetain groups icons
if int(variables[10]) in [5,7,8,9,10,11,12,13]:
   groups_font = font_size - 2
else:
   groups_font = font_size + 3

# Rofi Configuration Files
SOS_Backend= Rofi(rofi_args=['-theme', '~/.config/rofi/SOS_Backend.rasi'])
SOS_Themes= Rofi(rofi_args=['-theme', '~/.config/rofi/SOS_Themes.rasi'])
SOS_Panel= Rofi(rofi_args=['-theme', '~/.config/rofi/SOS_Panel.rasi'])
SOS_Network= Rofi(rofi_args=['-theme', '~/.config/rofi/SOS_Network.rasi'])
SOS_Audio= Rofi(rofi_args=['-theme', '~/.config/rofi/SOS_Faudio.rasi'])

# Weather
w_appkey = str(variables[3].strip()) # Get a key here https://home.openweathermap.org/users/sign_up 
w_cityid ="3995402" # "3514783" Veracruz, "3995402" Morelia, "3521342" Playa del Carmen https://openweathermap.org/city/

# Rofi Launcher
rofi_launcher = 'rofi -show drun -show-icons -theme "~/.config/rofi/SOS_Launcher.rasi"'
sudo_rofi_launcher = 'sudo rofi -show drun -show-icons -theme "~/.config/rofi/SOS_Launcher.rasi"'

#### Hooks ####
@hook.subscribe.startup
def start():
  subprocess.call(home + '/.local/bin/SOS_Restart')
      
@hook.subscribe.startup_once
def start_once():
  subprocess.call(home + '/.local/bin/SOS_Start')

@hook.subscribe.client_new
def follow_window(client):
  for group in groups:
    match = next((m for m in group.matches if m.compare(client)), None)
    if match:
      targetgroup = qtile.groups_map[group.name]
      targetgroup.toscreen(toggle=False)
      break

@hook.subscribe.client_name_updated
def follow_window_name(client):
  for group in groups:
    match = next((m for m in group.matches if m.compare(client)), None)
    if match:
      targetgroup = qtile.groups_map[group.name]
      targetgroup.toscreen(toggle=False)
      break

#### Functions ####
# Run i3-lock with Colors

def i3lock_colors(qtile):
  subprocess.run(['i3lock', 
    '--image=%s' % wallpaper,
    '--fill',          
    '--ring-color={}'.format(secondary_color[0]+"aa"),
    '--inside-color={}'.format(secondary_color[0]),
    '--line-color={}'.format(color[2]),
    '--separator-color={}'.format(color[4]),
    '--time-color={}'.format(color[2]),           
    '--date-color={}'.format(color[4]),
    '--insidever-color={}'.format(secondary_color[0]),
    '--ringver-color={}'.format(color[0]),
    '--verif-color={}'.format(color[5]),          
    '--verif-text=Validating',
    '--insidewrong-color={}'.format(secondary_color[0]+"aa"),
    '--ringwrong-color={}'.format(secondary_color[0]+"aa"),
    '--wrong-color={}'.format(secondary_color[0]+"aa"),
    '--wrong-text=Wrong!',
    '--keyhl-color={}'.format(color[1]),         
    '--bshl-color={}'.format(color[6]),            
    '--clock',
    '--indicator',       
    '--time-str=%H:%M:%S',
  ])

# Toggle Bar Blur
def toggle_bar_blur(qtile):
  with open(home + '/.config/picom/picom.conf', 'w') as file:
    file.writelines(bar_blur)
  
  qtile.restart()

# Transparent for bars and widgets
transparent="00000000"

## Get network device in use
def get_net_dev():
  get_dev = "echo $(ip route get 8.8.8.8 | awk -- '{printf $5}')"
  ps = subprocess.Popen(get_dev,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
  output = ps.communicate()[0].decode('ascii').strip()
  return(output)

wifi = get_net_dev()

## Get local IP Address
def get_private_ip():
    try:
        ip = socket.gethostbyname(socket.gethostname())
    except socket.gaierror:
        # Alternative method if gethostbyname fails
        ip = get_private_ip_alternative()
    return ip

def get_private_ip_alternative():
    # Using an alternative method to get the private IP address
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # This IP address does not need to be reachable
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

private_ip = get_private_ip()

## Get Public IP Address
def get_public_ip(timeout=2):
    try:
        raw = requests.get('https://api.duckduckgo.com/?q=ip&format=json', timeout=timeout)
        raw.raise_for_status() 
        answer = raw.json()["Answer"].split()[4]
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        return "0.0.0.0"
    except Exception as e:
        print(f"Unexpected error: {e}")
        return "0.0.0.0"
    else:
        return answer
        
public_ip = get_public_ip()

# Call Calendar Notification

def calendar_notification(qtile):{
  subprocess.call(home + '/.local/bin/SOS_Calendar')
}

def calendar_notification_prev(qtile):{
  subprocess.call([home + '/.local/bin/SOS_Calendar', 'prev'])
}

def calendar_notification_next(qtile):{
  subprocess.call([home + '/.local/bin/SOS_Calendar', 'next'])
}
   
## Rofi Widgets

## Set default backend
def set_default_backend(qtile):
  options = backend
  index, key = SOS_Backend.select(' Backend -> ' + def_backend.capitalize() , options)
  if key == -1 or index == 4:
    rofi_left.close()
  else:
    subprocess.run(["wal", light.lower(), "-i", "/usr/local/backgrounds/background.png", "--backend", "%s" %backend[index].lower()])
    subprocess.run(["wpg", light, "-s", "/usr/local/backgrounds/background.png", "--backend", "%s" %backend[index].lower()])
    subprocess.run(["cp", "-r", home + "/.local/share/themes/FlatColor",  "/usr/local/themes/"])
    variables[2]=backend[index] + "\n"
    with open(home + '/.config/qtile/variables', 'w') as file:
      file.writelines(variables)
    qtile.restart()
    subprocess.run(["notify-send","-a", " SpectrumOS", "Color Theme: ", " %s" %backend[index]])

# Display Shortcuts widget
def shortcuts(qtile):
  subprocess.run("cat ~/.shortcuts | rofi -theme '~/.config/rofi/SOS_Shortcuts.rasi' -i -dmenu -p ' Shortcuts:'",shell=True)

# Display Emojis
def emojis(qtile):
  subprocess.run("rofi -modi emoji -show emoji -theme '~/.config/rofi/SOS_Emoji.rasi' -emoji-format {emoji}",shell=True)

# NightLight widget
def nightLight_widget(qtile):
  options = [' Night Time(3500k)', ' Neutral (6500k)', ' Cool (7500k)']
  index, key = SOS_Backend.select('  Night Light', options)
  if key == -1:
    rofi_left.close()
  else:
    if index == 0:
      os.system('redshift -O 3500k -r -P')
      subprocess.run(["notify-send","-a", " SpectrumOS", "Temperature Set to Night Time"])
    elif index == 1:
      os.system('redshift -x')
      subprocess.run(["notify-send","-a", " SpectrumOS", "Temperature Set to Neutral"])
    else:
      os.system('redshift -O 7500k -r -P')
      subprocess.run(["notify-send","-a", " SpectrumOS", "Temperature Set to Cool"])

# Farge Widget
def fargewidget(qtile):
  options = [' Hex',' RGB']
  index, key = SOS_Backend.select('  Color Picker', options)
  if key == -1:
    rofi_left.close()
  else:
    if index ==0:
      subprocess.run("farge --notify --expire-time 20000",shell=True)
    else:
      subprocess.run("farge --notify --rgb --expire-time 20000",shell=True)

# Draw Widget
def draw_widget(qtile):
  options = [' Draw', ' Exit']
  index, key = SOS_Backend.select('  Screen Draw', options)
  if key == -1:
    rofi_left.close()
  else:
    if index ==0:
      subprocess.run("gromit-mpx -a &",shell=True)
      subprocess.run(["notify-send", "-a", " SpectrumOS", "You can Draw Now"])
    else:
      subprocess.run("gromit-mpx -q",shell=True)

# Logout widget
def session_widget(qtile):
  options = ['','󰒲','󰈆', '󰜉','⏻']
  index, key = SOS_Backend.select('  Session', options)
  if key == -1:
    SOS_Backend.close()
  else:
    if index == 0:
      qtile.function(i3lock_colors)
    elif index == 1:
      os.system('systemctl suspend')
    elif index == 2:
      qtile.shutdown()
    elif index == 3:
      os.system('systemctl reboot')
    else:
      os.system('systemctl poweroff')

# Audio widget
def audio_widget(qtile):
  options = [' Input','󰓃 Output']
  index, key = SOS_Audio.select(' 󱡫 Audio Selection:', options)
  if key == -1:
    SOS_Backend.close()
  else:
    if index == 0:
      qtile.spawn(home + '/.local/bin/SOS_Audio source')
    else:
      qtile.spawn(home + '/.local/bin/SOS_Audio sink')

# Network Widget
def network_widget(qtile):
    options = [' Wlan Manager', '  Bandwidth Monitor (CLI)', ' Network Manager (CLI)']
    index, key = SOS_Network.select(f"󱫋 {private_ip} -  {public_ip}", options)
    if key != -1:
        commands = [
            (0, home + '/.local/bin/SOS_Wifi_Menu'),
            (1, "alacritty -e bash -c '. ~/.zshrc; bmon'"),
            (2, "alacritty -e bash -c '. ~/.zshrc; nmtui'")
        ]
        qtile.spawn(commands[index][1])

## Show / Hide all Groups
def show_groups(qtile):
  if hide_unused_groups == True:
    variables[8]=" " + "\n"
    variables[9]="" + "\n"
  else:
    variables[8]="True" + "\n"
    variables[9]="" + "\n"
      
  with open(home + '/.config/qtile/variables', 'w') as file:
    file.writelines(variables)
  qtile.restart()
   
## groups_icon_select
def group_icon(qtile):
  options = [
    '         ', 
    '零 一 二 三 四 五 六 七 八 九',
    '         ',
    '         ',
    '         ',
    '0 1 2 3 4 5 6 7 8 9',
    ': ( ) { : | : & } ;',
    '         ',
    '         ',
    '         ',
    '         ',
    '         ',
    '         ',
    'TERM DEV WWW SYS DOC VIRT MSG MUS VID GFX'
    ]
  index, key = SOS_Panel.select(' Group Icons ', options)
  if key == -1:
    rofi_left.close()
  else:
    variables[10]=str(index) + "\n"
    with open(home + '/.config/qtile/variables', 'w') as file:
      file.writelines(variables)
    qtile.restart()

## Select Dark or Light Theming
def dark_white(qtile):
  options = [' Dark', ' Light']
  index, key = SOS_Backend.select(' Theme -> ' + str(variables[7].strip()), options)
  if key == -1 or index == 2:
    rofi_left.close()
  else:
    if index == 0:
      variables[4]="-c" + "\n"
      variables[7]="Dark" + "\n"
      variables[5]="/.config/qtile/themes/dark" + "\n"
      subprocess.run(['cp', home + '/.config/qtile/themes/dark/' + current_theme + ".py", home + '/.config/qtile/theme.py'])
      subprocess.run(["wal", "-i", "/usr/local/backgrounds/background.png", "--backend", "%s" %def_backend])
      subprocess.run(["wpg", "-s", "/usr/local/backgrounds/background.png", "--backend", "%s" %def_backend])
    else:
      variables[4]="-L" + "\n"
      variables[7]="Light" + "\n"
      variables[5]="/.config/qtile/themes/light" + "\n"
      subprocess.run(['cp', home + '/.config/qtile/themes/light/' + current_theme + ".py", home + '/.config/qtile/theme.py'])
      subprocess.run(["wal", "-l", "-i", "/usr/local/backgrounds/background.png", "--backend", "%s" %def_backend])
      subprocess.run(["wpg", "-L", "-A", "-s", "/usr/local/backgrounds/background.png", "--backend", "%s" %def_backend])

    subprocess.run(["cp", "-r", home + "/.local/share/themes/FlatColor",  "/usr/local/themes/"])
    with open(home + '/.config/qtile/variables', 'w') as file:
      file.writelines(variables)
    qtile.restart()
    subprocess.run(["notify-send","-a", " SpectrumOS", "Theme changed to: ", "%s" %options[index]])


## Select Bar Position Top or Bottom
def bar_pos(qtile):
  options = ['Top', 'Bottom', 'Toggle Bar']
  index, key = SOS_Backend.select(' Bar -> ' + bar_position , options)
  if key == -1:
    rofi_left.close()
  else:
    if index == 0:
      variables[6]="top" + "\n"
      subprocess.run(["cp", "-r", home + "/.local/share/themes/FlatColor",  "/usr/local/themes/"])
      with open(home + '/.config/qtile/variables', 'w') as file:
        file.writelines(variables)
      qtile.restart()
    elif index == 1:
      variables[6]="bottom" + "\n"
      subprocess.run(["cp", "-r", home + "/.local/share/themes/FlatColor",  "/usr/local/themes/"])
      with open(home + '/.config/qtile/variables', 'w') as file:
        file.writelines(variables)
      qtile.restart()
    else:
      qtile.hide_show_bar()

# Change Theme widget
def change_theme(qtile):
  options = theme
  index, key = SOS_Themes.select('  Theme -> ' + current_theme , options)
  if key == -1:
    rofi_left.close()
    subprocess.run(["notify-send","-a", " SpectrumOS", "No Theme Selected!"])
  else:
    subprocess.run('rm -rf ~/.config/qtile/theme.py', shell=True)
    variables[1]=theme[index] + "\n"
    new_theme=theme[index] + ".py"
    subprocess.run(['cp', themes_dir + "/" + new_theme, home + '/.config/qtile/theme.py'])
    with open(home + '/.config/qtile/variables', 'w') as file:
      file.writelines(variables)
    qtile.restart()
    subprocess.run(["notify-send","-a", " SpectrumOS", " Theme: ", "%s" %theme[index]])

# Screenshot widget
def screenshot(qtile):
  options = [' Area', ' Screen', ' Window',  ' 5s Screen']
  index, key = SOS_Backend.select('  Screenshot', options)
  if key == -1:
    rofi_left.close()
  else:
    if index ==0:
      subprocess.run("flameshot gui --path ~/Pictures/area_screenshot.png --delay 400",shell=True)
    elif index==1:
      subprocess.run("flameshot full --path ~/Pictures/Screenshot.png --delay 500",shell=True)
    elif index==2:
      subprocess.run("scrot -u 'window_screenshot.png' -e 'mv $f ~/Pictures/ #; feh -F ~/Pictures/$f' && notify-send -a 'flameshot' 'Window Picture Taken!'",shell=True)
    else:
      subprocess.run("flameshot full --path ~/Pictures/Screenshot.png --delay 5000",shell=True)

# Popup Widgets
def show_chords(qtile):
    controls = [
        PopupWidget(
            widget=widget.Chord(
              background=color[0],
              foreground=color[1],
            ),
            width=1,
            height=1,
        )
    ]

    layout = PopupRelativeLayout(
        qtile,
        pos_x=0.8,
        pos_y=0.8,
        width=100,
        height=50,
        controls=controls,
        background=color[0],
        initial_focus=None,
        close_on_click=False,
        hide_on_mouse_leave=True,
        keyboard_navigation=True,
    )
    layout.show(centered=True)

def hide_chords(qtile):
    if hasattr(qtile, 'current_popup'):
        qtile.current_popup.hide()
        del qtile.current_popup

## Support SpectrumOS
def support_spectrumos(qtile):
  options = [' Become a Patreon', ' Buy me a Coffee']
  index, key = SOS_Backend.select(' Support SpectrumOS', options)
  if key == -1 or index == 2:
    rofi_left.close()
  else:
    if index == 0:
      subprocess.run(["xdg-open", "https://www.patreon.com/user?u=48005915"])
    else:
      subprocess.run(["xdg-open", "https://www.buymeacoffee.com/gibranlp"])
    
    subprocess.run(["notify-send","-a", " SpectrumOS", "Thanks for supporting SpectrumOS"])

# Control Panel Widget
def control_panel(qtile):
  options = [
    ' Wallpaper Options',#0
    '     Set Random Wallpaper (⎇ + R)',
    '     Select Wallpaper (❖ +  + R)',
    ' Theme Options',#3
    '     Set Color Scheme (⎇ +  + i)',
    '     Dark/Light Theme (❖ + D)',
    ' Bar Options',#6
    '     Bar Position (❖ +  + I)',
    '     Change Bar Theme (⎇ + i)',
    '    %s Toggle Bar Blur' %blur_icon,
    '    %s Toggle Groups' %str(variables[9].strip()),
    '     Change Groups Icons',
    ' Tools',#12
    '     Find / Open Files (❖ + F)',
    '     Todo List (⎇ + L)',
    '     Apps as Sudo (⎇ +  + )',
    '     Calculator (❖ + C)',
    '     Network Manager (❖ + B)',
    '     Screenshot (prtnsc)',
    '     Monitor Temperature (❖ +  + O)',
    '     Monitor Layout (❖ +  + X)',
    '     Bluetooth Manager (❖ + T)',
    ' Miscelaneous',#23
    '     Screen Draw (❖ +  + P)',
    '     Pick Color (❖ + P)',
    '     View Shortcuts (❖ +  + z)',
    '     Emojis ( +  + )',
    '     System Cleaner',
    ' Session Menu (❖ + X)',
    ' Support SpectrumOS',    
    ]
    
  index, key = SOS_Panel.select('  Control Panel', options)
  if key == -1:
    SOS_Panel.close()
  else:
    if index == 1:
      qtile.run(home + '/.local/bin/SOS_Wallpaper')
    elif index == 2:
      qtile.spawn(home + '/.local/bin/SOS_Select_Wallpaper')
    elif index == 4:
      qtile.function(set_default_backend)
    elif index == 5:
      qtile.function(dark_white)
    elif index == 7:
      qtile.function(bar_pos)
    elif index == 8:
      qtile.function(change_theme)
    elif index == 9:
      qtile.function(toggle_bar_blur) 
    elif index == 10:
      qtile.function(show_groups)
    elif index == 11:
      qtile.function(group_icon)
    elif index == 13:
      subprocess.run(home + '/.local/bin/SOS_Search')
    elif index == 14:
      qtile.spawn('rofi -modi TODO:~/.local/bin/SOS_Todo -show TODO -theme ~/.config/rofi/SOS_Todo.rasi')
    elif index == 15:
      qtile.spawn('sudo rofi -show drun -show-icons -theme "~/.config/rofi/SOS_Launcher.rasi"')
    elif index == 16:
      subprocess.run(home + '/.local/bin/SOS_Calculator')
    elif index == 17:
      qtile.function(network_widget)
    elif index == 18:
      qtile.function(screenshot)
    elif index == 19:
      qtile.function(nightLight_widget)
    elif index == 20:
      subprocess.run(home + '/.local/bin/SOS_Multimonitor')
    elif index == 21:
      subprocess.run(home + '/.local/bin/SOS_Bluetooth')
    elif index == 23:
      qtile.function(draw_widget)
    elif index == 24:
      qtile.function(fargewidget)
    elif index == 25:
      qtile.function(shortcuts)
    elif index == 26:
      qtile.function(emojis)
    elif index == 27:
      qtile.spawn(home + '/.local/bin/SOS_Clean_System')
    elif index == 28:
      qtile.function(session_widget)
    elif index == 29:
      qtile.function(support_spectrumos)

# Own Widgets

class WifiText(widget.GenPollText):
    defaults = [
        ('update_interval', 5, 'Update interval in seconds'),
    ]

    def __init__(self, **config):
        widget.GenPollText.__init__(self, func=self.poll, **config)
        self.add_defaults(WifiText.defaults)

    def poll(self):
        signal_strength = self.get_wifi_signal_strength()
        return self.select_text(signal_strength)

    def get_wifi_signal_strength(self):
        try:
            # Get the Wi-Fi signal strength using nmcli
            result = subprocess.run(
                ["nmcli", "-t", "-f", "ACTIVE,SIGNAL", "dev", "wifi"],
                stdout=subprocess.PIPE,
                text=True
            ).stdout

            # Find the line with ACTIVE:yes, which means the connected network
            active_wifi = [line for line in result.split('\n') if 'yes' in line]
            if active_wifi:
                signal_strength = int(active_wifi[0].split(':')[-1])
                return signal_strength
        except Exception as e:
            return 0
        
    def select_text(self, signal_strength):
        if signal_strength >= 75:
            text = ''
        elif signal_strength >= 50:
            text = ''
        elif signal_strength >= 25:
            text = ''
        elif signal_strength > 0:
            text = ''
        else:
            text = ''
        
        return text
