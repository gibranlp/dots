# _____             _                 _____ _____ 
#|   __|___ ___ ___| |_ ___ _ _ _____|     |   __|
#|__   | . | -_|  _|  _|  _| | |     |  |  |__   |
#|_____|  _|___|___|_| |_| |___|_|_|_|_____|_____|
#      |_|   
# SpectrumOS - Embrace the Chromatic Symphony!
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence 
#
from functions import *
from custom_widgets import InternetIcon, TemperatureIcon, VolumeIcon

widget_defaults = dict(
  font=main_font,
  fontsize=font_size,
  padding=4,
)
# Theme

## Screens
def init_widgets_list():
  widgets_list = [
    widget.LaunchBar(
      background=secondary_color[0],
      fontsize=font_size+3,
      progs=[
        ('<span color="#ffffff"></span>', 'firefox https://www.github.com', 'Github'),
        ('<span color="#0c5274">󰸉</span>', 'firefox https://wallhaven.cc/', 'Wallhaven'),
        ('<span color="#ff0000"></span>', 'firefox https://www.youtube.com', 'Youtube'),
        ('<span color="#ffe600"></span>', 'firefox https://mercadolibre.com.mx/', 'MercadoLibre'),
        ('<span color="#ff4500">󰑍</span>', 'firefox https://reddit.com/', 'Reddit'),
        ]
    ),

    widget.Spacer(
      length=4,
      background=transparent,
    ),
    
    widget.GroupBox(
      background=color[1],
      fontsize=groups_font,
      disable_drag=True,
      hide_unused=hide_unused_groups,
      borderwidth=0,
      active=third_color[1], #Program opened in that group
      inactive=secondary_color[0], # Empty Group
      rounded=False,
      highlight_method="block",
      this_current_screen_border=secondary_color[0],
      center_aligned = True,
      other_curren_screen_border=secondary_color[0],   
      urgent_border="fc0000",
      block_highlight_text_color=color[1],
    ),

    widget.Spacer(
      length=4,
      background=transparent,
    ),
    
    widget.Chord(
      background=secondary_color[0],
      foreground=color[3],
    ),
    
    widget.Prompt(
      background=secondary_color[0],
      prompt=prompt,
      foreground=secondary_color[4],
      cursor_color=secondary_color[4],
      visual_bell_color=[4],
      visual_bell_time=0.2,
    ),
    
    widget.Spacer(
      length=bar.STRETCH,
    ),

    widget.Clipboard(
      background=color[6],
      selection='CLIPBOARD',
      foreground=secondary_color[0],
      width=widget_width -20,
      scroll=True,
      scroll_repeat=True,
      scroll_interval=0.1,
      scroll_step=1,
      update_interval=1,
      timeout=5,
    ),

    widget.Spacer(
      length=4,
      background=transparent,
    ),

    widget.Visualiser(
       bar_colour=color[1],
       bars=12,
       framerate=60,
       hide=True,
    ),

    widget.Spacer(
      length=4,
      background=transparent,
    ),

    widget.CheckUpdates(
       background=color[1],
       distro='Arch_paru',
       colour_have_updates=color[0],
       colour_no_updates=color[0],
       display_format='󰁠',
       no_update_string='󱧧',
       update_interval=60,
       execute='paru -Syu',
       fontsize=font_size+3,
       mouse_callbacks={'Button1': lambda: qtile.spawn(terminal + " -e zsh -c 'source ~/.zshrc && paru -Syu --noconfirm; exec zsh'")},
    ),

    widget.Spacer(
      length=4,
      background=transparent,
    ),

    TemperatureIcon(
       fontsize=font_size+3,
       background=color[5],
       foreground=color[0],
       mouse_callbacks = {'Button1': lambda: qtile.spawn(terminal + " -e zsh -c 'source ~/.zshrc && sensors; exec zsh'")},
       update_interval=1, 
       tag_sensor='CPUTIN',
    ),
    
    widget.ThermalSensor(
      background=color[5],
      format='{temp:.1f}{unit}',
      foreground=color[0],
      tag_sensor='CPUTIN',
      mouse_callbacks = {'Button1': lambda: qtile.spawn(terminal + " -e zsh -c 'source ~/.zshrc && sensors; exec zsh'")},
      update_interval=1,
    ),

    widget.Spacer(
      length=4,
      background=transparent,
    ),

    widget.TextBox(
       background=color[2],
       text="",
       foreground=color[0],
       mouse_callbacks={'Button1': lambda: qtile.spawn(terminal + " -e zsh -c 'source ~/.zshrc && htop'")},
       fontsize=font_size+3,
    ),
    
    widget.CPU(
      background=color[2],
      format='{load_percent}%',
      foreground=color[0],
      mouse_callbacks={'Button1': lambda: qtile.spawn(terminal + " -e zsh -c 'source ~/.zshrc && htop'")},
    ),

    widget.Spacer(
      length=4,
      background=transparent,
    ),

    widget.TextBox(
       background=color[3],
       font=symbols_font,
       text="",
       foreground=color[0],
       mouse_callbacks={'Button1': lambda: qtile.spawn(terminal + " -e zsh -c 'source ~/.zshrc && htop'")},
       fontsize=font_size,
    ),
    
    widget.Memory(
      background=color[3],
      measure_mem='M',
      format='{MemUsed: .0f}{mm}',
      foreground=color[0],
      mouse_callbacks={'Button1': lambda: qtile.spawn(terminal + " -e zsh -c 'source ~/.zshrc && htop'")},
    ),

    widget.Spacer(
      length=4,
      background=transparent,
    ),

    widget.TextBox(
       background=color[4],
       text="󰟜",
       foreground=color[0],
      mouse_callbacks={'Button1': lambda: qtile.spawn(terminal + " -e zsh -c 'source ~/.zshrc && df -hi; exec zsh'")},
      fontsize=font_size+3,
    ),
    
    widget.DF(
      background=color[4],
      format='{p} ({uf}{m})',
      partition='/',
      foreground=color[0],
      measure='G',
      visible_on_warn=False,
      mouse_callbacks={'Button1': lambda: qtile.spawn(terminal + " -e zsh -c 'source ~/.zshrc && df -hi; exec zsh'")},
    ),

    widget.Spacer(
      length=4,
      background=transparent,
    ),

    widget.Wttr(
      background=secondary_color[1],
      foreground=color[0],
      location={'': ''},
      update_interval=300,
      format='%c %t',
      mouse_callbacks={'Button1': lambda: qtile.spawn(terminal + " -e zsh -c 'curl wttr.in; exec zsh'")},
    ),

    widget.Spacer(
      length=4,
      background=transparent,
    ),
    
    InternetIcon(
      background=color[6],
      font=symbols_font,
      update_interval=1,
      foreground=color[0],
      fontsize=font_size+3,
      mouse_callbacks={'Button1':lambda: qtile.function(network_widget)}
    ),
    
    widget.Wlan(
      background=color[6],
      interface=wifi,
      format='{essid}',
      disconnected_message='󰱟',
      foreground=color[0],
      width=widget_width -20,
      scroll=True,
      scroll_repeat=True,
      scroll_interval=0.1,
      scroll_step=1,
      update_interval=1,
      mouse_callbacks={'Button1':lambda: qtile.function(network_widget)}
    ),
    
    widget.Net(
      background=color[6],
      prefix='M',
      interface=wifi,
      format='{down:1.1f}',
      foreground=color[0],
      use_bits=True,
      mouse_callbacks={'Button1':lambda: qtile.function(network_widget)},
    ),

    widget.Spacer(
      length=4,
      background=transparent,
    ),

    widget.TextBox(
       fontsize=font_size+3,
       background=secondary_color[2],
       text="󰂯",
       foreground=color[0],
       mouse_callbacks={'Button1': lambda: qtile.spawn(home + '/.local/bin/SOS_Bluetooth')},
    ),

    widget.Bluetooth(
      background=secondary_color[2],
      foreground=color[0],
      format='Adapter: {name} [{powered}{discovery}]',
      default_text='{connected_devices}',
      device_format='Device: {name}{battery_level} [{symbol}]',
      device_battery_format=' ({battery}%)',
      width=widget_width,
      scroll=True,
      scroll_repeat=True,
      scroll_interval=0.1,
      scroll_step=1,
      update_interval=1,
      mouse_callbacks={'Button1': lambda: qtile.spawn(home + '/.local/bin/SOS_Bluetooth')},
      scroll_fixed_width=False,
      default_show_battery=True,
    ),

    widget.Spacer(
      length=4,
      background=transparent,
    ),

    VolumeIcon(
       background=secondary_color[5],
       foreground=color[0],
       mouse_callbacks={'Button1': lambda: qtile.function(audio_widget),'Button4': lambda: qtile.spawn("amixer -q set Master 5%+ && dunstify -a Volume ' '$(pamixer --get-volume-human) -h int:value:$(pamixer --get-volume)", shell=True),'Button5': lambda: qtile.spawn("amixer -q set Master 5%- && dunstify -a Volume ' '$(pamixer --get-volume-human) -h int:value:$(pamixer --get-volume)", shell=True)},
    ),

    widget.Spacer(
      length=4,
      background=transparent,
    ),

    widget.Clock(
      background=secondary_color[3],
      foreground=color[0],
      format="%a %d %H:%M",
      update_interval=1,
      mouse_callbacks={'Button1': lambda: qtile.function(calendar_notification),'Button4': lambda: qtile.function(calendar_notification_prev),'Button5': lambda: qtile.function(calendar_notification_next)},              
    ),

    widget.Spacer(
      length=4,
      background=transparent,
    ),
    widget.StatusNotifier(
      decorations=[RectDecoration(colour=secondary_color[1], radius=5, filled=True)],
    ),

    widget.Spacer(
      length=4,
      background=transparent,
    ),

    widget.UPowerWidget(
      background=secondary_color[0],
      border_charge_colour=secondary_color[7],
      border_colour=secondary_color[3],
      border_critical_colour='#cc0000',
      fill_critical='#cc0000',
      fill_low='#FF5511',
      fill_normal=secondary_color[3],
      foreground=secondary_color[3],
      percentage_critical=0.2,
      percentage_low=0.4,
      text_charging=' ({percentage:.0f}%) {ttf} to ',
      text_discharging=' ({percentage:.0f}%) {tte} Left',
    ),
    ]
  return widgets_list

def screen1_widgets():
    widgets_screen1=init_widgets_list()
    return widgets_screen1

def init_screens_bottom():
    return[Screen(bottom=bar.Bar(widgets=screen1_widgets(),size=bar_size,background=transparent,margin=[bar_margin[0], bar_margin[1],bar_margin[2],bar_margin[3]]))]

def init_screens_top():
    return[Screen(top=bar.Bar(widgets=screen1_widgets(),size=bar_size,background=transparent,margin=[bar_margin[0], bar_margin[1],bar_margin[2],bar_margin[3]]))]

if bar_position == "top":
    screens=init_screens_top()
else:
  screens=init_screens_bottom()

widgets_list = init_widgets_list()
widgets_screen1 = screen1_widgets()