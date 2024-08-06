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
from custom_widgets import InternetIcon, TemperatureIcon

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
       font=symbols_font,
       decorations=[RectDecoration(colour=secondary_color[0]+"BB", radius=5, filled=True,padding=2)],
       text="",
       foreground=secondary_color[2],
       mouse_callbacks={'Button1':lambda: qtile.function(control_panel)},
    ),

    TemperatureIcon(
       font=symbols_font,
       decorations=[RectDecoration(colour=secondary_color[0]+"BB", radius=5, filled=True,padding=2)],
       foreground=secondary_color[5],
       mouse_callbacks = {'Button1': lambda: qtile.spawn(terminal + " -e zsh -c 'sensors'")},
       update_interval=5, 
       sensor='thermal_zone4'
    ),

    widget.WindowName(
      decorations=[RectDecoration(colour=secondary_color[0]+"BB", radius=5, filled=True,padding=2)],
      foreground=secondary_color[1],
      width=widget_width+100,
      format=' {name}',
      scroll=True,
      scroll_delay=2,
      scroll_repeat=True,
      scroll_step=1,
      empty_group_string=" Empty"
    ),
    
    widget.Chord(
      decorations=[RectDecoration(colour=secondary_color[0]+"BB", radius=5, filled=True,padding=2)],
      foreground=color[3],
    ),
    
    widget.Prompt(
      decorations=[RectDecoration(colour=secondary_color[0]+"BB", radius=5, filled=True,padding=2)],
      prompt=prompt,
      foreground=secondary_color[4],
      cursor_color=secondary_color[4],
      visual_bell_color=[4],
      visual_bell_time=0.2,
    ),
    
    widget.Spacer(
      length=bar.STRETCH,
    ),
    
    widget.GroupBox(
      decorations=[RectDecoration(colour=secondary_color[0]+"BB", radius=5, filled=True,padding=2)],
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
      length=bar.STRETCH,
    ),
    
    widget.Wttr(
        decorations=[RectDecoration(colour=secondary_color[0]+"BB", radius=5, filled=True,padding=2)],
        foreground=secondary_color[1],
        location={'':''},
        update_interval=300,
        format='%c',
        mouse_callbacks={'Button1': lambda: qtile.spawn(terminal + " -e zsh -c 'curl wttr.in; exec zsh'")},
      ),
    
    InternetIcon(
      font=symbols_font,
      decorations=[RectDecoration(colour=secondary_color[0]+"BB", radius=5, filled=True,padding=2)],
      update_interval=5,
      foreground=secondary_color[5],
      mouse_callbacks={'Button1':lambda: qtile.function(network_widget)}
    ),

    VolumeIcon(
      decorations=[RectDecoration(colour=secondary_color[0]+"BB", radius=5, filled=True,padding=2)],
      foreground=secondary_color[4],
      mouse_callbacks={'Button1': lambda: qtile.function(audio_widget),'Button4': lambda: qtile.spawn("amixer -q set Master 5%+ && dunstify -a Volume ' '$(pamixer --get-volume-human) -h int:value:$(pamixer --get-volume)", shell=True),'Button5': lambda: qtile.spawn("amixer -q set Master 5%- && dunstify -a Volume ' '$(pamixer --get-volume-human) -h int:value:$(pamixer --get-volume)", shell=True)},
    ),
    
    widget.Clock(
      decorations=[RectDecoration(colour=secondary_color[0]+"BB", radius=5, filled=True,padding=2)],
      foreground=secondary_color[2],
      format="%H:%M",
      update_interval=1,
      mouse_callbacks={'Button1': lambda: qtile.function(calendar_notification),'Button4': lambda: qtile.function(calendar_notification_prev),'Button5': lambda: qtile.function(calendar_notification_next)},              
    ),
    
    widget.UPowerWidget(
      decorations=[RectDecoration(colour=secondary_color[0]+"BB", radius=5, filled=True,padding=2)],
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
    )
    ]
  return widgets_list

def screen1_widgets():
    widgets_screen1=init_widgets_list()
    return widgets_screen1

def init_screens_bottom():
    return[Screen(bottom=bar.Bar(widgets=screen1_widgets(),size=bar_size,background=color[0]+"77",margin=[bar_margin[0], 200,bar_margin[2],200]))]

def init_screens_top():
    return[Screen(top=bar.Bar(widgets=screen1_widgets(),size=bar_size,background=color[0]+"77",margin=[bar_margin[0], 200,bar_margin[2],200]))]

if bar_position == "top":
    screens=init_screens_top()
else:
  screens=init_screens_bottom()

widgets_list = init_widgets_list()
widgets_screen1 = screen1_widgets()