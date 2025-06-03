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
     widget.TextBox(
      text='Darker',
      foreground=third_color[1],
      background=third_color[0]
     ),
    widget.TextBox(
      text='0',
      foreground=third_color[1],
      background=third_color[0]
      ),
    widget.TextBox(
      text='1',
      foreground=third_color[0],
      background=third_color[1]
      ),
    widget.TextBox(
      text='2',
      foreground=third_color[0],
      background=third_color[2]
    ),
    widget.TextBox(
      text='3',
      foreground=third_color[0],
      background=third_color[3]
    ),
    widget.TextBox(
      text='4',
      foreground=third_color[0],
      background=third_color[4]
    ),
    widget.TextBox(
      text='5',
      foreground=third_color[0],
      background=third_color[5]
    ),
    widget.TextBox(
      text='6',
      foreground=third_color[0],
      background=third_color[6]
    ),
    widget.TextBox(
      text='7',
      foreground=third_color[0],
      background=third_color[7]
    ),
    widget.TextBox(
      text='8',
      foreground=third_color[0],
      background=third_color[8]
    ),
    widget.TextBox(
      text='Normal',
      foreground=color[1],
      background=color[0]
     ),
    widget.TextBox(
      text='0',
      foreground=color[1],
      background=color[0]
      ),
    widget.TextBox(
      text='1',
      foreground=color[0],
      background=color[1]
      ),
    widget.TextBox(
      text='2',
      foreground=color[0],
      background=color[2]
    ),
    widget.TextBox(
      text='3',
      foreground=color[0],
      background=color[3]
    ),
    widget.TextBox(
      text='4',
      foreground=color[0],
      background=color[4]
    ),
    widget.TextBox(
      text='5',
      foreground=color[0],
      background=color[5]
    ),
    widget.TextBox(
      text='6',
      foreground=color[0],
      background=color[6]
    ),
    widget.TextBox(
      text='7',
      foreground=color[0],
      background=color[7]
    ),
    widget.TextBox(
      text='8',
      foreground=color[0],
      background=color[8]
    ),
    widget.TextBox(
      text='Light',
      foreground=secondary_color[1],
      background=secondary_color[0]
     ),
    widget.TextBox(
      text='0',
      foreground=secondary_color[1],
      background=secondary_color[0]
      ),
    widget.TextBox(
      text='1',
      foreground=secondary_color[0],
      background=secondary_color[1]
      ),
    widget.TextBox(
      text='2',
      foreground=secondary_color[0],
      background=secondary_color[2]
    ),
    widget.TextBox(
      text='3',
      foreground=secondary_color[0],
      background=secondary_color[3]
    ),
    widget.TextBox(
      text='4',
      foreground=secondary_color[0],
      background=secondary_color[4]
    ),
    widget.TextBox(
      text='5',
      foreground=secondary_color[0],
      background=secondary_color[5]
    ),
    widget.TextBox(
      text='6',
      foreground=secondary_color[0],
      background=secondary_color[6]
    ),
    widget.TextBox(
      text='7',
      foreground=secondary_color[0],
      background=secondary_color[7]
    ),
    widget.TextBox(
      text='8',
      foreground=secondary_color[0],
      background=secondary_color[8]
    ),


    widget.Spacer(
      length=bar.STRETCH,
    ),
    widget.TextBox(
      text='0',
      foreground=third_color[1],
      background=third_color[0]
      ),
    widget.TextBox(
      text='0',
      foreground=color[1],
      background=color[0]
    ),
    widget.TextBox(
      text='0',
      foreground=secondary_color[1],
      background=secondary_color[0]
      ),
    widget.TextBox(
      text='1',
      foreground=third_color[0],
      background=third_color[1]
      ),
    widget.TextBox(
      text='1',
      foreground=color[0],
      background=color[1]
    ),
    widget.TextBox(
      text='1',
      foreground=secondary_color[0],
      background=secondary_color[1]
      ),
    widget.TextBox(
      text='2',
      foreground=third_color[0],
      background=third_color[2]
      ),
    widget.TextBox(
      text='2',
      foreground=color[0],
      background=color[2]
    ),
    widget.TextBox(
      text='2',
      foreground=secondary_color[0],
      background=secondary_color[2]
      ),
    widget.TextBox(
      text='3',
      foreground=third_color[0],
      background=third_color[3]
      ),
    widget.TextBox(
      text='3',
      foreground=color[0],
      background=color[3]
    ),
    widget.TextBox(
      text='3',
      foreground=secondary_color[0],
      background=secondary_color[3]
      ),
    widget.TextBox(
      text='4',
      foreground=third_color[0],
      background=third_color[4]
      ),
    widget.TextBox(
      text='4',
      foreground=color[0],
      background=color[4]
    ),
    widget.TextBox(
      text='4',
      foreground=secondary_color[0],
      background=secondary_color[4]
      ),
    widget.TextBox(
      text='5',
      foreground=third_color[0],
      background=third_color[5]
      ),
    widget.TextBox(
      text='5',
      foreground=color[0],
      background=color[5]
    ),
    widget.TextBox(
      text='5',
      foreground=secondary_color[0],
      background=secondary_color[5]
      ),
    widget.TextBox(
      text='6',
      foreground=third_color[0],
      background=third_color[6]
      ),
    widget.TextBox(
      text='6',
      foreground=color[0],
      background=color[6]
    ),
    widget.TextBox(
      text='6',
      foreground=secondary_color[0],
      background=secondary_color[6]
      ),
    widget.TextBox(
      text='7',
      foreground=third_color[0],
      background=third_color[7]
      ),
    widget.TextBox(
      text='7',
      foreground=color[0],
      background=color[7]
    ),
    widget.TextBox(
      text='7',
      foreground=secondary_color[0],
      background=secondary_color[7]
      ),
    widget.TextBox(
      text='8',
      foreground=third_color[0],
      background=third_color[8]
      ),
    widget.TextBox(
      text='8',
      foreground=color[0],
      background=color[8]
    ),
    widget.TextBox(
      text='8',
      foreground=secondary_color[0],
      background=secondary_color[8]
    ),
    
    ]
  return widgets_list

def screen1_widgets():
    widgets_screen1=init_widgets_list()
    return widgets_screen1

def bar_config(position):
    bar_instance = bar.Bar(
        widgets=screen1_widgets(),
        size=bar_size,
        background=color[0]+"00",
        margin=[bar_margin[0],
                bar_margin[1],
                bar_margin[2],
                bar_margin[3]]
    )
    return {position: bar_instance}

def init_screens_bottom():
    if single_monitor:
        return [Screen(**bar_config("bottom"))]
    else:
        return [Screen(**bar_config("bottom")) for _ in range(get_screen_count())]

def init_screens_top():
    if single_monitor:
        return [Screen(**bar_config("top"))]
    else:
        return [Screen(**bar_config("top")) for _ in range(get_screen_count())]

if bar_position == "top":
    screens=init_screens_top()
else:
  screens=init_screens_bottom()

widgets_list = init_widgets_list()
widgets_screen1 = screen1_widgets()