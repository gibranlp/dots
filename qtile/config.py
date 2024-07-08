# _____             _                 _____ _____ 
#|   __|___ ___ ___| |_ ___ _ _ _____|     |   __|
#|__   | . | -_|  _|  _|  _| | |     |  |  |__   |
#|_____|  _|___|___|_| |_| |___|_|_|_|_____|_____|
#      |_|   
# SpectrumOS - Embrace the Chromatic Symphony!
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence
#

from theme import *

#### Keys ####

keys = [
    # Qtile System Actions
    Key([mod], "t", lazy.layout.spawn_split(terminal, "x")),
    Key([mod, "shift"], "t", lazy.layout.spawn_split(terminal, "y")),
    Key([mod, "shift"], "r",lazy.restart()),
    Key([mod, "shift"], "q",lazy.shutdown()),
    Key([mod], "q",lazy.window.kill()), # Close Window
    Key([mod], "r", lazy.spawncmd()), # Launch Prompt

    # SpectrumOS
    Key([mod], "Return", lazy.layout.spawn_split(rofi_launcher, "x")), # Open Rofi launcher on X split
    Key([mod, "shift"], "Return", lazy.layout.spawn_split(rofi_launcher, "y")), # Open Rofi launcher on Y split

    Key([alt], "r",lazy.spawn(home + '/.local/bin/SOS_Wallpaper')), # Set random wallpaper

    # Rofi Widgets
    Key([alt],"l",lazy.spawn('rofi -modi TODO:~/.local/bin/SOS_Todo -show TODO -theme ~/.config/rofi/left.rasi')),# Todo Manager

    Key([mod],"b",lazy.function(network_widget)), # Network Settings
    Key([mod],"f",lazy.function(dark_white)), # Select Dark or Light Theme
    Key([mod, "Shift"],"z",lazy.function(shortcuts)), # Shortcuts widget  
    Key([alt, "shift"],"w",lazy.function(bar_pos)), # Set bar position
    Key([mod, "shift"],"o",lazy.function(nightLight_widget)), # Set night light
    Key(["control", "shift"], "Return", lazy.function(emojis)), # Open Rofi Emojis
    Key([mod],"p",lazy.function(fargewidget)), # Color Picker Widget
    Key([mod, "shift"],"p",lazy.function(draw_widget)), # Desktop draw widget
    Key([alt], "Return", lazy.function(control_panel)), # Search for files and folders
    Key([mod],"x",lazy.function(session_widget)), # Log out
    Key([mod, "shift"],"w",lazy.function(set_default_backend)), # Set Default Color Scheme
    Key([mod],"w",lazy.function(change_theme)), # Change Theme


    Key([mod], "n", lazy.spawn(home + '/.local/bin/SOS_Notes')), # Notes Widget
    Key([alt, "shift"], "r",lazy.spawn(home + '/.local/bin/SOS_Select_Wallpaper')), # Select Wallpaper
    Key([mod],"c",lazy.spawn(home + '/.local/bin/SOS_Calculator')), # Calculator Widget
    Key([alt],"w",lazy.spawn(home + '/.local/bin/SOS_Search')),# Find Files
    Key([mod, "shift"], "b", lazy.spawn(home + '/.local/bin/SOS_Bluetooth')), # Bluetooth widget
    Key([mod, "shift"],"x",lazy.spawn(home + '/.local/bin/SOS_Multimonitor')),# Monitor modes Widget
    
    #Sudo
    Key([alt, "shift"], "Return", lazy.spawn('sudo rofi -show drun -show-icons -theme "~/.config/rofi/SOS_Launcher.rasi"')), # Open Rofi launcher as Sudo

    # Apps
    Key([mod],"e",lazy.spawn('thunar')),# Thunar

    # Layout Focus
    Key([mod], "i", 
        lazy.layout.up()
    ),
    Key([mod], "j", 
        lazy.layout.left()
    ),
    Key([mod], "k", 
        lazy.layout.down()
    ),
    Key([mod], "l", 
        lazy.layout.right()
    ),

    # Layout Resize
    Key([mod, "shift"], "i", 
        lazy.layout.resize("up", 30)
    ),
    Key([mod, "shift"], "j", 
        lazy.layout.resize("left", 30)
    ),
    Key([mod, "shift"], "k", 
        lazy.layout.resize("down", 30)
    ),
    Key([mod, "shift"], "l", 
        lazy.layout.resize("right", 30)
    ),

    # Layout swap
    Key([alt], "i", 
        lazy.layout.swap("up")
    ),
    Key([alt], "j", 
        lazy.layout.swap("left")
    ),
    Key([alt], "k", 
        lazy.layout.swap("down")
    ),
    Key([alt], "l", 
        lazy.layout.swap("right")
    ),

    # Layout Push
    Key([alt, "shift"], "i", 
        lazy.layout.push_in("up")
    ),
    Key([alt, "shift"], "j", 
        lazy.layout.push_in("left")
    ),
    Key([alt, "shift"], "k", 
        lazy.layout.push_in("down")
    ),
    Key([alt, "shift"], "l", 
        lazy.layout.push_in("right")
    ),

    # Layout merge tabs
    Key([mod], "Tab", 
        lazy.layout.next_tab()
    ),
    Key([mod, "shift"], "Tab", 
        lazy.layout.merge_tabs("previous")
    ),
    
    # Pull out to tab
    Key([alt], "Tab",
        lazy.layout.pull_out_to_tab(),
    ),
    
    Key([alt, "shift"], "Tab", 
        lazy.layout.shuffle_down(),
        lazy.layout.swap_right()
        ), # Swap Right Up
    
    Key([mod], 'period', lazy.next_screen()), # Send Cursor to next screen

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("sudo xbacklight -inc 5")), # Aument Brightness
    Key(["control", alt], "p", lazy.spawn("sudo xbacklight -inc 5")), # Aument Brightness
    Key([], "XF86MonBrightnessDown", lazy.spawn("sudo xbacklight -dec 5")), # Lower Brightness
    Key(["control", alt], "o", lazy.spawn("sudo xbacklight -dec 5")),

    # Volume
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")), # Mute
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 2%- && dunstify -a Volume ' '$(pamixer --get-volume-human) -h int:value:$(pamixer --get-volume)", shell=True)),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 2%+ && dunstify -a Volume ' '$(pamixer --get-volume-human) -h int:value:$(pamixer --get-volume)", shell=True)), # Raise Volume

    # Media Control
    Key([], "XF86AudioPlay", lazy.spawn("playerctl --player=%any play-pause")), # Play Pause
    Key([], "XF86AudioNext", lazy.spawn("playerctl --player=%any next")), # Next song
    Key([], "XF86AudioPrev", lazy.spawn("playerctl --player=%any previous")), # Previous Song

    # Window hotkeys
    Key([alt], "f", lazy.window.toggle_fullscreen()), # Toggle Current window ;n
    Key([alt, "shift"], "f", lazy.window.toggle_floating()), # Toggle current window floating
    Key([mod], "space", lazy.next_layout()), # Cycle layouts

    # Keyboard
    Key([alt], "space", lazy.widget["keyboardlayout"].next_keyboard()), # Change Keyboard Layout

    # Screenshots
    Key([], "Print", lazy.function(screenshot)),

    # Lock Screen
    Key(["control", alt],"l",lazy.function(i3lock_colors)), # Run i3lock 

    # Dunst Shortuts
    Key(["control"], "space",  lazy.spawn("dunstctl close")), # Clear Last Notification
    Key(["control", "shift"], "space",  lazy.spawn("dunstctl close-all")), # Clear All Notifications
    Key(["control", "shift"], "n",  lazy.spawn("dunstctl  history-pop")), # Show Notificaction history

    # Kill window            
    Key([alt], "Escape", lazy.spawn('xkill')), # Click window to close

    # Scratchpads
    Key(["shift"], 'F12', lazy.group['scratchpad'].dropdown_toggle("music")),
    Key(["control","shift"], 'F12', lazy.group['scratchpad'].dropdown_toggle("lyrics")),
    Key([alt], 'F12', lazy.group['scratchpad'].dropdown_toggle("htop")),
    Key([alt], 'F11', lazy.group['scratchpad'].dropdown_toggle("weather")),

    # Show Keyboard Layouts
    Key([mod],"g",lazy.function(show_keyboard_layout)), # Run i3lock 
]

