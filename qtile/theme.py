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
    widget.Mpris2(
      decorations=[RectDecoration(colour=secondary_color[1], radius=5, filled=True)],
      mouse_callbacks={'Button1': lazy.group['scratchpad'].dropdown_toggle("music")},
      objname=None,
      foreground=secondary_color[0],
      width=350,
      format='󰠃 {xesam:artist} 󰀥 {xesam:album} 󰎇 {xesam:title}',
      stopped_text="Stop",
      paused_text='  ',
      scroll=True,
      scroll_repeat=True,
      scroll_delay=0.1,
    ),

    widget.Spacer(
      length=bar.STRETCH,
      background=transparent,
    ),

    widget.TextBox(
      decorations=[RectDecoration(colour=secondary_color[3], radius=[5,0,0,5], filled=True)],
      text="󰒮",
      foreground=secondary_color[0],
      mouse_callbacks={'Button1': lambda: qtile.spawn("playerctl --player=%any previous")},
      font=symbols_font,
      fontsize=font_size+3,

    ),

    widget.Visualizer(
      decorations=[RectDecoration(colour=secondary_color[3], radius=0, filled=True)],
      bar_colour=secondary_color[0],
      hide=True,
      bars=30,
      framerate=60,
      spacing=2,
      width=300,
      channels='stereo',
      mouse_callbacks={'Button1': lazy.group['scratchpad'].dropdown_toggle("music")},
    ),

    widget.TextBox(
      decorations=[RectDecoration(colour=secondary_color[3], radius=[0,5,5,0], filled=True)],
      text="󰒭",
      foreground=secondary_color[0],
      mouse_callbacks={'Button1': lambda: qtile.spawn("playerctl --player=%any next")},
      font=symbols_font,
      fontsize=font_size+3,
    ),

    widget.Spacer(
      length=bar.STRETCH,
      background=transparent,
    ),

    InternetIcon(
      decorations=[RectDecoration(colour=secondary_color[4], radius=5, filled=True)],
      update_interval=1,
      foreground=secondary_color[0],
      fontshadow=secondary_color[1],
      font=symbols_font,
      mouse_callbacks={'Button1':lambda: qtile.function(network_widget)}
    ),

    widget.Spacer(
      length=5,
      background=transparent,
    ),

    VolumeIcon(
      decorations=[RectDecoration(colour=secondary_color[2], radius=5, filled=True)],
      foreground=secondary_color[0],
      fontshadow=secondary_color[1],
      mouse_callbacks={'Button1': lambda: qtile.function(audio_widget),'Button4': lambda: qtile.spawn("amixer -q set Master 5%+ && dunstify -a Volume ' '$(pamixer --get-volume-human) -h int:value:$(pamixer --get-volume)", shell=True),'Button5': lambda: qtile.spawn("amixer -q set Master 5%- && dunstify -a Volume ' '$(pamixer --get-volume-human) -h int:value:$(pamixer --get-volume)", shell=True)},
    ),

    widget.Spacer(
      length=5,
      background=transparent,
    ),

    widget.UPowerWidget(
      border_charge_colour=secondary_color[7],
      border_colour=secondary_color[0],
      border_critical_colour='#cc0000',
      fill_critical='#cc0000',
      fill_low='#FF5511',
      fill_normal=secondary_color[0],
      foreground=secondary_color[0],
      percentage_critical=0.2,
      percentage_low=0.4,
      text_charging=' ({percentage:.0f}%) {ttf} to ',
      text_discharging=' ({percentage:.0f}%) {tte} Left',
      fontshadow=secondary_color[1],
    ),
    
    widget.Spacer(
      length=5,
      background=transparent,
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