##### Groups ####

#Labels
labels = {
    0: ["","","","","","","","","",""], # SpectrumOS
    1: ["零","一","二","三","四","五","六","七","八","九"], # Kanji Numbers
    2: ["","","","","","","","","",""], # Custom
    3: ["","","","","","","","","",""], # Star Wars
    4: ["","","","","","","","","",""], # Chess
    5: ["0","1","2","3","4","5","6","7","8","9"], # Numbers
    6: [":","(",")","{",":","|",":","&","}",";"], # Fork Bomb
    7: ["","","","","","","","","",""], # Circles
    8: ["","","","","","","","","",""], # Squares
    9: ["","","","","","","","","",""], # Triangles
    10: ["","","","","","","","","",""], # Hexagons
    11: ["","","","","","","","","",""], # Rectangles
    12: ["","","","","","","","","",""], # Square Ring
    13: ["TERM","DEV","WWW","SYS","DOC","VIRT","MSG","MUS","VID","GFX"] # Custom Labels
}

selected_label = int(variables[10])
group_labels = labels.get(selected_label, [])


group_layouts=["bonsai", "bonsai", "bonsai", "bonsai", "bonsai", "bonsai", "bonsai", "bonsai", "bonsai", "bonsai"]
for i in range(len(group_names)):
  groups.append(
    Group(
      name=group_names[i],
      layout=group_layouts[i].lower(),
      label=group_labels[i],
  ))
for i in groups:
    keys.append(Key([mod], i.name, lazy.group[i.name].toscreen()))
    keys.append(Key([mod, 'shift'], i.name, lazy.window.togroup(i.name)))

# Scratchpads

groups.append(ScratchPad("scratchpad", [
   DropDown("lyrics", "alacritty -e bash -c '. ~/.zshrc; lyrics'",
      x=0.75, y=0.05, width=0.20, height=0.9, opacity=0.9,
      on_focus_lost_hide=False),

   DropDown("music", "alacritty -e bash -c '. ~/.zshrc; cmus'",
      x=0.05, y=0.0, width=0.9, height=0.7, opacity=0.9,
      on_focus_lost_hide=False),
               
   DropDown("htop", "alacritty -e bash -c '. ~/.zshrc; htop'",
      x=0.05, y=0.0, width=0.9, height=0.7, opacity=0.9,
      on_focus_lost_hide=False),            
               
                      ]),
          )

## Layouts
def init_layout_theme():
  return {
    "font":main_font,
    "fontsize":font_size,
    "margin":layout_margin,
    "border_on_single":False,
    "border_width":layout_border_width,
    "border_normal":color[0],
    "border_focus":color[2],
    "single_margin":single_layout_margin,
    "single_border_width":single_border_width,
    "change_ratio":0.01,
    "new_client_position":'bottom',
   }

layout_theme = init_layout_theme()

def init_layouts():
  return [
   Bonsai(
      **{
         "window.border_size": layout_border_width,
         "window.margin":layout_margin,
         "window.border_color": color[0],
         "window.active.border_color": color[1],
         "window.default_add_mode": "match_previous",
         "auto_cwd_for_terminals": False,
         "tab_bar.height": 10,
         "tab_bar.bg_color": color[0],
         "tab_bar.tab.padding": 0,
         "tab_bar.tab.bg_color": color[3],
         "tab_bar.tab.fg_color": color[3],
         "tab_bar.tab.font_family": main_font,
         "tab_bar.tab.font_size": font_size,
         "tab_bar.tab.active.bg_color": color[7],
         "tab_bar.tab.active.fg_color": color[7],
         "tab_bar.margin": [2,5,0,5],
      }),
 ]
layouts = init_layouts()

floating_layout = layout.Floating(
    border_width=layout_border_width,
    border_normal=color[0],
    border_focus=color[2],
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(title="Xephyr"), # lightdm testing
    ]
)

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

wmname = "LG3D"